#!/usr/bin/node

// Query a URL and log the status code

const url = process.argv[2];
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    console.log('code: ', response && response.statusCode);
  }
});
