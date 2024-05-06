// Use JQuery to add list items w onclick
$(function () {
  $('#add_item').on('click', function () {
    $('UL.my_list').append('\n<li>Item</li>');
  });
});
