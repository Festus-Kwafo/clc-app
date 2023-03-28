
(function() {
    "use strict";
  
    /**
     * Easy selector helper function
     */
    const select = (el, all = false) => {
      el = el.trim()
      if (all) {
        return [...document.querySelectorAll(el)]
      } else {
        return document.querySelector(el)
      }
    }
  
    /**
     * Easy event listener function
     */
    const on = (type, el, listener, all = false) => {
      let selectEl = select(el, all)
      if (selectEl) {
        if (all) {
          selectEl.forEach(e => e.addEventListener(type, listener))
        } else {
          selectEl.addEventListener(type, listener)
        }
      }
    }
  
    /**
     * Easy on scroll event listener 
     */
    const onscroll = (el, listener) => {
      el.addEventListener('scroll', listener)
    }
  
    /**
     * Toggle .navbar-reduce
     */
    let selectHNavbar = select('.navbar-default')
    if (selectHNavbar) {
      onscroll(document, () => {
        if (window.scrollY > 100) {
          selectHNavbar.classList.add('navbar-reduce')
          selectHNavbar.classList.remove('navbar-trans')
        } else {
          selectHNavbar.classList.remove('navbar-reduce')
          selectHNavbar.classList.add('navbar-trans')
        }
      })
    }
  
    /**
     * Back to top button
     */
    let backtotop = select('.back-to-top')
    if (backtotop) {
      const toggleBacktotop = () => {
        if (window.scrollY > 100) {
          backtotop.classList.add('active')
        } else {
          backtotop.classList.remove('active')
        }
      }
      window.addEventListener('load', toggleBacktotop)
      onscroll(document, toggleBacktotop)
    }
  
    /**
     * Preloader
     */
    let preloader = select('#preloader');
    if (preloader) {
      window.addEventListener('load', () => {
        preloader.remove()
      });
    }
  
    /**
     * Search window open/close
     */
    let body = select('body');
    var logo = select('.logo');
    var search_toggle = select('#search-bar');
    var navbar_toggler = select('.navbar-toggler');
    on('click', '.navbar-toggle-box', function(e) {
      e.preventDefault()
        console.log("Toggle click")
        logo.classList.add('logo-hide');
        search_toggle.classList.add('search-bar-show');
        search_toggle.classList.remove('search-bar');
        navbar_toggler.classList.add('logo-hide');
      body.classList.add('box-collapse-open')
      body.classList.remove('box-collapse-closed')
    });

    /**Owl Carousel */
    $(".owl-carousel1").owlCarousel({
      loop: true,
      center: true,
      margin: 0,
      responsiveClass: true,
      nav: true,
      autoplay: true,
      autoplayHoverPause: true,

      responsive: {
        0: {
          items: 1,
          nav: false
        },
        680: {
          items: 2,
          nav: false,
          loop: false
        },
        1000: {
          items: 3,
          nav: true
        },
      }
    });


})()
