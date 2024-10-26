import random
import time
import requests
from bs4 import BeautifulSoup
import nltk

# Ensure you have the necessary NLTK resources
nltk.download('punkt')

# Function to scrape a webpage and analyze its content
def scrape_and_analyze(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            print(f"Visiting: {url}")
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Extract title and text for analysis
            title = soup.title.string if soup.title else 'No title'
            text = soup.get_text()
            
            # Simple tokenization using NLTK
            words = nltk.word_tokenize(text)
            word_count = len(words)
            
            print(f"Title: {title}")
            print(f"Word Count: {word_count}")
        else:
            print(f"Failed to retrieve {url} - Status code: {response.status_code}")
    except Exception as e:
        print(f"Error while visiting {url}: {e}")

# Function to visit a list of URLs randomly at intervals
def visit_urls_randomly(urls, min_interval, max_interval):
    while True:
        # Choose a random URL from the list
        url = random.choice(urls)
        scrape_and_analyze(url)
        
        # Wait for a random interval between min_interval and max_interval
        wait_time = random.uniform(min_interval, max_interval)
        print(f"Waiting for {wait_time:.2f} seconds...")
        time.sleep(wait_time)

if __name__ == "__main__":
    # List of URLs to visit
    urls_to_visit = [
        "https://www.example.com",
        "https://www.example.org",
        "https://www.example.net",
        # Add more URLs as needed
    ]
    
    # Define the minimum and maximum intervals (in seconds)
    min_interval = 10  # Minimum wait time between visits
    max_interval = 30  # Maximum wait time between visits

    visit_urls_randomly(urls_to_visit, min_interval, max_interval)
