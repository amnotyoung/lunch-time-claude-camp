# 클로드 코드 사용 환경을 구성해보자

## Meta
- **Topic**: 클로드 코드(데스크톱 앱의 '코드' 탭) 사용 환경 구성 — 설치부터 코드 탭 이해, 준비물, 설정까지
- **Target Audience**: Week 1 수강자, Windows 사용자, 클로드 코드 입문자
- **Tone/Mood**: 깔끔하고 고급스럽게, 단계별로 명확하게
- **Slide Count**: 8슬라이드
- **Aspect Ratio**: 16:9 (720pt × 405pt)
- **Style**: custom — Apple design system. Colors: canvas #ffffff, parchment #f5f5f7, ink #1d1d1f, accent blue #0066cc, dark tile #272729, pure black #000000, muted #7a7a7a. Font: system-ui, -apple-system, Helvetica Neue — weight 600 headlines (letter-spacing -0.3~-0.5pt), weight 400 body, weight 300 for airy subtitles. Shapes: pill border-radius (9999pt) for badges/CTAs, 14pt radius for utility cards. No decorative gradients, no shadows on UI. Elevation via surface color change (light ↔ dark). Cover and closing: pure black background. Workspace: parchment #f5f5f7. Installation/settings: white #ffffff. Dark content slides: #272729 or #1d1d1f.
- **Design Reference**: DESIGN.md (Apple — awesome-design-md, installed at slides/week2-환경구성/DESIGN.md)

## Slide Composition
> 실제 슬라이드(slide-01~08.html)가 정본. 아래는 그에 맞춘 구성 요약.

### Slide 1 — Cover
- **Type**: Cover
- **Title**: 클로드 코드 사용 환경을 구성해보자
- **Subtitle**: Claude Code · Environment Setup
- **Background**: #000000

### Slide 2 — 설치하기 (Windows)
- **Type**: Content (steps + screenshots)
- **Key Message**: 앱 다운로드 → 설치·실행 → 로그인 → 개인정보보호 설정
- **Details**:
  - claude.ai/download → Windows 설치 파일
  - 설치 마법사 → 데스크톱 아이콘 실행
  - Anthropic 계정 브라우저 인증
  - 로그인 직후 "Claude 개선에 도움주기" 끄기 (기본값이 켜져 있으므로 직접 끄기)
- **Background**: #ffffff

### Slide 3 — 워크스페이스 어디에 만들까
- **Type**: Content (options + flow)
- **Key Message**: 먼저 작업 폴더를 만들고, 앱에서 연결한다
- **Details**:
  - ✅ 추천: Documents\Claude Projects\
  - ✅ 가능: 바탕화면 Claude 폴더
  - ❌ 비추천: C:\ 루트 (시스템 폴더와 섞임)
  - 연결 흐름: 폴더 생성 → "폴더 열기..." → 대화 시작
- **Background**: #f5f5f7

### Slide 4 — 채팅 탭 vs 코드 탭
- **Type**: Content (2-column compare, dark)
- **Key Message**: 코드 탭은 따로 설치할 게 없다 — 파일·터미널이 내장
- **Details**:
  - 채팅 탭: 대화·문서 작업 중심 / 로컬 파일·터미널을 직접 다루려면 별도 연결 도구를 설치해야 함 (그 도구 이야기는 3주차에서)
  - 코드 탭(우리가 쓰는 탭): 파일 읽기·쓰기·터미널 명령 실행이 처음부터 내장 → 추가 설치 없이 바로 내 PC에서 작업 (Node · Python · git 설치도 한 줄)
  - 하단: 이 캠프는 코드 탭만 사용 → 따로 설치할 도구가 없음
- **Background**: #272729

### Slide 5 — 준비물: Node.js
- **Type**: Content (3 reasons + command)
- **Key Message**: 다음 주 MCP 도구(koica-reg 등)가 Node.js로 동작 — 미리 준비
- **Details**:
  - ① koica-reg도 Node 기반 — 다음 주 실습 커넥터가 Node.js로 동작
  - ② 코드 탭이 직접 설치 — 내장 터미널로 한 줄이면 끝
  - ③ Week 3 준비물 — 다음 주에 더 많은 MCP 도구를 설치
  - 명령: "Node.js LTS 버전 설치해줘" → 코드 탭이 다운로드·설치·버전 확인까지 진행
- **Background**: #272729

### Slide 6 — Global Settings vs Project Settings
- **Type**: Content (Split)
- **Key Message**: 전역 = 나 / 프로젝트 = 여기서만
- **Details**:
  - Global: 모든 프로젝트 적용 · ~/.claude/CLAUDE.md
  - Project: 이 프로젝트만 · .claude/CLAUDE.md · 팀 공유 가능
  - 하단: 코드 탭에서 바로 열기 — "~/.claude/CLAUDE.md 파일 열어줘"
- **Background**: #ffffff

### Slide 7 — 첫 실습 (코드 탭으로 파일 다루기)
- **Type**: Practice (dark)
- **Key Message**: 코드 탭에서는 바로 된다 — 설치 없이 파일을 직접 다룬다
- **Details**:
  - "이 폴더에 있는 파일 목록 알려줘"
  - "바탕화면에 test.txt 파일 만들어줘"
  - 탐색기를 열지 않아도 클로드가 직접 파일을 다룸
- **Background**: #1d1d1f

### Slide 8 — 다음 주 예고 & 클로징
- **Type**: Closing
- **Message**: 나만의 Claude 스킬을 만들어 보자
- **Details**: 반복 작업을 명령어 하나로 자동화
- **Background**: #000000
