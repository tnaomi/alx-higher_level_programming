#!/usr/bin/node

// Read a file using 'fs', print (err) or (data)

const input = process.argv[2];
const fs = require('fs');

fs.readFile(input, 'utf-8', function (err, data) {
  if (err) {
    console.log(err);
  } else {
    console.log(data);
  }
});
