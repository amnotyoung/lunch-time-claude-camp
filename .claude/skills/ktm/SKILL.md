---
name: ktm
description: KOICA 규정 텍스트마이닝 보고서 스킬. category(hr/finance 등) 단위로 koica-reg 조문을 모아 TF-IDF 상위 키워드를 뽑고, 막대그래프·워드클라우드 PNG를 만든 뒤 마크다운 보고서 한 장으로 묶는다. 트리거 키워드 — "인사규정 핵심 보고서 만들어줘", "회계 규정 텍스트마이닝 보고서", "사업 분야 핵심 키워드 보고서", "파트너십 규정 분석 정리해줘", "ktm 스킬로 분석". 사용자가 koica-reg 데이터의 특정 category에 대해 키워드 분석 보고서를 보고 싶어 할 때 사용.
---

# ktm — KOICA Text Mining (보고서까지)

4주차(5월25일주) 점심시간 클로드 캠프 데모 스킬. 3주차에 노트북으로 돌렸던 TF-IDF 분석을 자연어 한 마디로 재실행하고, 마지막에 **마크다운 보고서**까지 자동으로 묶어주는 다단계 스킬.

## 워크플로 (4단계)

사용자 입력에서 **category 키워드**(예: "인사" → `hr`, "회계" → `finance`)를 추출한 뒤 아래 순서로 실행한다.

1. **조회** — `python scripts/fetch.py --category <CATEGORY>` — koica-reg-mcp의 `data/index.json`에서 해당 category 조문을 모아 `outputs/<category>_docs.json`에 저장.
2. **키워드 마이닝** — `python scripts/mine.py --category <CATEGORY> --top 15` — TF-IDF로 규정(source) 단위 상위 키워드를 뽑아 `outputs/<category>_top_keywords.csv` 생성.
3. **시각화** — `python scripts/viz.py --category <CATEGORY>` — 규정별 막대그래프(`<category>_top_keywords_bars.png`) + 전체 워드클라우드(`<category>_wordcloud.png`) 생성.
4. **보고서** — `python scripts/report.py --category <CATEGORY>` — 위 산출물을 한 장의 마크다운으로 묶어 `outputs/<category>_report.md` 생성.

마지막에 Claude는 보고서 경로와 핵심 키워드를 간단히 표로 정리해서 사용자에게 보여준다.

## 카테고리 한국어 매핑

자연어 발화에서 다음 매핑으로 `--category` 인자를 결정:
- 인사 → `hr`
- 회계 → `finance`
- 사업 → `project`
- 파트너십 → `partnership`
- 법무 → `law`
- 봉사단 → `volunteer`
- 경영 → `management`

매핑이 모호하면 `python scripts/fetch.py --list-categories`로 사용 가능한 목록 출력 후 사용자에게 확인.

## 의존성

- Python 3.10+
- 패키지: `pandas`, `scikit-learn`, `matplotlib`, `wordcloud`
- 외부 레포: koica-reg-mcp (week3에서 연결한 그 도구). `fetch.py`가 `KOICA_REG_REPO` 환경변수 → `~/Documents/Claude/Projects/koica-reg-mcp` → `~/Documents/...` → cwd 순으로 `data/index.json`을 자동 탐색한다. 이 환경에서는 `/Users/nomadresearch/Documents/Claude/Projects/koica-reg-mcp`로 자동 인식됨. 못 찾으면 안내 메시지에 따라 `git clone https://github.com/amnotyoung/koica-reg-mcp` 또는 환경변수 지정.
- 폰트: macOS `AppleGothic` 기본 (Windows는 `Malgun Gothic` 자동 fallback, viz.py 안에서 sys.platform 분기)

## 출력 위치

스킬은 호출된 작업 디렉토리의 `outputs/` 폴더에 산출물을 만든다. 작업 디렉토리가 비어 있으면 `~/ktm-runs/<timestamp>/`를 만들어 사용한다(현재는 단순히 cwd/outputs/ 사용 — 필요 시 Claude가 mkdir).

## 사용 예시

```
# 사용자: "인사규정 핵심 보고서 만들어줘"
cd ~/.claude/skills/ktm
python scripts/fetch.py --category hr
python scripts/mine.py --category hr --top 15
python scripts/viz.py --category hr
python scripts/report.py --category hr
# → outputs/hr_report.md 생성
```

견본 산출물은 `examples/hr_sample/` 참조.
