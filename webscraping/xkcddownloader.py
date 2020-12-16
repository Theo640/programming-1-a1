# xkcddownloader.py
# automated download of xkcd from web

import os
import requests
import bs4

# setup the url for xkcd
url = "https://xkcd.com"

# create a folder to store the comics
os.makedirs("xkcd_pictures", exist_ok=True)

# loop to download all the comics
while not url.endswith("#"):
    # TODO: download the page (html)
    print(f"Downloading page {url}...")
    res = requests.get(url)
    res.raise_for_status()
    soup = bs4.BeautifulSoup(res.text, "html.parser")

    # TODO: find the URL of the picture using bs4
    # TODO: download the image
    # TODO: save the image
    # TODO: get the Previous button URL
    prev_link = soup.select('a[rel="prev"]')[0] # "/2396/"
    url = "https//xkcd.com" + prev_link.get("href")

print("Done")