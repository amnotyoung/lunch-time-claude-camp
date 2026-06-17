# 나만의 스킬을 만들어보자 — 예시 ktm

## Meta
- **Topic**: 나만의 스킬을 만드는 법 — 자연어 한 마디로 조회·분석·시각화·보고서까지 도는 다단계 스킬. 예시는 ktm.
- **Target Audience**: 3주차에 koica-reg + Python으로 자연어 텍스트마이닝을 함께 돌려본 KOICA 동료
- **Tone/Mood**: "스킬 만들기는 이렇게 쉽다"는 감각 전달. ktm 자체는 부수적.
- **Slide Count**: 7슬라이드 (30분)
- **Aspect Ratio**: 16:9 (720pt × 405pt)
- **style**: Bento Grid 메인 유지. Slide 02(Swiss) · Slide 05(timeline)만 컴포넌트 변형.
- **금지 단어**: "노트북", "Jupyter", "ipynb", "셀"
- **호칭**: "동료" 또는 주어 생략 ("학생" 금지)

## Slide Composition

### Slide 01 — Cover
- **Type**: Cover (기존 유지)
- **Title**: 나만의 스킬을 만들어보자
- **Subtitle**: Make Your Own Skill · 예시 ktm
- **Badge**: SESSION 04 · 2026.5.25주

### Slide 02 — Claude 확장은 3종 (커넥터·스킬·플러그인)
- **Type**: Bento + Swiss International (3-column 비교)
- **Key Message**: 같은 앱 안 세 가지 확장 — 오늘은 그중 "스킬"을 만든다
- **3열 비교**:
  | 종류 | 무엇 | 우리가 아는 것 | 비유 |
  |---|---|---|---|
  | **커넥터** | 외부 도구·서비스 연결(MCP) | koica-reg, SQLite, Word/PPT | 손·발 — 외부와 닿는 통로 |
  | **스킬** | 다단계 작업 절차 패키지 | 오늘 만들 ktm | 일하는 방법 — 어떻게 시킬지 |
  | **플러그인** | 스킬·명령어·훅 묶음 | codex, anthropic-skills | 한 보따리 |
- **One-liner**: "커넥터로 닿고, 스킬로 묶고, 플러그인으로 모은다"
- **Footer**: "**3주차 = 외부 연결 체험** / 오늘 = 스킬" · `02 / 07`

### Slide 03 — SKILL.md 표준 + 풀 구조 + 설치 위치
- **Type**: Bento (anchor + 4-tile)
- **Key Message**: SKILL.md 1장이 필수, 나머지는 보조. user/project level 둘 다 가능.
- **Anchor (좌)**: 풀 폴더 구조 + frontmatter 예시 (ktm)
  ```
  my-skill/
  ├── SKILL.md
  ├── template.md
  ├── examples/
  └── scripts/
  ```
- **4타일** (우):
  - **설치 위치 2종**: `~/.claude/skills/<이름>/` (user) **또는** `<프로젝트>/.claude/skills/<이름>/` (project)
  - SKILL.md 1장이 필수
  - 트리거는 **description에 키워드를 충분히** 적어두면 평소 한국어 발화에 잘 걸림
  - 개방 표준 — Claude Code · Codex · Antigravity
- **Footer**: `03 / 07`

### Slide 04 — 변환 지시: 짧은 자연어 한 줄로 충분 (폴더 경로만 함께)
- **Type**: Bento (prompt + 결과 + 사전 준비)
- **Key Message**: 어렵게 시킬 필요 없음 — 폴더 경로 한 자리만 채우면 Claude가 알아서 만든다
- **변환 명령 (placeholder)**:
  ```
  3주차에 만든 분석 파일 폴더
  [내 경로]를 활용해서 ktm 스킬 만들어줘.

  카테고리 받아서 koica-reg 조회 →
  키워드 마이닝 → 그래프 →
  마크다운 보고서까지 한 번에 도는
  걸로.
  ```
- **결과 패키지** (참고):
  ```
  ktm/
  ├── SKILL.md
  ├── scripts/ (fetch · mine · viz · report)
  ├── examples/hr_sample/
  └── README.md
  ```
- **사전 준비 3항목**:
  - ① 3주차 분석 파일 폴더 — 강사가 zip으로 공유
  - ② koica-reg MCP 설치 — 3주차에 연결한 그대로
  - ③ Python 설치 — 3주차의 "python 설치해줘" 한 줄로 재확인
- **Footer**: "약 7분, 직접 입력해 함께 본다" · `04 / 07`

### Slide 05 — 자연어 한 줄 → 4단계 자동 (보고서까지)
- **Type**: Bento + horizontal timeline (4-step)
- **Key Message**: 평범한 한국어 한 마디로 4단계가 자동 — 마지막에 **보고서**까지
- **대표 발화**: `"인사규정 핵심 보고서 만들어줘"`
- **다른 표현도 OK**:
  - "회계 규정 텍스트마이닝 보고서"
  - "사업 분야 핵심 키워드 보고서"
  - "파트너십 규정 분석 정리해줘"
- **4단계 timeline**:
  ```
  [1] 조회 (fetch.py)   → koica-reg 카테고리 조문 모음
  [2] 마이닝 (mine.py)  → TF-IDF 상위 키워드 CSV
  [3] 시각화 (viz.py)   → 막대그래프 + 워드클라우드 PNG
  [4] 보고서 (report.py) → outputs/<카테고리>_report.md
  ```
- **카테고리 자동 인식**: 인사→hr / 회계→finance / 사업→project / 파트너십→partnership / 법무→law / 봉사단→volunteer / 경영→management
- **Footer**: "**한 줄 발화 → 보고서까지 자동**. Codex / Antigravity에서도 같은 폴더 그대로 작동" · `05 / 07`

### Slide 06 — Codex / Antigravity 사용자라면 (곁다리)
- **Type**: Bento 3-tile
- **Key Message**: SKILL.md는 개방 표준 — 만든 ktm 폴더를 그대로 옮기면 됨
- **3타일**:
  - **Codex CLI**: `~/.codex/skills/ktm/`에 복사 또는 심볼릭 링크
  - **Antigravity**: 도구 설정에서 "스킬 폴더 위치" 확인 후 같은 패키지 두기
  - **차이점 한 줄**: 실행 환경(셸 권한·MCP 연결 방식)은 도구별 약간 다름
- **Footer**: "ChatGPT만 / Antigravity로 옮긴 분도 본 흐름 그대로" · `06 / 07`

### Slide 07 — 마무리: 만드는 법을 익혔다
- **Type**: Closing (우측 1칸 확대)
- **Key Message**: 오늘 가져갈 것은 ktm이 아니라 **"스킬은 이렇게 만든다"는 감각**
- **Details**:
  - 좌측 anchor: 익힘 + ktm은 예시일 뿐 + skillsmp 둘러보기 한 줄
  - 우측(전체 칸): 다음 주차(6월08일주 Git) — 만든 스킬을 git으로 버전 관리
  - 한 달 뒤(6월22일주) 카드는 노출 안 함 (강사용 PLAN에만 유지)
- **Footer**: `07 / 07`
