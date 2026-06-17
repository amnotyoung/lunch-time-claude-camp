"""1단계: koica-reg index.json에서 category별 조문 모음.

3주차 load_data.py와 동일한 어댑터 패턴 — koica_search의 토크나이저 자원
(STOPWORDS, JOSA_RE, _nfc)을 재사용한다.
"""
from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Iterable

import pandas as pd

KOICA_REG_REPO_URL = "https://github.com/amnotyoung/koica-reg-mcp"


def _find_koica_reg_repo() -> Path:
    """koica-reg-mcp repo 경로 자동 탐색.

    우선순위:
      1) 환경변수 KOICA_REG_REPO
      2) 동료별로 흔한 후보 경로들
      3) 못 찾으면 안내 메시지와 함께 종료
    """
    env = os.environ.get("KOICA_REG_REPO")
    if env:
        p = Path(env).expanduser()
        if (p / "data" / "index.json").exists():
            return p
    home = Path.home()
    candidates = [
        home / "Documents" / "Claude" / "Projects" / "koica-reg-mcp",
        home / "Documents" / "koica-reg-mcp",
        home / "koica-reg-mcp",
        Path.cwd() / "koica-reg-mcp",
        Path.cwd().parent / "koica-reg-mcp",
    ]
    for c in candidates:
        if (c / "data" / "index.json").exists():
            return c
    raise SystemExit(
        "koica-reg-mcp repo를 찾을 수 없습니다. 셋 중 하나로 해결:\n"
        f"  1) git clone {KOICA_REG_REPO_URL} ~/koica-reg-mcp\n"
        "  2) KOICA_REG_REPO=/실제/경로 환경변수 설정 후 재실행\n"
        "  3) koica-reg-mcp 폴더를 ~/Documents/ 또는 현재 작업 디렉토리에 두기"
    )


REPO = _find_koica_reg_repo()
INDEX = REPO / "data" / "index.json"

sys.path.insert(0, str(REPO))
from koica_search import STOPWORDS, JOSA_RE, _nfc  # noqa: E402


def load_articles(category: str) -> pd.DataFrame:
    raw = json.loads(INDEX.read_text(encoding="utf-8"))
    rows = [a for a in raw["articles"] if a.get("category") == category]
    if not rows:
        raise SystemExit(f"category={category!r} 에 해당하는 조문이 없습니다.")
    df = pd.DataFrame(rows)[["source", "article", "article_title", "chapter", "body"]]
    df["body"] = df["body"].fillna("")
    return df


def tokenize_body(text: str, extra_stopwords: Iterable[str] = ()) -> list[str]:
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
        if candidate.isdigit():
            continue
        tokens.append(candidate)
    return tokens


def docs_by_source(df: pd.DataFrame) -> pd.DataFrame:
    return (
        df.groupby("source", sort=False)
        .agg(body=("body", lambda s: "\n".join(s)), n_articles=("article", "count"))
        .reset_index()
    )


def list_categories() -> list[tuple[str, int]]:
    raw = json.loads(INDEX.read_text(encoding="utf-8"))
    seen: dict[str, int] = {}
    for a in raw["articles"]:
        c = a.get("category")
        if c:
            seen[c] = seen.get(c, 0) + 1
    return sorted(seen.items(), key=lambda x: -x[1])


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--category")
    p.add_argument("--list-categories", action="store_true")
    p.add_argument("--outdir", default="outputs")
    args = p.parse_args()

    if args.list_categories:
        for cat, n in list_categories():
            print(f"{cat}\t{n}")
        return

    if not args.category:
        raise SystemExit("--category 가 필요합니다. --list-categories 로 목록 확인.")

    out = Path(args.outdir)
    out.mkdir(parents=True, exist_ok=True)

    articles = load_articles(args.category)
    docs = docs_by_source(articles).rename(columns={"source": "doc_id"})
    payload = {
        "category": args.category,
        "n_articles": int(len(articles)),
        "n_docs": int(len(docs)),
        "docs": docs.to_dict(orient="records"),
    }
    target = out / f"{args.category}_docs.json"
    target.write_text(json.dumps(payload, ensure_ascii=False, indent=2), encoding="utf-8")
    print(f"saved {target} (articles={len(articles)}, docs={len(docs)})")


if __name__ == "__main__":
    main()
