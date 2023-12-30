function scrollToTop() {
    $('html, body').animate({ scrollTop: 0 }, 'slow');
}

// Show/hide the button based on scroll position
$(document).ready(function () {
    $(window).scroll(function () {
        if ($(this).scrollTop() > 100) {
            $('#scrollToTopBtn').fadeIn();
        } else {
            $('#scrollToTopBtn').fadeOut();
        }
    });
});