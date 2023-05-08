#!/usr/bin/node

const request = require('request');

const apiUrl = process.argv[2];
const characterId = 18;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const movieData = JSON.parse(body).results;
  let count = 0;
  movieData.forEach(movie => {
    const characters = movie.characters;
    if (characters.includes(`https://swapi-api.alx-tools.com/api/people/${characterId}/`)) {
      count++;
    }
  });
  console.log(`${count}`);
});
