#!/usr/bin/node

import { argv } from 'node:process';
let count = 0;
const undef = 'undefined';

argv.forEach((_val) => {
  count += 1;
});

if (count === 4) {
  console.log(argv[2], 'is', argv[3]);
} else if (count === 3) {
  console.log(argv[2], 'is', undef);
} else {
  console.log(undef, 'is', undef);
}
