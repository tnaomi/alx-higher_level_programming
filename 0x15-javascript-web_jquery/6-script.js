// Use JQuery to replace content w onclick
$(function () {
  $('#update_header').on('click', function () {
    $('header').contents().replaceWith('New Header!!!');
  });
});
