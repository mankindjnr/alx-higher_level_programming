#!/usr/bin/node
const firstArg = process.argv[2];
let convertFirstArg;

if (isNaN(firstArg)) {
  console.log('Not a number');
} else {
  convertFirstArg = parseInt(firstArg);
  console.log('My number: ' + convertFirstArg);
}
