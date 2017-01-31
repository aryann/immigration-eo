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

	// initialise  slideshow
	$('.flexslider').flexslider({
  	animation: "fade",
  	directionNav: false,
    start: function(slider){
      // alert()
      // $('body').removeClass('loading');
    }
  });

	// call initialize when dom is loaded

	// commenting this out for now - `#topnav` does not exits
	// TODO fix this
	// initialize();


});


