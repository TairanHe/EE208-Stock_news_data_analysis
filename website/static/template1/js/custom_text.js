(function ($) {

  "use strict";

    // MENU
    $('.menu-burger').on('click', function() {
      $('.menu-bg, .menu-items, .menu-burger').toggleClass('fs');
      $('.menu-burger').text() == "☰" ? $('.menu-burger').text('✕') : $('.menu-burger').text('☰');
    });

    $('body').vegas({
        slides: [
            { src: 'static/template1/images/32.jfif' },
            { src: 'static/template1/images/31.jfif' }
        ],
        timer: false,
        transition: [ 'fade', ]
    });

})(jQuery);
