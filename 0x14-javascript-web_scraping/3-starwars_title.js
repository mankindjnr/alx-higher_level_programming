#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];
request(`https://swapi-api.alx-tools.com/api/films/${movieId}`, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movieData = JSON.parse(body);
  console.log(`${movieData.title}`);
});
