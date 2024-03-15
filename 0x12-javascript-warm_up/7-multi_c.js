#!/usr/bin/node

import { argv } from 'node:process';

const occ = Math.floor(Number(argv[2]));
if (isNaN(occ)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < occ; index++) {
    console.log('C is fun');
  }
}
