# ktm — KOICA Text Mining

자연어 한 마디로 KOICA 규정 카테고리 조회 + TF-IDF 키워드 분석 + 그래프·워드클라우드 + 마크다운 보고서까지 한 번에 만들어주는 Claude 스킬.

## 빠른 시작

Claude Code에서:

> "인사규정 핵심 보고서 만들어줘"

또는 직접 셸에서:

```bash
cd ~/.claude/skills/ktm
mkdir -p outputs
python scripts/fetch.py  --category hr
python scripts/mine.py   --category hr --top 15
python scripts/viz.py    --category hr
python scripts/report.py --category hr
open outputs/hr_report.md
```

## 산출물

| 파일 | 내용 |
|---|---|
| `outputs/<cat>_docs.json` | 카테고리 조문 모음 |
| `outputs/<cat>_top_keywords.csv` | 규정 단위 TOP 15 키워드 |
| `outputs/<cat>_top_keywords_bars.png` | 규정별 막대그래프 그리드 |
| `outputs/<cat>_wordcloud.png` | 전체 워드클라우드 |
| `outputs/<cat>_report.md` | 위 4가지를 묶은 마크다운 보고서 |

## 카테고리

`hr` (인사) · `finance` (회계) · `project` (사업) · `partnership` (파트너십) · `law` (법무) · `volunteer` (봉사단) · `management` (경영)

전체 목록과 조문 수: `python scripts/fetch.py --list-categories`

## 트러블슈팅

- **워드클라우드 한국어 깨짐 (Windows/Linux)**: `viz.py` 안 `KOREAN_FONT` 경로를 본인 OS의 한글 폰트로 수정.
- **`koica_search` import 실패**: `koica-reg-mcp` 레포 경로(`fetch.py` 상단 `REPO`)를 본인 환경에 맞게 수정.
- **`min_df` 에러**: 카테고리 조문이 너무 적을 때 발생. 더 큰 카테고리로 시도.
