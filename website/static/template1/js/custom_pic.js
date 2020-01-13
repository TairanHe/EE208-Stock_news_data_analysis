(function ($) {

  "use strict";

    // MENU
    $('.menu-burger').on('click', function() {
      $('.menu-bg, .menu-items, .menu-burger').toggleClass('fs');
      $('.menu-burger').text() == "☰" ? $('.menu-burger').text('✕') : $('.menu-burger').text('☰');
    });

    $('body').vegas({
        slides: [
            { src: 'static/template1/images/11.jfif' },
            { src: 'static/template1/images/12.jfif' }
        ],
        timer: false,
        transition: [ 'burn', ]
    });

})(jQuery);
