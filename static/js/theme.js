// 다크 / 라이트 모드 전환
// Bootstrap 5.3은 <html data-bs-theme="dark|light"> 값으로 테마를 정합니다.
// 고른 테마는 브라우저(localStorage)에 저장해서 새로고침해도 유지됩니다.

(function () {
  var KEY = "board-theme";

  function getSaved() {
    try {
      return localStorage.getItem(KEY);
    } catch (e) {
      return null;
    }
  }

  function save(theme) {
    try {
      localStorage.setItem(KEY, theme);
    } catch (e) {}
  }

  // 1) 페이지가 그려지기 전에 저장된 테마를 먼저 적용 (깜빡임 방지)
  var saved = getSaved();
  if (saved === "light" || saved === "dark") {
    document.documentElement.setAttribute("data-bs-theme", saved);
  }

  // 버튼 글자: 지금 테마의 "반대쪽"을 보여줌
  function updateButton(btn) {
    var now = document.documentElement.getAttribute("data-bs-theme");
    btn.textContent = now === "dark" ? "☀️ 라이트 모드" : "🌙 다크 모드";
  }

  // 2) 화면이 다 준비되면 버튼에 클릭 동작 연결
  document.addEventListener("DOMContentLoaded", function () {
    var btn = document.getElementById("board-theme-toggle");
    if (!btn) return;

    updateButton(btn);

    btn.addEventListener("click", function () {
      var now = document.documentElement.getAttribute("data-bs-theme");
      var next = now === "dark" ? "light" : "dark";
      document.documentElement.setAttribute("data-bs-theme", next);
      save(next);
      updateButton(btn);
    });
  });
})();
