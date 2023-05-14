import requests
from bs4 import BeautifulSoup

def find_printable_bookmarks(url):
    response = requests.get(url)
    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        bookmark_pins = soup.find_all('a', {'class': 'GrowthUnauthPinImage'})
        
        for pin in bookmark_pins:
            bookmark_url = pin.get('href')
            download_printable_bookmark(bookmark_url)

def download_printable_bookmark(url):
    response = requests.get(url)
    if response.status_code == 200:
        file_name = url.split('/')[-1]
        with open(file_name, 'wb') as f:
            f.write(response.content)
            print(f"Downloaded bookmark: {file_name}")

# Specify the Pinterest board URL where printable bookmarks are located
pinterest_board_url = 'https://www.pinterest.com/karenfrye376/printable-bookmarks/'

find_printable_bookmarks(pinterest_board_url)
