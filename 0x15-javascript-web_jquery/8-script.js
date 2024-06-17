// Use JQuery to GET content w onclick
const API_URL = 'https://swapi-api.alx-tools.com/api/films/?format=json';

$(function () {
  $.getJSON(API_URL, function (data) {
    $.each(data.results, function (i) {
      for (i of data.results) {
        $('UL#list_movies').append(`<li>${i.title}</li>`);
      }
    });
  });
});
