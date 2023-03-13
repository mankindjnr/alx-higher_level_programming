#!/usr/bin/node

function recurse (integer) {
  if (integer <= 1) {
    return 1;
  } else {
    return integer * recurse(integer - 1);
  }
}

if (process.argv.length === 2) {
  console.log('1');
} else {
  const rec = recurse(parseInt(process.argv[2]));
  console.log(rec);
}
