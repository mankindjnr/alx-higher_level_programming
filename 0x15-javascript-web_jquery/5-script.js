// Wait for the document to load before executing the script
$(document).ready(function() {

    // Add a click event listener to the #add_item div
    $('#add_item').click(function() {
  
      // Create a new <li> element and add it to the <ul> list
      var newListItem = $('<li>').text('Item');
      $('ul.my_list').append(newListItem);
      
    });
  
  });
  