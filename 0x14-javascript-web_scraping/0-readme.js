#!/usr/bin/node
const fileSystem = require('fs');
fileSystem.readFile(process.argv[2], 'utf8', function (err, data) {
  console.log(err || data);
});
