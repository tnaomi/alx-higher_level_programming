// Use JQuery to GET content w onclick
const API_URL = 'https://hellosalut.stefanbohacek.dev/?lang=fr';

$(function () {
  $.getJSON(API_URL, function (data) {
    $('DIV#hello').text(data.hello).append();
  });
});
