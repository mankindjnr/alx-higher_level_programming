$(document).ready(function() {

    // Send an HTTP GET request to the SWAPI API
    $.get('https://swapi-api.alx-tools.com/api/people/5/?format=json', function(data) {
  
      // Extract the character name from the response
      var characterName = data.name;
  
      // Display the character name in the <div> element
      $('#character').text(characterName);
  
    });
  
  });
  