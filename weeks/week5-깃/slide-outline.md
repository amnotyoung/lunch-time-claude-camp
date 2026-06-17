# 깃(Git)이란 무엇인가 — 자연어로 다루는 버전 관리

## Meta
- **Topic**: 로컬 git으로 버전 관리하기. 명령어를 외우지 않고 자연어로 Claude Code를 통해 다룬다. 실습 대상은 week4에서 만든 ktm 스킬.
- **Target Audience**: week4에서 ktm 스킬을 직접 만들어본 비개발자 KOICA 동료
- **Tone/Mood**: "git은 어렵지 않다 — 자연어로 충분하다". 되돌릴 수 있다는 안심.
- **Slide Count**: 7슬라이드 (30분)
- **Aspect Ratio**: 16:9 (720pt × 405pt)
- **style**: Bento Grid 메인. Slide 05만 week4 timeline 컴포넌트 차용.
- **금지**: GitHub·원격(remote)·push/clone·pull 언급 없음 (6월22일주 별도). "학생" 금지.
- **호칭**: "동료" 또는 주어 생략

## Slide Composition

### Slide 01 — Cover
- Title: 깃(Git)이란 무엇인가
- Subtitle: Version Control · 자연어로 다루는 버전 관리
- Badge: SESSION 05 · WEEK 05 · 2026.6.08주 · 점심시간 클로드 캠프

### Slide 02 — 왜 git인가: 버전 관리가 필요한 순간
- Key Message: `ktm_최종.py`, `ktm_최종_진짜최종.py` … 파일명 버전 관리의 한계 → git이 대신
- 3 pain: ① 되돌리기 ② 기록 ③ 실험
- 보조: git은 텍스트 파일(.py/.md/설정)에 적합, 바이너리(.png/.pdf/.xlsx)는 부적합
- One-liner: "git = 폴더의 타임머신"

### Slide 03 — git 핵심 개념 3개 (저장소·커밋·이력)
- Key Message: 외울 건 딱 3개. 명령어는 안 외워도 됨 — 자연어로 시키면 Claude가 git 명령 대신 실행
- 저장소(repository) / 커밋(commit=스냅샷, 세이브 포인트) / 이력(history/log)
- 커밋 ID(해시): 커밋마다 고유 ID → log로 이력 확인, 커밋 ID 기준 revert

### Slide 04 — 시작: ktm 폴더를 저장소로 만들기
- 발화: "이 폴더 git으로 버전 관리 시작해줘" + [ktm 폴더 경로]
- 뒤에서: git init → git add . → git commit
- .gitignore: 추적 안 할 것 (outputs/·*.png·*.pdf·__pycache__/·.DS_Store·.env)
- 사전 준비: ① git 설치("git 설치해줘") ② 대상 = ktm 폴더

### Slide 05 — 실습: ktm을 더 개발하며 버전 남기기 (4단계 timeline)
- 대표 발화: "ktm에 그래프 색 바꾸고 새 카테고리 추가해줘"
- [1] 개선 → [2] 저장(commit) → [3] 이력(log) → [4] 되돌리기(restore/revert)
- 팁: "주요 작업마다 안 시켜도 알아서 커밋해"

### Slide 06 — 자연어 ↔ git 대응표 + 브랜치
- 대응표 5줄: 저장해줘 / 뭐 바뀌었어 / 이력 보여줘 / 되돌려줘 / 실험용으로 따로
- 브랜치: 실험용 평행 우주

### Slide 07 — 마무리 + 다음 주차
- Today: 버전 관리 감각 익힘 ✓
- Next: 6월15일주 — 에이전트와 서브 에이전트
