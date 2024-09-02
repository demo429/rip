import requests
import schedule
import time

# Set your bot's token here
TOKEN = "YOUR_BOT_TOKEN"

# Set your chat ID here
CHAT_ID = "YOUR_CHAT_ID"

# Telegram API URL
URL = f"https://api.telegram.org/bot{TOKEN}"

def get_updates():
    response = requests.get(f"{URL}/getUpdates")
    return response.json()

def send_message(chat_id, text):
    payload = {'chat_id': chat_id, 'text': text}
    response = requests.post(f"{URL}/sendMessage", json=payload)
    return response.json()

def handle_updates():
    updates = get_updates()
    
    for update in updates.get('result', []):
        message = update.get('message', {})
        text = message.get('text', '')
        
        if text.startswith("/search"):
            search_term = text[8:].strip()
            search_results = search_google(search_term)
            
            send_message(CHAT_ID, search_results)

def search_google(query):
    # Google search URL (this is a placeholder, Google does not provide a public API for search)
    search_url = "https://www.google.com/search"
    response = requests.get(search_url, params={'q': query})
    
    # Extracting text from the search result page is complex and not recommended for scraping
    # Placeholder for extracted results
    return "Search results are not available via Google API."

# Schedule the bot to run every minute
schedule.every(1).minute.do(handle_updates)

while True:
    schedule.run_pending()
    time.sleep(1)
