#!/usr/bin/node

// Query a URL and log the status code

const url = process.argv[2];
const request = require('request');

request(url, function (err, _response, body) {
  if (err) {
    console.error(err);
  } else {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const Index in films) {
      const filmChars = films[Index].characters;
      for (const charIndex in filmChars) {
        if (filmChars[charIndex].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
