// Use JQuery to add list items w onclick
$(function () {
  $('#add_item').on('click', function () {
    $('UL.my_list').append('<li>Item</li>');
  }).done(
    $('#remove_item').on('click', function () {
      $('UL.my_list>li:last-child').remove();
    }),
    $('#clear_list').on('click', function () {
      $('UL.my_list>li').remove();
    })
);
});

