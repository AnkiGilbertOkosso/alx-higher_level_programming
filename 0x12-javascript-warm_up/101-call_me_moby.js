#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  for (let num = 0; num < x; num++) {
    theFunction();
  }
};
