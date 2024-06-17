#!/usr/bin/node

const dim = Math.floor(Number(process.argv[2]));
if (isNaN(dim)) {
  console.log('Missing size');
} else {
  for (let r = 0; r < dim; r++) {
    let row = '';
    for (let c = 0; c < dim; c++) row += 'X';
    console.log(row);
  }
}
