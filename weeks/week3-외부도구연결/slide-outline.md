# 더 많은 외부 서비스 및 도구를 연결해보자

## Meta
- **Topic**: 외부 서비스·도구를 Claude에 연결하는 두 가지 방식 — koica-reg-mcp 실습으로 패턴 익히기
- **Target Audience**: Week 1·2 수강자, Claude 코드 입문자 (KOICA 직원 맥락)
- **Tone/Mood**: 깔끔하고 실용적, 누적 실습의 첫 주답게 손에 잡히는 결과물 강조
- **Slide Count**: 10슬라이드 (Codex 곁다리 1장 + Python 설치 1장 포함)
- **Aspect Ratio**: 16:9 (720pt × 405pt)
- **style**: bento-grid
- **Cumulative Note**: 이번 주부터 누적 실습 시작. 이번 주 결과물(koica-reg 연결 + 조문 검색·인용 검증 체험 + Python 환경)이 4주차(나만의 스킬: 코이카 규정 텍스트 마이닝)의 시작점이 됨.

## Slide Composition

### Slide 1 — Cover
- **Type**: Cover
- **Title**: 더 많은 외부 서비스 및 도구를 연결해보자
- **Subtitle**: External Connectors · Two Ways
- **Background**: #000000
- **Badge**: SESSION 03 (blue pill #0066cc)

### Slide 2 — 두 연결 방식 한눈에
- **Type**: Conceptual (split)
- **Key Message**: 외부 도구를 Claude에 붙이는 길은 두 갈래
- **Details**:
  ┌─ 방식 ①: 앱 내장 커넥터 ──────┐  ┌─ 방식 ②: GitHub repo ──────────┐
  │ Claude 앱에서 클릭 한 번        │  │ "이 주소 도구 설치해줘" + URL  │
  │ 검증된 인기 도구                │  │ 최신·다양한 도구              │
  │ 사례: Desktop Commander         │  │ 사례: koica-reg-mcp            │
  └─────────────────────────────────┘  └─────────────────────────────────┘
- **Footnote**: "이런 연결 방식을 MCP라 부릅니다" (DC는 채팅 탭용 — 코드 탭엔 이미 내장)
- **Background**: #f5f5f7

### Slide 3 — GitHub 도구 연결 + Node.js 점검 (Win/Mac)
- **Type**: Content (split)
- **Key Message**: 코드 탭이 GitHub 도구를 자동 설치, 막히면 Node.js 점검
- **Details**:
  ┌─ 정상 설치된 분들 ──────────────────────────┐
  │ 코드 탭에 "이 GitHub 도구 연결해줘"           │
  │ → 이게 방식 ①                                │
  └─────────────────────────────────────────────┘
  ┌─ 설치가 막힌 분들 — OS별 차이는 ②뿐 ────────┐
  │ ① Node.js 직접 설치                          │
  │   → nodejs.org/ko → LTS 다운로드 → 설치     │
  │ ② 터미널 열기                                │
  │   - Windows: PowerShell (또는 cmd)           │
  │   - Mac: 터미널(Terminal)                    │
  │ ③ 한 줄 입력 (양 OS 동일):                   │
  │   nodejs.org/ko → LTS 설치 후 코드 탭 재시작 │
  │ ④ Claude 앱 재시작 → 커넥터 목록에서 확인    │
  └─────────────────────────────────────────────┘
- **Background**: #ffffff

### Slide 4 — 코드 탭으로 Python 한 줄 설치
- **Type**: Practice (live demo)
- **Key Message**: 코드 탭이라면 Python 설치도 한 줄로 끝
- **Details**:
  - 명령: `"python 설치해줘"` — Claude가 OS(Win/Mac) 알아서 처리
  - 왜: 다음 주 "나만의 스킬"의 재료. 스킬다운 스킬엔 코드 실행이 필요(Python이 가장 보편)
  - 확인: `"python 버전 확인해줘"` → Python 3.x.x
- **Cumulative Note**: 수업 시간 안에 설치까지 끝내고 마무리 (숙제 없음 원칙)
- **Background**: bento-grid (yellow main + coral why + teal check)

### Slide 5 — 방식 ② 본격: koica-reg-mcp 연결
- **Type**: Content
- **Key Message**: GitHub 주소만 알려주면 Claude가 알아서 설치한다
- **Prereq (한 줄)**: 코드 탭이면 바로 OK — Node.js만 준비돼 있으면 됨
- **Details**:
  - "이 GitHub 주소의 도구를 연결해줘" + github.com/amnotyoung/koica-reg-mcp
  - Claude가 clone → 의존성 설치 → 커넥터 등록까지
  - 연결 확인 명령: "koica-reg 잘 연결됐는지 확인해줘"
- **Why koica-reg**: KOICA 규정 38개·1,660 조문을 자연어로 — 규정 PDF Ctrl+F 시대 종료
- **Background**: #272729 (dark)

### Slide 6 — 실습 ①: 조문 검색 + 본문 조회
- **Type**: Practice (live demo)
- **Key Message**: 자연어 한 줄 → 정확한 조문과 본문이 즉시
- **Details**:
  - 명령 예: "KOICA 인사규정 채용 결격사유 알려줘"
  - Claude가 search_regulation → get_article 자동 호출
  - 산출물: 정답 조문 1건 (예: 인사규정 제19조 본문 전체)
  - 본인 업무 주제로 자유 — "국외여비 일비 기준" / "사업평가 절차" 등
- **Cumulative**: 4주차(스킬 만들기)에서 이 호출 패턴을 슬래시 명령 하나로 묶을 예정
- **Background**: #ffffff

### Slide 7 — 실습 ②: 인용 검증 + 상호참조
- **Type**: Practice (live demo)
- **Key Message**: 보고서·답변에 들어간 인용이 진짜로 존재하는지 확인
- **Details**:
  - 명령 예 1: "이 문장 인용이 맞는지 검증해줘" → verify_citation (ok / not_found / unknown_source)
  - 명령 예 2: "직제규정 제9조를 인용한 다른 규정 다 찾아줘" → find_references (incoming 그래프)
  - 결과: LLM 환각 방지 + 규정 간 상호참조 자동 추적
- **Background**: #f5f5f7

### Slide 8 — 같은 방식 ②로 연결되는 도구들
- **Type**: Gallery (4-tile)
- **Key Message**: 한 패턴을 익히면 생태계 전체가 열린다
- **Details** (4 tiles):
  - **sqlite** — 데이터베이스 다루기
  - **zotero** — 학술 문헌 관리
  - **tiro** — 음성→텍스트, 회의록
  - **slides-grab** — 슬라이드 자동 제작 (이 슬라이드도 이걸로 빌드)
- **Closing line**: "본인 업무 분야 도구도 GitHub에 있으면 같은 방식으로"
- **Background**: #1d1d1f (dark)

### Slide 9 — Codex 사용자라면 (곁다리)
- **Type**: Sidebar / Parallel Path
- **Key Message**: 오늘 배운 패턴은 Claude Code 외 Codex CLI에서도 동일하게 통한다
- **Details**:
  - Codex CLI = OpenAI 진영의 터미널 AI 에이전트 (Claude Code 대응)
  - 같은 MCP 서버를 동일 방식으로 연결 가능 (koica-reg 포함, `codex mcp add` 명령)
  - 공통점: Codex도 코드 탭처럼 셸 실행 권한이 내장 → 별도 도구 불필요
  - 즉 추가 설치 없이 슬라이드 4부터 같은 흐름
- **Audience**: 이번 분기 ChatGPT만 구독 중인 분들
- **Tone**: 짧고 안심시키는 톤 — "본 흐름과 동일, 손해 없음"

### Slide 10 — 다음 주 예고 & 클로징
- **Type**: Closing
- **Message**: 나만의 스킬을 만들어 보자 — 코이카 규정 텍스트 마이닝
- **Details**: 오늘 연결한 koica-reg + Python으로 규정 원문을 텍스트 마이닝하는 나만의 스킬
- **Background**: #000000
