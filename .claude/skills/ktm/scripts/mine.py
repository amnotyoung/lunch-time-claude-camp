"""2단계: 카테고리별 조문 → TF-IDF 상위 키워드 CSV.

3주차 노트북 셀 4~6을 그대로 이식.
"""
from __future__ import annotations

import argparse
import json
from pathlib import Path

import numpy as np
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer

from fetch import tokenize_body

DOMAIN_STOPWORDS = {
    "협력단", "이사장", "다음", "각호", "경우", "대하여", "관하여", "관한", "대한",
    "있다", "한다", "하는", "따라", "따른", "관련", "이상", "이하", "하여", "하여야",
    "본다", "본조", "제1항", "제2항", "제3항", "해당", "아니", "아니한다", "아니하다",
    "그러하지", "같다", "이를", "이에", "또는", "및", "등의", "및의",
}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--category", required=True)
    p.add_argument("--outdir", default="outputs")
    p.add_argument("--top", type=int, default=15)
    args = p.parse_args()

    out = Path(args.outdir)
    docs_path = out / f"{args.category}_docs.json"
    if not docs_path.exists():
        raise SystemExit(f"{docs_path} 가 없습니다. 먼저 fetch.py 를 실행하세요.")

    payload = json.loads(docs_path.read_text(encoding="utf-8"))
    docs = pd.DataFrame(payload["docs"])
    docs["tokens"] = docs["body"].apply(lambda t: tokenize_body(t, DOMAIN_STOPWORDS))
    corpus = docs["tokens"].apply(" ".join).tolist()

    vec = TfidfVectorizer(
        tokenizer=str.split,
        preprocessor=lambda x: x,
        lowercase=False,
        token_pattern=None,
        min_df=2,
        max_df=0.9,
    )
    X = vec.fit_transform(corpus)
    vocab = np.array(vec.get_feature_names_out())

    rows = []
    for i, doc_id in enumerate(docs["doc_id"]):
        row = X[i].toarray().ravel()
        top_idx = row.argsort()[::-1][: args.top]
        for rank, j in enumerate(top_idx, 1):
            if row[j] == 0:
                break
            rows.append(
                {"source": doc_id, "rank": rank, "keyword": vocab[j], "tfidf": float(row[j])}
            )

    top_kw = pd.DataFrame(rows)
    target = out / f"{args.category}_top_keywords.csv"
    top_kw.to_csv(target, index=False, encoding="utf-8")

    weights = {}
    X_dense = X.toarray()
    max_score = X_dense.max(axis=0)
    for term, w in zip(vocab, max_score):
        if w > 0:
            weights[term] = float(w)
    weights_path = out / f"{args.category}_term_weights.json"
    weights_path.write_text(
        json.dumps(weights, ensure_ascii=False, indent=2), encoding="utf-8"
    )

    print(f"saved {target} (rows={len(top_kw)})")
    print(f"saved {weights_path} (terms={len(weights)})")


if __name__ == "__main__":
    main()
