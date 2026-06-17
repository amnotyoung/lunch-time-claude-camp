"""3단계: TF-IDF CSV → 막대그래프 그리드 + 워드클라우드 PNG.

3주차 노트북 셀 7~8을 그대로 이식.
한국어 폰트: macOS AppleGothic 기본. Windows라면 KOREAN_FONT 경로를
Malgun Gothic 등으로 바꾸면 된다.
"""
from __future__ import annotations

import argparse
import json
import math
import sys
from pathlib import Path

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import rcParams
from wordcloud import WordCloud

if sys.platform == "darwin":
    KOREAN_FONT = "/System/Library/Fonts/Supplemental/AppleGothic.ttf"
    rcParams["font.family"] = "AppleGothic"
elif sys.platform.startswith("win"):
    KOREAN_FONT = "C:/Windows/Fonts/malgun.ttf"
    rcParams["font.family"] = "Malgun Gothic"
else:
    KOREAN_FONT = "/usr/share/fonts/truetype/nanum/NanumGothic.ttf"
    rcParams["font.family"] = "NanumGothic"
rcParams["axes.unicode_minus"] = False


def main() -> None:
    p = argparse.ArgumentParser()
    p.add_argument("--category", required=True)
    p.add_argument("--outdir", default="outputs")
    p.add_argument("--bar-top", type=int, default=10)
    p.add_argument("--max-words", type=int, default=200)
    args = p.parse_args()

    out = Path(args.outdir)
    csv_path = out / f"{args.category}_top_keywords.csv"
    weights_path = out / f"{args.category}_term_weights.json"
    if not csv_path.exists() or not weights_path.exists():
        raise SystemExit("mine.py 산출물이 없습니다. 먼저 mine.py 를 실행하세요.")

    top_kw = pd.read_csv(csv_path)
    sources = list(top_kw["source"].unique())
    ncol = 2
    nrow = max(1, math.ceil(len(sources) / ncol))
    fig, axes = plt.subplots(nrow, ncol, figsize=(13, 3 * nrow))
    axes = axes.flatten() if hasattr(axes, "flatten") else [axes]
    for ax, src in zip(axes, sources):
        sub = top_kw[top_kw["source"] == src].head(args.bar_top).iloc[::-1]
        ax.barh(sub["keyword"], sub["tfidf"], color="steelblue")
        ax.set_title(src, fontsize=11)
        ax.tick_params(axis="y", labelsize=9)
    for ax in axes[len(sources):]:
        ax.axis("off")
    plt.tight_layout()
    bars_path = out / f"{args.category}_top_keywords_bars.png"
    plt.savefig(bars_path, dpi=140, bbox_inches="tight")
    plt.close(fig)

    weights = json.loads(weights_path.read_text(encoding="utf-8"))
    wc = WordCloud(
        font_path=KOREAN_FONT,
        width=1200,
        height=700,
        background_color="white",
        max_words=args.max_words,
        colormap="tab20",
    ).generate_from_frequencies(weights)
    wc_path = out / f"{args.category}_wordcloud.png"
    wc.to_file(str(wc_path))

    print(f"saved {bars_path}")
    print(f"saved {wc_path}")


if __name__ == "__main__":
    main()
