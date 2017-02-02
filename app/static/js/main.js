$(document).ready(function(){

  var $window = $(window);
  var $flexSlider = $('.flexslider');
  var windowWidth = $window.width();
  var windowHeight = $window.height();
	var $venobox = $('.venobox');
  var mobileBreakPoint = 768;
  var $up = $('.up-arrow-scroll');
  var fallBackCount = 'More than 1000 ';
  var $counterEl = $('.counter');
  var $counterContainerEl = $('.counter-container');

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

  function loadCount() {
    var endPoint = '//docs.google.com/spreadsheets/d/17jz1v4DusIRhtQYhkvelHq1oJlsFSBat5aSb0cHNQ2k/pubhtml?gid=1523619827&widget=false&headers=false&chrome=false&single=true';
    $.ajax({
      url: endPoint,
      dataType: 'html'
    }).done(function(data, textStatus, jqXHR) {
      var $data = $(data);
      var $countCell = $($data[8].getElementsByClassName('s0'));
      var count = $countCell.text();
      $counterEl.text(count + ' ');

    }).fail(function(error) {
      $counterContainerEl.addClass('failed');
      $counterEl.text(fallBackCount);
    }).always(function() {
      $loaderEl.fadeOut();
      $counterContainerEl.removeClass('loading');
    });
  }

  loadCount();

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


