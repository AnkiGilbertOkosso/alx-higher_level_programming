#!/usr/bin/node
exports.esrever = function (list) {
  let lenn = list.length - 1;
  let i = 0;
  while ((lenn - i) > 0) {
    const auxs = list[lenn];
    list[lenn] = list[i];
    list[i] = auxs;
    i++;
    lenn--;
  }
  return list;
};
