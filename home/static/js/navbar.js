// navbar.js
document.addEventListener('DOMContentLoaded', function() {
    const toggleButton = document.getElementById('navbar-toggle');
    const menu = document.getElementById('navbar-menu');

    toggleButton.addEventListener('click', function() {
        menu.classList.toggle('active');
    });
});
