#!/usr/bin/node

// List all characters in a movie by Id

const movieId = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/:id'.replace(':id', movieId);
const request = require('request');

request(url, function (err, _response, body) {
  if (err) {
    console.error(err);
  } else {
    const filmCharacters = JSON.parse(body).characters;
    for (const character in filmCharacters) {
      console.log(character);
    }
  }
});
