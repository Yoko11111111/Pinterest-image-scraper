from bs4 import BeautifulSoup
import requests
import os
import urllib.request

response = requests.get("https://www.pinterest.at/HoodesClub/profile/")
soup = BeautifulSoup(response.text, 'html.parser')

img_tags = soup.find_all('img')

img_urls = [img['src'] for img in img_tags]
print(img_urls)

downloaded_urls = set()

if not os.path.exists("images"):
    os.makedirs("images")

for i, url in enumerate(img_urls):
    if url in downloaded_urls:
        print(f"Skipping {url} as already downloaded")
        continue
    try:
        response = requests.get(url)
        with open(f"images/img{i}.jpg", "wb") as img_file:
            img_file.write(response.content)
            downloaded_urls.add(url)
    except:
        print(f'Error in img{i}')

