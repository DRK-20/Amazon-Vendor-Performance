document.addEventListener('DOMContentLoaded', function() {
    console.log('scripts.js loaded successfully');

    const loadingOverlay = document.getElementById('loading-overlay');
    if (loadingOverlay) {
        loadingOverlay.classList.remove('active');
    }

    const forms = document.querySelectorAll('form');
    forms.forEach(form => {
        form.addEventListener('submit', () => {
            if (loadingOverlay) {
                loadingOverlay.classList.add('active');
            }
        });
    });
});

document.addEventListener('DOMContentLoaded', function() {
    AOS.init({
        duration: 1000,
        once: true,
    });
});
