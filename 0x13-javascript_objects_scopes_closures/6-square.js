#!/usr/bin/node
const Ssquare = require('./5-square');

class Square extends Ssquare {
  charPrint (c) {
    if (!c) {
      let row = '';

      for (let i = 0; i < this.height; i++) {
        row += 'X';
      }

      for (let j = 0; j < this.width; j++) {
        console.log(row);
      }
    } else {
      let row = '';

      for (let i = 0; i < this.height; i++) {
        row += c;
      }

      for (let j = 0; j < this.width; j++) {
        console.log(row);
      }
    }
  }
}

module.exports = Square;
