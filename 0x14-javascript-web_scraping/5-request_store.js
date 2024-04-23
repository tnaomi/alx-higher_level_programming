#!/usr/bin/node

// Store contents of a webpage in a file

const url = process.argv[2];
const path = process.argv[3];
const fs = require('fs');
const request = require('request');

request(url, function (err, response, body) {
  if (err) {
    console.error(err);
  } else {
    fs.writeFile(path, body, { encoding: 'utf-8', mode: 0o666 }, function (err, _data) {
      if (err) {
        console.log(err);
      }
    });
  }
});
