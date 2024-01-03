#!/usr/bin/node
const httpRequest = require('request');
const filmUrl = 'https://swapi-api.alx-tools.com/api/' + process.argv[2];
httpRequest(filmUrl, function (err, res, body) {
  if (!err) {
    const characters = JSON.parse(body).characters;
    printCharacters(characters, 0);
  }
});

function printCharacters(characters, index) {
  httpRequest(characters[index], function (err, res, body) {
    if (!err) {
      console.log(JSON.parse(body).name);
      if (index + 1 < characters.length) {
        printCharacters(characters, index + 1);
      }
    }
  });
}
