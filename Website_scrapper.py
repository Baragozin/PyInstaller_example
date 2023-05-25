import time
import requests
from bs4 import BeautifulSoup

# Ask the user for the website URL
url = input("Enter the website URL: ")

# Send a request to the website and get the HTML content
response = requests.get(url)
html_content = response.content

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Extract the data you want from the HTML using BeautifulSoup methods
title = soup.title.string
links = [link.get('href') for link in soup.find_all('a')]

# Output the results to a file
with open('output.txt', 'w') as f:
    f.write("Title: {}\n".format(title))
    f.write("Links: {}\n".format(links))

print("Check your folder")
time.sleep(2)
input("Нажмите Enter для выхода")