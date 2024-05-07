# Imports
import requests
from bs4 import BeautifulSoup

# Functions
def check_website(url):
    response = requests.get(url)
    if response.status_code == 200:
        print(f"Website {url} is up and running.")
        generate_website_report(url)
    else:
        print(f"Website {url} returned status code {response.status_code}.")

def generate_website_report(url):
    response = requests.get(url) # Retrives information
    if response.status_code == 200: # Returns status code of URL and checks it
        soup = BeautifulSoup(response.content, 'html.parser') # This will retrive all the html tag content
        title = soup.title.string.strip() # it returns title of website
        print(f"Title of website: {title}")

        images = soup.find_all('img')
        num_images = len(images)
        print(f"Number of Images: {num_images}")

        header_tags = ['h1', 'h2', 'h3', 'h4', 'h5', 'h6']
        print("Header Tags:")
        for tag in header_tags:
            headers = soup.find_all(tag)
            num_headers = len(headers)
            print(f"{tag}: {num_headers}")

        # Number of paragraphs
        paragraphs = soup.find_all('p')
        num_paragraphs = len(paragraphs)
        print(f"Number of Paragraphs: {num_paragraphs}")

        # Number of links with different attributes
        links = soup.find_all('a')
        num_links = len(links)
        print(f"Number of Links: {num_links}")

    else:
        print(f"Error: Unable to fetch website data. Status code: {response.status_code}")

# Executable part
# User input for Website URL
url = input("Enter the URL of the website to check and generate report: ")

# Function call
check_website(url)

