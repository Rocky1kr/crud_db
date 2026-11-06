# 디자인 규칙 (모든 화면 공통)

참고 이미지: `design/ref1.png` (처음 디자인의 출발점. 지금은 아래 규칙이 우선)

## 전체 분위기
- 화면마다 **큰 제목 하나가 주인공**이다. 나머지는 조용하고 단정하게.
- 제목 아래 **굵은 선(3px)** 에서 내용이 시작된다.
- 내용은 상자(카드)에 넣지 않는다. 가는 줄로만 나눈다.
- 다크 모드가 기본, 버튼으로 라이트 모드 전환.

## 색상
`board.css` 맨 위의 `--board-` 변수로 관리한다. 아래 표의 값만 사용한다.

| 용도 | 변수 | 다크 | 라이트 |
| --- | --- | --- | --- |
| 페이지 배경 | `--board-bg` | `#1a1d1e` | `#f5f6f7` |
| 기본 글자, 굵은 선 | `--board-text` | `#e8eaea` | `#1a1d1e` |
| 보조 글자 (개수, 라벨, 번호) | `--board-sub` | `#a0a6a8` | `#5f6668` |
| 입력칸 테두리 | `--board-line` | `#3a3f41` | `#d5d9db` |
| 줄 사이 가는 선 | `--board-row-line` | `#2c3032` | `#e4e7e8` |
| 줄 hover 배경 | `--board-hover` | `#23272a` | `#eef0f1` |
| 보조 버튼 배경 | `--board-badge-bg` | `#2a2f31` | `#e8ebec` |
| 기본 버튼 배경 | `--board-btn-bg` | `#e8ecf4` | `#1a1d1e` |
| 기본 버튼 글자 | `--board-btn-text` | `#1a1d1e` | `#ffffff` |
| 기본 버튼 hover | `--board-btn-hover` | `#ffffff` | `#3a3f41` |
| 입력칸 배경 | `--board-input-bg` | `#23272a` | `#ffffff` |
| 강조 (삭제) | `--board-accent` | `#ff4d4f` | `#ff4d4f` |

## 글꼴
- **큰 제목**: `Black Han Sans` (Google Fonts, 굵은 포스터풍 한글 글꼴). 클래스 `board-display`
  - 모든 화면 `<head>`에서 Bootstrap 다음, `board.css` 앞에 불러온다.
    ```html
    <link rel="preconnect" href="https://fonts.googleapis.com" />
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin />
    <link href="https://fonts.googleapis.com/css2?family=Black+Han+Sans&display=swap" rel="stylesheet" />
    ```
- **나머지 모든 글자**: `"Malgun Gothic"`, `"Apple SD Gothic Neo"`, `sans-serif`
- 큰 제목은 한 화면에 하나만 쓴다.

| 쓰임 | 클래스 | 크기 (휴대폰) |
| --- | --- | --- |
| 목록 "게시판" | `board-display-xl` | 72px (52px) |
| 글쓰기 / 글 수정 | `board-display-lg` | 48px (36px) |
| 상세 화면의 글 제목 | `board-display-md` | 40px (30px) |
| 댓글 제목 (`board-h2`) | — | 18px, 굵게 |
| 게시글 제목 링크 | — | 17px |
| 본문 | — | 17px, 줄간격 1.8 |
| 라벨, 보조 글자, 버튼 | — | 14px |

## 레이아웃
- 내용 최대 너비 900px, 가운데 정렬 (`board-wrap mx-auto`)
- 페이지 바깥 여백: 위 24px, 좌우 16px, 아래 64px
- **화면 머리** (`<header class="board-head">`): 왼쪽 큰 제목, 오른쪽 버튼, 아래 3px 굵은 선
  - 목록: 제목 아래에 `글 N개` (`board-head-sub`)
  - 상세: 머리 위에 `board-topbar` 줄 → 왼쪽 "← 게시판으로 돌아가기", 오른쪽 테마 버튼

## 화면별 구성
- **목록**: 머리 → 표. 번호(큰 회색 숫자, 오른쪽 정렬) + 제목. 줄 전체가 링크(`stretched-link`).
  표 머리글(번호/제목)은 화면에서 숨기고 읽기 프로그램용으로만 둔다(`visually-hidden`).
- **상세**: 머리(글 제목) → 본문 → 가는 선 → 오른쪽에 수정·삭제 버튼 → 댓글
  - 댓글: "댓글 N개" 제목 + 2px 선, 댓글은 가는 줄로 구분
- **글쓰기 / 수정**: 머리 → 라벨+입력칸 → 오른쪽 아래 취소·등록 버튼

## 컴포넌트
- **기본 버튼** (`board-btn`): 화면에서 가장 중요한 동작 하나 (글쓰기, 등록, 수정 완료, 댓글 등록)
- **보조 버튼** (`board-btn-sub`): 그 밖의 동작 (취소, 수정하기, 테마 전환)
- **삭제 버튼** (`board-btn-danger`): 보조 버튼 모양 + 강조색 글자
- 버튼 모두: 둥근 모서리 8px, 14px 굵게, 안쪽 여백 10px 18px
- **입력칸** (`board-input`): 둥근 모서리 8px, 클릭하면 테두리가 기본 글자색으로 진해짐
- **빈 상태** (`board-empty`): 가운데 정렬 보조색 문구 + 할 일을 알려줌
  - 목록: "아직 글이 없어요." + "첫 글 쓰기" 버튼
  - 댓글: "아직 댓글이 없어요. 첫 댓글을 남겨 보세요."
- **줄 hover**: 배경이 `--board-hover`로 살짝 바뀌고 제목에 밑줄

## 테마 전환
- 모든 화면 오른쪽 위에 전환 버튼(`board-btn-sub`, `id="board-theme-toggle"`)
- 모든 화면은 `board.css` 다음 줄에서 `static/js/theme.js`를 불러온다.
- 버튼에는 바꿀 테마를 보여준다. (다크일 때 "☀️ 라이트 모드", 라이트일 때 "🌙 다크 모드")
- 고른 테마는 브라우저에 저장한다.

## 접근성 (누구나 쓰기 편하게)
- 키보드 Tab으로 이동하면 지금 위치에 테두리가 보이게 한다.
- 입력칸에는 항상 `<label>`을 붙인다. (눈에 안 보여도 되면 `visually-hidden`)

## Bootstrap 사용 규칙
- Bootstrap 5.3.3을 CDN으로 불러온다.
  `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" />`
- `<html>` 태그에 `data-bs-theme="dark"`를 넣는다.
- 배치와 여백은 Bootstrap 클래스를 먼저 쓴다. (예: `d-flex`, `gap-2`, `mb-4`, `mx-auto`)
- 버튼, 표, 입력칸은 Bootstrap 부품(`btn`, `table`, `form-control`)을 쓰고, 색과 크기만 우리 CSS로 덮어쓴다.
- 우리가 만드는 클래스 이름은 모두 `board-`로 시작한다.

## 지키는 원칙
- 템플릿 문법(`{{ post.title }}`, `{% for %}` 등)은 그대로 유지해서 기존 기능이 깨지지 않게 한다.
- HTML 안에 CSS를 직접 쓰지 않는다. (`<style>` 태그, `style=""` 속성 금지)
- 스타일은 `static/css/board.css`에 작성하고 Bootstrap 다음 줄에 불러온다.
- DB에 없는 정보(이름, 날짜, 조회수 등)는 화면에 만들지 않는다. (글/댓글 개수처럼 DB에서 셀 수 있는 것은 OK)
- 색상은 위 표의 값만 사용한다.
