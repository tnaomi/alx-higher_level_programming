// Use JQuery to GET input content w onclick
const API_URL = 'https://hellosalut.stefanbohacek.dev/';

$(function () {
  $('#btn_translate').on('click', function () {
    const lang = $('#language_code').val();
    $.getJSON(`${API_URL}?lang=${lang}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
});
