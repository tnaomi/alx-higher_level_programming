#!/usr/bin/node

import { argv } from 'node:process';
let count = 0; let buffer1; let results = [];
const numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9];

argv.forEach((val, index) => {
  count += 1;
});

if (count > 2) {
  buffer1 = argv[2];
  for (let index = 0; index < buffer1.length; index++) {
    if (buffer1[index] === '-' && buffer1[index + 1] in numbers) {
      results.push(buffer1[index]);
    }
    if (buffer1[index] in numbers) {
      results.push(buffer1[index]);
    }
  }
  if (results.length === 0) {
    console.log('Not a number');
  } else {
    if (results[0] !== '-') {
      results = results.filter((value, index, array) => array.indexOf(value) === index);
    }
    console.log('My number: ', results.toString().replace(/,/g, ''), results.length);
  }
} else {
  console.log('Not a number');
}
