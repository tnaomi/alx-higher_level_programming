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
      request(filmCharacters[currentIndex], function (err, _response, body) {
        if (err) {
          console.error(err);
        }
        console.log(JSON.parse(body).name);
      });
      currentIndex++;
    }
  }
});
