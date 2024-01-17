document.addEventListener("DOMContentLoaded", function() {
    console.log("DOMContentLoaded сработал.");

    // Получаем кнопку для переключения темы по ее ID "theme-toggle"
    const themeToggle = document.getElementById("theme-toggle");

    // Получаем элемент стилевого листа по его ID "theme-stylesheet"
    const styleSheet = document.getElementById("theme-stylesheet");

    // Проверяем, найдена ли кнопка и стилевой лист
    if (themeToggle && styleSheet) {
        themeToggle.addEventListener("click", function() {
            if (document.body.classList.contains("dark-theme")) {
                document.body.classList.remove("dark-theme");
                document.body.classList.add("light-theme");
                styleSheet.setAttribute("href", "/static/css/light-theme.css");
                console.log("Тема изменена на светлую");
            } else {
                document.body.classList.remove("light-theme");
                document.body.classList.add("dark-theme");
                styleSheet.setAttribute("href", "/static/css/dark-theme.css");
                console.log("Тема изменена на тёмную");
            }
        });
    } else {
        console.error("Элемент с ID 'theme-toggle' или 'theme-stylesheet' не найден.");
    }
});







