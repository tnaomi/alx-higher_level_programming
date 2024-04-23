#!/usr/bin/node

// Write to a file using 'fs' with variadic args

const path = process.argv[2];
const input = process.argv[3];
const fs = require('fs');

fs.writeFile(path, input, { encoding: 'utf-8', mode: 0o666 }, function (err, _data) {
  if (err) {
    console.log(err);
  }
});
