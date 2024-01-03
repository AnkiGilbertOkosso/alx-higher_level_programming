#!/usr/bin/node

const httpRequest = require('request');
const episodeNum = process.argv[2];
const API_URL = 'https://swapi-api.alx-tools.com/api/films/';

httpRequest(API_URL + episodeNum, function (error, res, body) {
  if (error) {
    console.log(error);
  } else if (res.statusCode === 200) {
    const responseJSON = JSON.parse(body);
    console.log(responseJSON.title);
  } else {
    console.log('Error code: ' + res.statusCode);
  }
});
