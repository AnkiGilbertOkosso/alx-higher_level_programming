#!/usr/bin/node
const dict = require('./101-data').dict;

const totList = Object.entries(dict);
const val = Object.values(dict);
const valUniq = [...new Set(val)];
const newDict = {};
for (const indexJ in valUniq) {
  const list = [];
  for (const indexK in totList) {
    if (totList[indexK][1] === valUniq[indexJ]) {
      list.unshift(totList[indexK][0]);
    }
  }
  newDict[valUniq[indexJ]] = list;
}
console.log(newDict);
