#!/usr/bin/node
const SquareP = require('./5-square');

class Square extends SquareP {
  charPrint (i) {
    if (i === undefined) {
      i = 'X';
    }
    for (let indexI = 0; indexI < this.height; indexI++) {
      let txt = '';
      for (let indexJ = 0; indexJ < this.width; indexJ++) {
        txt += i;
      }
      console.log(txt);
    }
  }
}
module.exports = Square;
