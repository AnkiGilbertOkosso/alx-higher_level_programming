#!/usr/bin/node
const fileSystem = require('fs');
fileSystem.writeFile(process.argv[2], process.argv[3], err => {
  if (err) console.log(err);
});
