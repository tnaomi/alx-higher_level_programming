// Use JQuery to GET content w onclick
const API_URL = 'https://swapi-api.alx-tools.com/api/people/5/?format=json'

$(function () {
  $.getJSON(API_URL, function (data) {
    $.each(data, function (key, value) {
      if (key === 'name') {
        $('#character').append(value)
      }
    });
  });
});
