#!/usr/bin/node
let nArg = 0;

exports.logMe = function (item) {
  console.log(nArg + ': ' + item);
  nArg++;
};
