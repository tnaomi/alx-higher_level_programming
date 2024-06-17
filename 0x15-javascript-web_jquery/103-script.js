// Use JQuery to GET content w onclick
const API_URL = 'https://hellosalut.stefanbohacek.dev/';


$(function () {
  $('#btn_translate').on('click', function () {
    const lang = $('#language_code').val();
    $.getJSON(`${API_URL}?lang=${lang}`, function (data) {
      $('DIV#hello').text(data.hello);
    });
  });
  $('#language_code').on('keypress', function (event) {
    if (event.which === 13) {
      const lang = $('#language_code').val();
      $.getJSON(`${API_URL}?lang=${lang}`, function (data) {
        $('DIV#hello').text(data.hello);
      });
    }
  });
});
