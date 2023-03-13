#!/usr/bin/node
if (process.argv.length === 2) {
  console.log('No argumnet');
} else
if (process.argv.length === 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
