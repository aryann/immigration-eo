$(document).ready(function(){

  var $window = $(window);
  var $flexSlider = $('.flexslider');
  var windowWidth = $window.width();
  var windowHeight = $window.height();
	var $venobox = $('.venobox');
  var mobileBreakPoint = 768;
  var $up = $('.up-arrow-scroll');
  var fallBackCount = 'More than 1000 ';

  var $loaderEl = $('ball-pulse');

  function isMobile() {
    return windowWidth < mobileBreakPoint;
  }

  // initialise  slideshow
	$('.flexslider').flexslider({
  	animation: "fade",
    slideshow: true,
    slideshowSpeed: 3000,
  	directionNav: false,
    controlNav: false
  });

  // initialize the modal plugin for Form + waypoint, up arrow link
  // opens form in new window if on mobile
  // opens form in modal if on desktop
  if(isMobile()) {
    $venobox.attr('target', '_blank');
  } else {
    $venobox.venobox();
    if($('body').attr('id') === 'home-page') {
      var waypoint = new Waypoint({
        element: document.querySelector('.signatures-wrapper'),
        handler: function(direction) {
          if(direction === 'down') {
            $up.fadeIn();
          } else {
            $up.fadeOut();
          }
        }
      });
    }

  }

  $up.on('click', function(e) {
    e.preventDefault();
    $("html, body").animate({ scrollTop: "0px" });
  });

  // share code
  var shareUrl = 'http://siliconvalleystands.org/';
  var shareOptions = {
    twitter: {
      text: 'We stand together for diversity, for inclusion, for immigrants #SVStands',
      via: 'SVStands'
    },
    facebook : true
  };

  $('.socialShare').shareButtons(shareUrl, shareOptions);


});


