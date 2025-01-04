import threading
import requests

# Function to fetch data from an API
def fetch_data(api_url):
    try:
        # Make an HTTP GET request
        response = requests.get(api_url)
        response.raise_for_status()  # Raise exception for HTTP errors
        
        # Print fetched data (for demonstration purposes, only display JSON structure)
        print(f"Data from {api_url}: {response.json()[:3]}") 
    except Exception as e:
        print(f"Error fetching data from {api_url}: {e}")

# List of API URLs to fetch data from
api_urls = [
    "https://jsonplaceholder.typicode.com/posts",
    "https://jsonplaceholder.typicode.com/comments",
    "https://jsonplaceholder.typicode.com/albums"
]

# Create and start threads for concurrent API fetching
threads = []
for url in api_urls:
    thread = threading.Thread(target=fetch_data, args=(url,))
    threads.append(thread)
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

print("Data fetched from all APIs.")
