#!/usr/bin/node
const x = process.argv[2];
let convertX, i;

if (!(+x)) {
  console.log('Missing number of occurences');
} else {
  convertX = parseInt(x);

  for (i = 0; i < convertX; i++) {
    console.log('C is fun');
  }
}
