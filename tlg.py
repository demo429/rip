function telegramBot() {
  var token = "7537654028:AAGwxMPjGEhmH4A7Gbx72jkRxRtG24L5_d4";
  var chatId = "-1007537654028";
  var url = "https://api.telegram.org/bot" + token;
  
  // Request to get updates from the bot
  var options = {
    'method': 'get',
    'headers': {
      'Content-Type': 'application/json'
    },
    'muteHttpExceptions': true
  };

  var response = UrlFetchApp.fetch(url + "/getUpdates", options);
  var json = JSON.parse(response.getContentText());

  // Loop through each update
  for (var i in json.result) {
    var update = json.result[i];
    
    if (update.message != null && update.message.text != null && update.message.text.startsWith("/search")) {
      var searchQuery = update.message.text.substring(8).trim(); // Extract search query
      var searchResult = performSearch(searchQuery);
      
      // Send the result back to Telegram
      var postOptions = {
        'method': 'post',
        'headers': {
          'Content-Type': 'application/json'
        },
        'muteHttpExceptions': true,
        'payload': JSON.stringify({
          'chat_id': update.message.chat.id,
          'text': searchResult
        })
      };

      UrlFetchApp.fetch(url + "/sendMessage", postOptions);
    }
  }
}

function performSearch(query) {
  var cx = "YOUR_SEARCH_ENGINE_ID"; // Google Custom Search Engine ID
  var apiKey = "YOUR_API_KEY"; // Google API Key
  var searchUrl = "https://www.googleapis.com/customsearch/v1?q=" + encodeURIComponent(query) + "&key=" + apiKey + "&cx=" + cx;

  var options = {
    'method': 'get',
    'muteHttpExceptions': true
  };

  var response = UrlFetchApp.fetch(searchUrl, options);
  var json = JSON.parse(response.getContentText());

  if (json.items && json.items.length > 0) {
    var firstResult = json.items[0];
    return "Title: " + firstResult.title + "\n" + "Link: " + firstResult.link;
  } else {
    return "No results found.";
  }
}

// Run the bot every minute
ScriptApp.newTrigger('telegramBot').timeBased().everyMinutes(1).create();
