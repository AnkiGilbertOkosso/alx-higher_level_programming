#!/usr/bin/node
exports.esrever = function (list) {
  let size = list.length - 1;
  let index = 0;
  while ((size - index) > 0) {
    const auxi = list[size];
    list[size] = list[index];
    list[index] = auxi;
    index++;
    size--;
  }
  return list;
};
