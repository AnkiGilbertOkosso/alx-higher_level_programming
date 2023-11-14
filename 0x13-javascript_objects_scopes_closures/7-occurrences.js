#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let nOccurrences = 0;
  for (let index = 0; index < list.length; index++) {
    if (searchElement === list[index]) {
      nOccurrences++;
    }
  }
  return nOccurrences;
};
