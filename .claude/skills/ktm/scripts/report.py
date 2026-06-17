"""4단계: 마크다운 보고서 생성.

이전 단계 산출물(docs.json + top_keywords.csv + bars/wordcloud PNG)을
한 장의 마크다운으로 묶는다. 상대 경로로 PNG를 참조하므로 outputs/ 폴더를
통째로 공유하거나 GitHub에 올리면 그대로 렌더링된다.
"""
from __future__ import annotations

import argparse
import json
from datetime import datetime
from pathlib import Path

import pandas as pd

CATEGORY_KO = {
    "hr": "인사",
    "finance": "회계",
    "project": "사업",
    "partnership": "파트너십",
    "law": "법무",
    "volunteer": "봉사단",
    "management": "경영",
}


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--category", required=True)
    p.add_argument("--outdir", default="outputs")
    p.add_argument("--summary-top", type=int, default=10)
    args = p.parse_args()

    out = Path(args.outdir)
    docs_path = out / f"{args.category}_docs.json"
    csv_path = out / f"{args.category}_top_keywords.csv"
    bars_png = f"{args.category}_top_keywords_bars.png"
    wc_png = f"{args.category}_wordcloud.png"

    missing = [p for p in [docs_path, csv_path, out / bars_png, out / wc_png] if not p.exists()]
    if missing:
        raise SystemExit(
            "이전 단계 산출물이 부족합니다: " + ", ".join(str(m.name) for m in missing)
        )

    payload = json.loads(docs_path.read_text(encoding="utf-8"))
    top_kw = pd.read_csv(csv_path)
    cat_ko = CATEGORY_KO.get(args.category, args.category)

    lines: list[str] = []
    lines.append(f"# KOICA {cat_ko}규정 텍스트마이닝 보고서")
    lines.append("")
    lines.append(f"- **카테고리**: `{args.category}` ({cat_ko}규정)")
    lines.append(f"- **분석 대상**: 규정 {payload['n_docs']}건 · 조문 {payload['n_articles']}개")
    lines.append(f"- **생성 시각**: {datetime.now().strftime('%Y-%m-%d %H:%M')}")
    lines.append(f"- **방법**: 규정 단위 TF-IDF, 상위 15 키워드 추출")
    lines.append("")
    lines.append("## 1. 전체 워드클라우드")
    lines.append("")
    lines.append(f"![워드클라우드]({wc_png})")
    lines.append("")
    lines.append(f"## 2. 규정별 상위 키워드 (TOP {args.summary_top})")
    lines.append("")
    lines.append(f"![막대그래프]({bars_png})")
    lines.append("")

    lines.append("## 3. 규정별 키워드 요약")
    lines.append("")
    for src, sub in top_kw.groupby("source", sort=False):
        head = sub.head(args.summary_top)
        kw_inline = " · ".join(f"**{r['keyword']}** ({r['tfidf']:.3f})" for _, r in head.iterrows())
        lines.append(f"### {src}")
        lines.append("")
        lines.append(kw_inline)
        lines.append("")

    lines.append("---")
    lines.append("")
    lines.append("> 생성: ktm (KOICA Text Mining skill). 데이터 출처: koica-reg-mcp.")
    lines.append("")

    target = out / f"{args.category}_report.md"
    target.write_text("\n".join(lines), encoding="utf-8")
    print(f"saved {target}")


if __name__ == "__main__":
    main()
