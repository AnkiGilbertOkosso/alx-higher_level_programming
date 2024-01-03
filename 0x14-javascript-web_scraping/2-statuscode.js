#!/usr/bin/node
const httpRequest = require('request');
httpRequest.get(process.argv[2]).on('response', function (res) {
  console.log(`code: ${res.statusCode}`);
});
