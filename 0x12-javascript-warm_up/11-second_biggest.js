#!/usr/bin/node

let i; const arg = [];

const len = process.argv.length;

function sortAscending (argumnets) {
  const sorted = [];

  while (argumnets.length > 0) {
    const minIndex = argumnets.indexOf(Math.min(...argumnets));
    sorted.push(argumnets[minIndex]);
    argumnets.splice(minIndex, 1);
  }
  return sorted;
}

if (len === 2 | len === 3) {
  console.log('0');
} else {
  // storing the argumnets in an array and convert to integers
  for (i = 2; i < len; i++) {
    arg.push(parseInt(process.argv[i]));
  }

  // the secon last object 2 elements are the names of the program
  console.log((sortAscending(arg)[len - 4]));
}
