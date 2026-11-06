# 디자인 규칙 (list.html 기준)

참고 이미지: `design/ref1.png` (어두운 테마의 게시판 목록)

## 전체 분위기
- 어두운 테마(다크 모드)
- 둥근 모서리, 가는 구분선, 깔끔한 표 형태

## 색상
| 용도 | 색상 |
| --- | --- |
| 페이지 배경 | `#1a1d1e` |
| 기본 글자 | `#e8eaea` |
| 보조 글자 (표 머리글, 뱃지) | `#a0a6a8` |
| 표 바깥 테두리 / 머리글 아래 선 | `#3a3f41` |
| 줄 사이 구분선 | `#2c3032` |
| 줄 hover(마우스 올림) 배경 | `#23272a` |
| 뱃지 배경 | `#2a2f31` |
| 버튼 배경 / 글자 | `#e8ecf4` / `#1a1d1e` |
| 강조(NEW 표시용) | `#ff4d4f` |

### 라이트 모드 색상
`<html data-bs-theme="light">`일 때 쓰는 색. `board.css` 맨 위의 `--board-` 변수로 관리한다.

| 용도 | 색상 |
| --- | --- |
| 페이지 배경 | `#f5f6f7` |
| 기본 글자 | `#1a1d1e` |
| 보조 글자 | `#5f6668` |
| 표 바깥 테두리 / 머리글 아래 선 | `#d5d9db` |
| 줄 사이 구분선 | `#e4e7e8` |
| 줄 hover 배경 | `#eef0f1` |
| 뱃지 배경 | `#e8ebec` |
| 버튼 배경 / 글자 | `#1a1d1e` / `#ffffff` (hover `#3a3f41`) |
| 입력칸 배경 | `#ffffff` |
| 강조 | `#ff4d4f` |

### 테마 전환
- 모든 화면 상단 오른쪽에 전환 버튼(`board-btn-sub`, `id="board-theme-toggle"`)을 둔다.
  - 목록: "글쓰기" 버튼 왼쪽 / 글쓰기·수정: 제목 줄 오른쪽 / 상세: 글 상자 위 오른쪽
- 모든 화면은 `board.css` 다음 줄에서 `static/js/theme.js`를 불러온다.
- 버튼에는 바꿀 테마를 보여준다. (다크일 때 "☀️ 라이트 모드", 라이트일 때 "🌙 다크 모드")
- 전환 코드는 `static/js/theme.js`에 두고, 고른 테마는 브라우저에 저장한다.

## 글꼴
- `"Malgun Gothic"`, `"Apple SD Gothic Neo"`, `sans-serif`
- 페이지 제목(h1): 30px
- 게시글 제목: 16px
- 표 머리글: 14px
- 뱃지: 13px

## 레이아웃
- 내용 최대 너비 900px, 가운데 정렬
- 페이지 바깥 여백: 위아래 24px, 좌우 16px
- 상단: 왼쪽 제목, 오른쪽 "글쓰기" 버튼 (양 끝 정렬)
- 본문: 둥근 테두리(반지름 10px)의 표

## 표 규칙
- 열: 번호(너비 90px, 가운데 정렬), 제목
- 머리글은 `th`, 글자색 보조색, 굵지 않게
- 칸 안쪽 여백: 머리글 12px 16px / 본문 14px 16px
- 마지막 줄은 아래 구분선 없음
- 줄에 마우스를 올리면 배경이 살짝 밝아짐

## 컴포넌트
- **번호 뱃지**: 알약 모양(`border-radius: 999px`), 최소 너비 52px, 가운데 정렬
- **제목 링크**: 밑줄 없음, hover 때만 밑줄. 제목 자체가 상세 페이지 링크
- **글쓰기 버튼**: 밝은 배경 + 어두운 글자, 둥근 모서리 8px, hover 때 더 밝게
- **빈 목록**: "아직 글이 없어요." 문구를 가운데에 표시

## Bootstrap 사용 규칙
- Bootstrap 5.3.3을 CDN으로 불러온다.
  `<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" />`
- `<html>` 태그에 `data-bs-theme="dark"`를 넣어 Bootstrap 다크 모드를 켠다.
- 배치와 여백은 Bootstrap 클래스를 먼저 쓴다. (예: `d-flex`, `justify-content-between`, `mb-3`, `mx-auto`, `text-center`)
- 버튼, 표, 뱃지는 Bootstrap 부품(`btn`, `table`, `badge rounded-pill`)을 쓰고, 색과 크기만 우리 CSS로 덮어쓴다.
- 우리가 만드는 클래스 이름은 모두 `board-`로 시작한다. (Bootstrap의 `.container`, `.btn`, `.badge`와 겹치지 않게)

## 지키는 원칙
- 템플릿 문법(`{{ post.title }}`, `{% for %}` 등)은 그대로 유지해서 기존 기능이 깨지지 않게 한다.
- HTML 안에 CSS를 직접 쓰지 않는다. (`<style>` 태그, `style=""` 속성 금지)
- 스타일은 `static/css/board.css` 파일에 작성하고 `<link href="/static/css/board.css" rel="stylesheet" />`로 불러온다. Bootstrap 다음 줄에 불러와야 덮어쓰기가 된다.
- DB에 없는 정보(이름, 날짜, 조회수 등)는 화면에 만들지 않는다.
- 색상은 위 표의 값만 사용해서 통일감을 유지한다.
