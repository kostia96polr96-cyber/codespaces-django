document.addEventListener('DOMContentLoaded', () => {
    const toggle = document.getElementById('theme-switch');

    toggle.addEventListener('change', () => {
    document.body.classList.toggle('dark', toggle.checked);
    })
});