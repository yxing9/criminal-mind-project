import os
import requests

#Turns a given URL into a file in this case a pdf file
#NOTE: This function is not working properly printing the return of this function gives the following result
# Albright_Charles.pdf 
# Alcala__Rodney__2012_.pdf
# Allanson_Patricia.pdf
# Anderson_Dale_-_2005.pdf
# Archer-Gilligan_Amy.pdf
def process_url(url):
    file_name = url.split('/')[-1]  # Get the last part of the URL, which is the file name
    file_name = file_name.replace('%20', '_').replace(',', '').replace('.', '_')
    print(file_name[:-4] + '.pdf')
    return file_name[:-4] + '.pdf'  # Replace the last underscore with a dot for the file extension

#The download_pdf function is used to download given pdf files and returns the file path
def download_pdf(url, download_path):
    response = requests.get(url)

    if response.status_code != 200:
        print(f"Error downloading file from {url}: status code {response.status_code}")
        return None

    file_name = process_url(url)
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
