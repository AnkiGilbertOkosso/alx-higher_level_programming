#!/usr/bin/node
const httpRequest = require('request');
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];

httpRequest(apiUrl, function (error, response, body) {
  if (!error) {
    const charactersList = JSON.parse(body).characters;
    printCharacters(charactersList, 0);
  }
});

function printCharacters(charactersList, index) {
  httpRequest(charactersList[index], function (error, response, body) {
    if (!error) {
      console.log(JSON.parse(body).name);
      if (index + 1 < charactersList.length) {
        printCharacters(charactersList, index + 1);
      }
    }
  });
}
