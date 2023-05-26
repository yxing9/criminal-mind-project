import requests
from bs4 import BeautifulSoup
import csv
import os
from urllib.parse import urljoin

def extract_urls(url, output_file):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    all_links = [urljoin(url, link.get('href')) for link in soup.find_all('a') if link.get('href')]
    links_to_download = all_links[:-2] # All urls except the last two

    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    with open(output_file, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        for link in links_to_download:
            writer.writerow([link])

if __name__ == "__main__":
    url = "http://maamodt.asp.radford.edu/Psyc%20405/serial_killer_timelines.htm"

    root_folder = "data"

    pdfs_raw_folder = os.path.join(root_folder, "pdfs_raw")
    output_file = os.path.join(root_folder, "links.csv")
    extract_urls(url, output_file)

    # Printing successful message
    print("CSV links downloading completed. Saved to file:" + " " + output_file)
