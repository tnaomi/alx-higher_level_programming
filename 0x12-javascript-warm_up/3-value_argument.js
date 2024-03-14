#!/usr/bin/node

import { argv } from 'node:process';
let count = 0;

argv.forEach((val) => {
  count += 1;
});
if (count > 2) {
  console.log(argv[2]);
} else {
  console.log('No argument');
}
