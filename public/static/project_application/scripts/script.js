$(document).ready(function() {
  $(".owl-carousel").owlCarousel();
  console.log("Owl loaded!");
});

$(document).ready(function() {
  $('#dtBasicExample').DataTable({
    "paging": false, // false to disable pagination (or any other option)
    "info": false,
    oLanguage: {
      "sSearch": "Szukaj:",
      "sRowEmpty": "Ups! Nie mamy t",
    },
    "order": [],
  });
  array = ['Cafe Kryzysowa', 'Warszawa', 'Kawiarnia', 'Zniżka'];
  $('.dataTables_length').addClass('bs-select');
  console.log("DataTable initilaized!")
  $('.dataTables_filter input').attr("placeholder", array[Math.floor(Math.random() * array.length)].toString());

});


(function($) {
  "use strict";
  console.log("JS loaded!");
  $(function() {
    var header = $(".start-style");
    $(window).scroll(function() {
      var scroll = $(window).scrollTop();

      if (scroll >= 10) {
        header.removeClass('start-style').addClass("scroll-on");
      } else {
        header.removeClass("scroll-on").addClass('start-style');
      }
    });
  });

  //Menu On Hover
  $('body').on('mouseenter mouseleave', '.nav-item', function(e) {
    if ($(window).width() > 750) {
      var _d = $(e.target).closest('.nav-item');
      _d.addClass('show');
      setTimeout(function() {
        _d[_d.is(':hover') ? 'addClass' : 'removeClass']('show');
      }, 1);
    }
  });

})(jQuery);