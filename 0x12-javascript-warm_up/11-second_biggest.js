#!/usr/bin/node
if (process.argv.length <= 3) {
  console.log('0');
} else {
  const first_arr = process.argv.slice(2).map(Number);
  const second_arr = first_arr.sort(function (a, b) { return b - a; })[1];
  console.log(second_arr);
}
