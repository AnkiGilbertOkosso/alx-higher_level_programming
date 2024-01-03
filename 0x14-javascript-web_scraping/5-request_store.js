#!/usr/bin/node
const fileSystem = require('fs');
const httpRequest = require('request');
httpRequest(process.argv[2]).pipe(fileSystem.createWriteStream(process.argv[3]));
