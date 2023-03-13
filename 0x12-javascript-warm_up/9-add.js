#!/usr/bin/node

function add (a, b) {
  const sum = a + b;

  console.log(sum);
}

const firstArg = parseInt(process.argv[2]);
const secondArg = parseInt(process.argv[3]);

add(firstArg, secondArg);
