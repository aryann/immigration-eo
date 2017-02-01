/**
 * Handles toggling the navigation menu for small screens.
 */
function initialize() {
	var button = document.getElementById( 'topnav' ).getElementsByTagName( 'div' )[0],
	    menu   = document.getElementById( 'topnav' ).getElementsByTagName( 'ul' )[0];

	if ( undefined === button )
		return false;

	// Hide button if menu is missing or empty.
	if ( undefined === menu || ! menu.childNodes.length ) {
		button.style.display = 'none';
		return false;
	}

	button.onclick = function() {
		if ( -1 == menu.className.indexOf( 'srt-menu' ) )
			menu.className = 'srt-menu';

		if ( -1 != button.className.indexOf( 'toggled-on' ) ) {
			button.className = button.className.replace( ' toggled-on', '' );
			menu.className = menu.className.replace( ' toggled-on', '' );
		} else {
			button.className += ' toggled-on';
			menu.className += ' toggled-on';
		}
	};
};

// Fireup the plugins
$(document).ready(function(){

  var $window = $(window);
  var $flexSlider = $('.flexslider');
  var $form = $('.form-iframe');
  var $signBtn = $('.buttonlink')
  var $backBtn = $('.back')
	// initialise  slideshow
	$('.flexslider').flexslider({
  	animation: "fade",
    slideshow: true,
    slideshowSpeed: 3000,
  	directionNav: false,
    controlNav: false
  });


  function initForm() {
    var windowHeight = $window.height();
    var windowWidth = $window.width();
    $form.attr('width', windowWidth);
    $form.attr('height', windowHeight);
    $signBtn.on('click', function(e) {
      e.preventDefault();
      // $backBtn.addClass('visible');
      if(windowWidth < 768) {
        window.open('https://docs.google.com/forms/d/e/1FAIpQLScOH4yMtuYrYIC-AUf1JTHc7bMZgqHRJ6rQ-_HShQGKIi31BQ/viewform');
      } else {
        $form.addClass('visible');
      }

    });
    $backBtn.on('click', function(e) {
      // $backBtn.removeClass('visible');
      $form.removeClass('visible');
    });
  }
	// call initialize when dom is loaded

	// commenting this out for now - `#topnav` does not exits
	// TODO fix this
	// initialize();
  initForm();

});


