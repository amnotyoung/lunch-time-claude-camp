"""KOICA hr 카테고리 조문 로더 + 토크나이저 어댑터."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path
from typing import Iterable

import pandas as pd

REPO = Path("/Users/nddn/Documents/Claude/Projects/koica-reg-mcp")
INDEX = REPO / "data" / "index.json"

sys.path.insert(0, str(REPO))
from koica_search import STOPWORDS, JOSA_RE, _nfc  # noqa: E402


def load_hr_articles() -> pd.DataFrame:
    raw = json.loads(INDEX.read_text(encoding="utf-8"))
    rows = [a for a in raw["articles"] if a.get("category") == "hr"]
    df = pd.DataFrame(rows)[
        ["source", "article", "article_title", "chapter", "body"]
    ]
    df["body"] = df["body"].fillna("")
    return df


def tokenize_body(text: str, extra_stopwords: Iterable[str] = ()) -> list[str]:
    """koica_search.tokenize와 동일 규칙. 단, TF 보존 위해 dedup 제외."""
    stop = set(STOPWORDS) | set(extra_stopwords)
    text = _nfc(text or "")
    tokens: list[str] = []
    for tok in re.split(r"[\s,·、]+", text.strip()):
        tok = tok.strip("().,!?\"'·:;[]【】<>")
        if not tok:
            continue
        stripped = JOSA_RE.sub("", tok)
        candidate = stripped if len(stripped) >= 2 else tok
        if candidate in stop or len(candidate) < 2:
            continue
        # 숫자만 있는 토큰 제거
        if candidate.isdigit():
            continue
        tokens.append(candidate)
    return tokens


def docs_by_source(df: pd.DataFrame) -> pd.DataFrame:
    """규정(source)별 본문을 합쳐 14개 문서로 집계."""
    return (
        df.groupby("source", sort=False)
        .agg(body=("body", lambda s: "\n".join(s)),
             n_articles=("article", "count"))
        .reset_index()
    )
