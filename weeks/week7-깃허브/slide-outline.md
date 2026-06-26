# GitHub로 함께 일해보자 — 이슈, PR, 그리고 머지

## Meta
- **Topic**: 지지난주(week5) 로컬 깃으로 '혼자 저장'한 것을 GitHub에 올려 '함께 협업'한다. 참여자가 강사의 공개 repo(koica-intro)에서 문제를 **직접** 발견(AI가 아니라 사람이) → 이슈와 PR을 **한 번에** 보내고 → 강사가 AI 도움을 받아 리뷰·머지. 명령어 암기 대신 자연어로 Claude Code(코드 탭)에 시킨다.
- **핵심 대비(데크 축)**: 로컬 Git = 내 컴퓨터에서 **나 혼자**(저장·이력·되돌리기) ↔ GitHub = 인터넷에서 **여럿이**(공유·이슈·PR·리뷰·머지)
- **역할 구분(중요)**: **식별은 사람**(KOICA 전문성) · **처리·리뷰는 AI**(이슈·PR 생성, PR 리뷰까지)
- **Target Audience**: ktm·koica-reg·로컬 git까지 직접 해본 비개발자 KOICA 동료 (누적)
- **Tone/Mood**: "혼자 저장에서 함께 협업으로". 어렵지 않게.
- **Slide Count**: 9슬라이드 (30분 — slide 02 로컬↔GitHub 비교 + slide 05 라이브 0단계 + slide 07 이슈+PR 통합 + slide 08 강사 시연)
- **Aspect Ratio**: 16:9 (720pt × 405pt)
- **style**: Bento Grid (week4·5·6 토큰 그대로). navy #1A1A2E / lime #E8FF3B / teal #4ECDC4 / yellow #FFE66D / pink #FF6B9D / off-white #F8F8F2 / gray #A0A0B0
- **금지**: "학생"(→"동료"/주어 생략). 자연어 지시 중심.
- **호칭**: "동료" 또는 주어 생략
- **주차 사실**: 로컬 깃 = **지지난주(week5)** / 지난주 = 에이전트팀(week6) / 이번 = GitHub(week7, 6/22주) / 다음 = 8주차 역할 반전(6/29주)
- **실습 repo**: https://github.com/amnotyoung/koica-intro (KOICA 소개, 의도된 문제 13곳 — 사실·표현·오타·데이터·줄바꿈·링크). 정답노트는 비공개.
- **협업 방식**: Fork → PR. 계정·인증은 세션 0단계 라이브(`gh auth login`). 코드 탭 내장 터미널에서 `git`/`gh` 실행.

## 사실 근거
- 공개(public) repo = **읽기**는 누구나, **쓰기(push)는 권한 필요**. 이슈는 계정만 있으면 누구나, PR은 본인 **fork**에서.
- 이슈·PR 생성, PR 리뷰 모두 자연어로 시키면 Claude Code가 `gh`로 수행. (메커니즘 1회 리허설로 검증 완료)
- 다음 주(8주차): 역할 반전 — 참여자가 repo 주인, 이슈를 내는 건 사람이 아니라 AI(Claude·Codex·Gemini).

## Slide Composition

### Slide 01 — Cover
- Title: GitHub로 함께 일해보자 / Subtitle: Collaborate on GitHub · 이슈 · PR · 머지
- Badge: SESSION 07 · WEEK 07 · 2026.6.22주

### Slide 02 — 지지난주 로컬 Git ↔ 오늘 GitHub (핵심 대비) ★요청
- hero: "혼자 저장에서 → 함께 협업으로"
- 로컬 Git(**지지난주**): 내 컴퓨터·나 혼자. commit·이력·되돌리기·브랜치 = 시간여행. "내가 언제 뭘 바꿨지?"
- GitHub(오늘): 인터넷·여럿이. 올리고 이슈·PR·리뷰·머지 = 제안·검토해 합침. "누가 뭘 제안했고, 합칠까?"
- band: 로컬=시간(혼자) ↔ GitHub=사람(함께). 같은 git, 무대만 내 PC→인터넷

### Slide 03 — GitHub 4가지 핵심 개념
- 원격 저장소 / 이슈(건의함) / PR(수정 제안서) / 머지(채택). foot: 알리고→고쳐 보내고→채택 한 바퀴

### Slide 04 — 오늘의 미션 한 바퀴 (플로우)
- repo → ① 직접 찾기(동료) → ② 이슈+PR 한 번에(동료, AI가 실행) → ③ 리뷰·머지(강사, AI 도움) → 반영 ✓
- foot: 지지난주 '혼자 커밋' → 오늘 '함께 머지'. ①② 동료 / ③ 강사

### Slide 05 — 0단계: 준비 (라이브)
- "내 GitHub에 로그인하게 도와줘"(`gh auth login`). gh 없으면 "gh 설치해줘"
- 체크포인트: `gh auth status` "Logged in". 임계경로(먼저 끝낸 동료는 repo 구경)

### Slide 06 — 1단계: 직접 찾기 (내 눈으로) ★수정
- **AI에게 "찾아줘" 하지 않는다 — 이상함을 알아채는 건 사람의 몫(KOICA 전문성)**. repo를 열어 직접 읽는다
- 결: 사실·표현·오타·데이터·형식 무엇이든
- foot: **하나만 잡아도 좋다 — 단 많이 잡을수록 더 좋다** (13곳 숨어있음)

### Slide 07 — 2단계: 이슈 + PR, 한 번에 ★통합(구 7+8)
- 발화: "내가 찾은 이 문제, 이슈로 올리고 fork해서 고쳐 PR까지 보내줘"
- 식별은 내가 / 처리는 AI가 — Claude가 이슈 + fork·수정·PR을 한 번에
- 강사는 이슈(무엇이·왜) + PR(수정안)을 함께 받음
- 왜 동시에? AI를 쓰면 문제를 짚는 순간 해결책도 같이 나온다. **AI가 못 고치면 우리 수준에서도 어렵다** — 나눌 이유 없음. (공개=읽기 → 내 fork에서 제안)

### Slide 08 — 강사의 화면 — 리뷰까지 AI가 ★수정
- 받은 이슈/PR: 누가 무엇을(자동 기록) → "이 PR 리뷰해줘"(AI가 요약·문제점·머지 가능 여부) → 좋으면 Merge
- 핵심: **원래 PR 리뷰는 코드를 꼼꼼히 읽고 신중히 판단하는 가장 어려운 일 — 이제 그것조차 AI가 도와준다**

### Slide 09 — 마무리 + 다음 주차
- Today: ①직접 찾기 ②이슈+PR ③리뷰·머지 ✓ — 식별은 사람, 처리·리뷰는 AI. 로컬(혼자)→GitHub(함께)
- Next: 8주차(6/29주) 역할 반전 — 내가 repo 주인, 이슈는 AI(Claude·Codex·Gemini)가 제기
- reassure: 올리고·알리고·합치는 감각 하나면 충분. 차차 learning by doing
