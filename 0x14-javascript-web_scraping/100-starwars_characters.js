#!/usr/bin/node

const httpRequest = require('request');
const filmId = process.argv[2];
const apiUrl = 'https://swapi-api.alx-tools.com/api/films/';

httpRequest.get(apiUrl + filmId, function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const filmData = JSON.parse(body);
  const charactersUrls = filmData.characters;
  for (const characterUrl of charactersUrls) {
    httpRequest.get(characterUrl, function (err, res, body1) {
      if (err) {
        console.log(err);
      }
      const characterData = JSON.parse(body1);
      console.log(characterData.name);
    });
  }
});
