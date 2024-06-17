// Use JQuery to change class w onclick
$(function () {
  $('#toggle_header').on('click', function () {
    if ($('header').hasClass('green')) {
      $('header').removeClass('green');
      $('header').addClass('red');
    } else {
      $('header').removeClass('red');
      $('header').addClass('green');
    }
  });
});
