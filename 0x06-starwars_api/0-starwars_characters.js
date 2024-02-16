#!/usr/bin/node
const request = require('request');
const url = 'https://swapi-api.alx-tools.com/api/';

// Function to fetch and display character names
function fetchAndPrintCharacters(movieId) {
  const filmUrl = `${url}films/${movieId}/`;

  // Request to get film details
  request({ url: filmUrl, json: true }, (error, response, body) => {
    if (!error && response.statusCode ===  200) {
      const charactersUrls = body.characters;
      
      // For each character URL, request character details
      charactersUrls.forEach((characterUrl, index) => {
        request({ url: characterUrl, json: true }, (err, res, charBody) => {
          if (!err && res.statusCode ===  200) {
            console.log(charBody.name);
          }
        });
      });
    }
  });
}

// Check if a movie ID was provided
if (process.argv[2]) {
  const movieId = process.argv[2];
  fetchAndPrintCharacters(movieId);
} else {
  console.log('Please provide a movie ID.');
}
