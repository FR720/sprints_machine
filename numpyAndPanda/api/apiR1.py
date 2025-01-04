import threading
import requests 
import os

# Function to download a file
def download_file(url, file_name):
    try:
        response = requests.get(url)
        response.raise_for_status()  # Check for HTTP errors
        with open(file_name, 'wb') as f:  # Open file in binary write mode
            f.write(response.content)
        print(f"{file_name} downloaded successfully.")
    except Exception as e:
        print(f"Error downloading {file_name}: {e}")

# List of file URLs to download
urls = [
    "https://cdn.futura-sciences.com/cdn-cgi/image/width=1024,quality=50,format=auto/sources/images/AI-creation.jpg",  
    "https://next-images.123rf.com/index/_next/image/?url=https://assets-cdn.123rf.com/index/static/assets/top-section-bg.jpeg&w=3840&q=75",
    "https://img-cdn.pixlr.com/image-generator/history/65bb506dcb310754719cf81f/ede935de-1138-4f66-8ed7-44bd16efc709/medium.webp"
]

# Create and start threads for concurrent downloading
threads = []
for i, url in enumerate(urls):
    file_name = f"image{i + 1}"+".png"
    thread = threading.Thread(target=download_file, args=(url, file_name))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()

print("All files downloaded.")
