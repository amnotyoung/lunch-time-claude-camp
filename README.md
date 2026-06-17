# 점심시간 클로드 코드 캠프

점심시간에 운영하는 **클로드 코드(Claude 데스크톱 앱의 '코드' 탭)** 학습 캠프 자료입니다.
비개발자 동료가 자연어로 클로드 코드를 다루며 매주 손에 잡히는 결과물을 만들어 갑니다.

## 커리큘럼

| 주차 | 일정 | 주제 | 자료 |
|---|---|---|---|
| 1 | 4월 27일주 | 클로드 채팅과 클로드 코드는 뭐가 다른가 | [week1](weeks/week1-클로드채팅vs코드/) |
| 2 | 5월 4일주 | 클로드 코드 사용 환경을 구성해보자 | [week2](weeks/week2-환경구성/) |
| 3 | 5월 11일주 | 더 많은 도구를 연결해보자 (MCP) | [week3](weeks/week3-외부도구연결/) |
| 4 | 5월 25일주 | 나만의 스킬을 만들어보자 (ktm) | [week4](weeks/week4-스킬만들기/) |
| 5 | 6월 8일주 | 깃(Git)이란 무엇인가 | [week5](weeks/week5-깃/) |
| 6 | 6월 15일주 | 에이전트와 서브 에이전트 | [week6](weeks/week6-에이전트팀/) |
| 7 | 6월 22일주 | 깃허브(GitHub)란 무엇인가 | _(예정)_ |
| 8 | 6월 29일주 | 클로드와 챗지피티를 협업시켜보자 | _(예정)_ |

## 폴더 구조

- `weeks/` — 주차별 슬라이드(`slide-*.html`)와 설계 아웃라인(`slide-outline.md`)
- `.claude/skills/ktm/` — 캠프에서 만든 자체 스킬: KOICA 규정 텍스트마이닝 (조회 → 키워드 → 그래프 → 보고서)
- `outputs/` — ktm 스킬 예시 산출물
- `references/` — 커리큘럼 등 참고 자료

> 슬라이드는 HTML 소스로 관리합니다. 발표용 PDF·배포용 zip은 저장소에 포함하지 않습니다.

## 환경 메모

이 캠프는 **Claude 데스크톱 앱의 '코드' 탭**만 사용합니다. 코드 탭은 파일 읽기·쓰기와
터미널 명령 실행이 내장되어 있어, 로컬 작업에 Desktop Commander 같은 별도 도구가 필요 없습니다.
(Desktop Commander는 '채팅' 탭이 로컬에 접근할 때 쓰는 MCP이며, 3주차에서 한 번 소개합니다.)

## 캠프에서 사용한 외부 도구

저장소 용량과 라이선스를 위해 외부 오픈소스 도구는 포함하지 않습니다. 필요하면 원본에서 설치하세요.

- **kordoc** — 한글 문서(HWPX) 처리 도구 · https://github.com/chrisryugj/kordoc
- **slides-grab** — HTML 슬라이드 자동 제작·변환 (이 캠프 슬라이드 제작에 사용) · https://github.com/vkehfdl1/slides-grab
- **koica-reg-mcp** — KOICA 규정 조회 MCP (3주차 실습) · https://github.com/amnotyoung/koica-reg-mcp
