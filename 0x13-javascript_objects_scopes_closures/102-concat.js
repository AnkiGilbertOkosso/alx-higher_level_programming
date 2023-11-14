#!/usr/bin/node
const s = require('fs');

const f = s.readFileSync(process.argv[2]).toString();
const sArg = s.readFileSync(process.argv[3]).toString();
s.writeFileSync(process.argv[4], f + sArg);
