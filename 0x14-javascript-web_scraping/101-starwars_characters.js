#!/usr/bin/node

// List all characters in the movie using the original format

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/:id'.replace(':id', movieId);
const request = require('request');

request(url, function (err, _response, body) {
  if (err) {
    console.error(err);
  } else {
    const filmCharacters = JSON.parse(body).characters;
    getChars(filmCharacters, 0);
  }
});

function getChars (filmCharacters, currentIndex) {
  request(filmCharacters[currentIndex], function (newErr, _newResponse, newBody) {
    if (!newErr) {
      console.log(JSON.parse(newBody).name);
      if (currentIndex + 1 < filmCharacters.length) {
        getChars(filmCharacters, currentIndex + 1);
      }
    }
  });
}
