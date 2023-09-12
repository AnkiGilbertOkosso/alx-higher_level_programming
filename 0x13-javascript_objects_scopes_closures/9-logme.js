#!/usr/bin/node
let n_arg = 0;

exports.logMe = function (item) {
  console.log(n_arg + ': ' + item);
  n_arg++;
};

