import requests
from bs4 import BeautifulSoup
import os
import time

#This script downloads the top 20 versions of an app from uptodown.com
#Replace the URL on lince 43

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.56 (KHTML, like Gecko) Chrome/123.0.4472.124 Safari/537.36"}

# Function to download a file
def download_file(url, folder):
    local_filename = url.split('/')[-1]
    local_filename = local_filename + ".apk"
    print("FileName: " + str(local_filename))
    local_filepath = os.path.join(folder, local_filename)
    print("FIlePath: " + str(local_filepath))
    # Make sure the folder exists
    os.makedirs(folder, exist_ok=True)
    
    with requests.get(url, stream=True,headers=headers) as r:
        r.raise_for_status()
        with open(local_filepath, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                f.write(chunk)
    return local_filepath

# Function to get the version download links from the page
def get_version_links(page_url):

    response = requests.get(page_url,headers = headers)
    response.raise_for_status()
    
    soup = BeautifulSoup(response.text, 'html.parser')
    version_links = []
    for link in soup.find_all('div'):
        if link.get('data-url') is not None:
           page_url = str(link.get('data-url'))
           download_url = page_url.replace("download","post-download")
           print(download_url)
           version_links.append(download_url)
    print("returning items: " + str(len(version_links)))
    return version_links

# URL of the page containing the versions
url = "https://android-system-webview.en.uptodown.com/android/versions"
folder = 'downloads'

# Get all version links
version_links = get_version_links(url)

# Download all versions
for link in version_links:
    print(f"Downloading {link}")
    download_file(link, folder)
    # Add a delay to avoid hitting the rate limit
    time.sleep(2)

print("All files downloaded.")
