$(document).ready(function() {

    // Send an HTTP GET request to the SWAPI API
    $.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data) {
  
      // Extract the list of movie titles from the response
      var movies = data.results;
      var movieTitles = movies.map(function(movie) {
        return '<li>' + movie.title + '</li>';
      });
  
      // Display the movie titles in the <ul> element
      $('#list_movies').html(movieTitles.join(''));
  
    });
  
  });
  