import requests

# API URL for JSONPlaceholder posts
url = "https://jsonplaceholder.typicode.com/posts"

try:
    # Make an HTTP GET request to fetch the data
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
    
    # Convert the response to JSON
    posts = response.json()

    print("Titles of the posts:")
    for post in posts:  # Loop through each post
        print(post['title'])  # Print the title of each post
except Exception as e:
    print(f"Error fetching data: {e}")
