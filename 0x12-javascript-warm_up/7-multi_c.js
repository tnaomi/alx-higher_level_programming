#!/usr/bin/node

const occ = Math.floor(Number(process.argv[2]));
if (isNaN(occ)) {
  console.log('Missing number of occurrences');
} else {
  for (let index = 0; index < occ; index++) {
    console.log('C is fun');
  }
}
