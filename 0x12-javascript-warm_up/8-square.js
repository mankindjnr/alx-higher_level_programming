#!/usr/bin/node
const firstArg = process.argv[2];
let i, j, convertFirstArg;

if (!(+firstArg)) {
  console.log('Missing size');
} else {
  convertFirstArg = parseInt(firstArg);

  for (i = 0; i < convertFirstArg; i++) {
    let row = '';

    for (j = 0; j < convertFirstArg; j++) {
      row += 'X';
    }
    console.log(row);
  }
}
