import random
import string

# A dictionary to store the original URL with a corresponding short URL
url_db = {}

# Base URL for the shortened URL
BASE_URL = "http://short.ly/"

# Function to generate a random short URL key
def generate_short_key(length=6):
    characters = string.ascii_letters + string.digits  # Letters and digits
    short_key = ''.join(random.choice(characters) for _ in range(length))
    return short_key

# Function to shorten the URL
def shorten_url(long_url):
    # Check if the long URL already exists in the dictionary
    for short_key, url in url_db.items():
        if url == long_url:
            return BASE_URL + short_key
    
    # Generate a new short key
    short_key = generate_short_key()

    # Store the long URL with the corresponding short URL key
    url_db[short_key] = long_url

    # Return the shortened URL
    return BASE_URL + short_key

# Function to expand the shortened URL back to the original URL
def expand_url(short_url):
    # Extract the short key from the shortened URL
    short_key = short_url.replace(BASE_URL, '')
    
    # Check if the short key exists in the dictionary
    if short_key in url_db:
        return url_db[short_key]
    else:
        return "Invalid shortened URL."

# Main function to interact with the user
def url_shortener():
    print("Welcome to the URL Shortener!")
    
    while True:
        print("\n1. Shorten a URL")
        print("2. Expand a shortened URL")
        print("3. Exit")
        
        choice = input("Enter your choice (1/2/3): ")
        
        if choice == '1':
            long_url = input("Enter the URL to shorten: ")
            short_url = shorten_url(long_url)
            print(f"Shortened URL: {short_url}")
        
        elif choice == '2':
            short_url = input("Enter the shortened URL: ")
            original_url = expand_url(short_url)
            print(f"Original URL: {original_url}")
        
        elif choice == '3':
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

# Run the URL shortener program
url_shortener()
