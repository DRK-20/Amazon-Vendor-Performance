document.addEventListener('DOMContentLoaded', function() {
    console.log('Custom JS Loaded Successfully');

    const getStartedBtn = document.querySelector('.btn-lg');
    if (getStartedBtn) {
        getStartedBtn.addEventListener('click', function(event) {
            event.preventDefault();
            const targetSection = document.querySelector('#features');
            if (targetSection) {
                targetSection.scrollIntoView({ behavior: 'smooth' });
            }
        });
    }
});
