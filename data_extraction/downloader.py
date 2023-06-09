import os
import requests
from urllib.parse import urlparse, unquote
import re

'''

Functionality: Downloads pdf files from a csv file of urls.

Call clean_data() to generate the correct file name for the downloaded pdf files 
in the form of firstname_lastname.pdf
e.g. given the link: "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Bathory,%20Elizabeth%20-%20spring,%202006.pdf"
the correct output of file name should be "Elizabeth_Bathory.pdf"

Note:
1. Middle names are ignored. 
    e.g. http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Armstrong,%20John%20Eric.pdf
    John_Armstrong.pdf

'''


def clean_data(url):
    path = unquote(urlparse(url).path)
    last_part = path.split('/')[-1]
    
    # Look for a comma, if not found, look for a dot
    separator_index = last_part.find(',')
    separator = ',' if separator_index != -1 else '.'
    if separator == '.':
        separator_index = last_part.find('.')
        
    last_name = last_part[:separator_index]
    first_name_with_extra = last_part[separator_index+2:].split(' ')[0]

    # Checking if any word in the names starts with a non-capitalized letter
    for name_part in re.split('[ ,.]', last_name + ' ' + first_name_with_extra):
        if name_part and not name_part[0].isupper():
            return 'Invalid name'
    
    return f'{first_name_with_extra}_{last_name}.pdf'

#The download_pdf function is used to download given pdf files and returns the file path
def download_pdf(url, download_path):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error downloading file from {url}: status code {response.status_code}")
        return None

    file_name = clean_data(url)
    file_path = os.path.join(download_path, file_name)

    with open(file_path, "wb") as f:
        f.write(response.content)

    return file_path

# returns multiple pdf files and downloads then using the download_pdf function
def download_pdfs(urls, download_path):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    pdf_files = []
    for url in urls:
        pdf_file = download_pdf(url, download_path)
        if pdf_file:
            pdf_files.append(pdf_file)

    return pdf_files
