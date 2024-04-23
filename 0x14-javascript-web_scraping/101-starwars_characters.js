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
    let currentIndex = 0;
    while (currentIndex < filmCharacters.length) {
      request(filmCharacters[currentIndex], function (newErr, _newResponse, newBody) {
        if (newErr) {
          console.error(newErr);
        }
        console.log(JSON.parse(newBody).name);
      });
      currentIndex++;
    }
  }
});
