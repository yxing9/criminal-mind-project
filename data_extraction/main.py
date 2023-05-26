import os
import csv

import downloader
import pdf_converter_to_csv
import csv_processor
import csv_merger

# Previous example of list of PDF URLs
# pdf_urls = [
#     "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Albright,%20Charles.pdf",
#     "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Alcala.%20Rodney%20_2012_.pdf",
#     "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Allanson,%20Patricia.pdf",
#     "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Anderson,%20Dale%20-%202005.pdf",
#     "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Archer-Gilligan,%20Amy.pdf",
#     "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Armstrong,%20John%20Eric.pdf",
#     "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Barfield,%20Velma%20-%202005,%20Fall.pdf",
#     "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Bathory,%20Elizabeth%20-%20spring,%202006.pdf",
#     "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Baumeister,%20Herb%20-%20fall,%202005.pdf",
#     "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Beets,%20Betty%20Lou%20_spring%202007_.pdf",
#     "http://maamodt.asp.radford.edu/Psyc%20405/serial%20killers/Berdella,%20Robert.pdf"
# ]

def read_csv_file(input_csv_file):
    pdf_urls = []
    with open(csv_file, newline='') as input_csv_file:
        reader = csv.reader(input_csv_file)
        for row in reader:
            pdf_urls.append(row[0])
    return pdf_urls

if __name__ == "__main__":
    csv_file = "./data/links.csv"
    pdf_urls = read_csv_file(csv_file)


# Create file paths by replacing hard-coded paths
root_folder = "data"
first_layer_folder = "website_to_csv"

pdfs_raw_folder = os.path.join(root_folder, first_layer_folder, "pdfs_raw")
csv_raw_folder = os.path.join(root_folder, first_layer_folder, "csv_raw")
csv_processed_folder = os.path.join(root_folder, first_layer_folder, "csv_processed") # csv_processed_folder = './data/dataExtraction/csv_processed/'
merged_csv_file = os.path.join(root_folder, first_layer_folder, "final_csv", "killers.csv") # './data/dataExtraction/final_csv/killers.csv'

# downloader.py
# Download the PDF files to the specified folder
pdf_raw_files = downloader.download_pdfs(pdf_urls, pdfs_raw_folder) # "./data/dataExtraction/pdfs"
print(pdf_raw_files)

# pdf_converter_to_csv.py
# Convert the downloaded PDF files to CSV files (raw)
csv_raw_files = pdf_converter_to_csv.convert_pdfs_to_csvs(pdf_raw_files, csv_raw_folder) # "./data/dataExtraction/csv_raw"
print("PDF to CSV conversion completed. CSV files generated:")
for csv_raw_file in csv_raw_files:
    print(csv_raw_files)

# csv_processor.py
# Process the raw CSV files and write the output to the 'csv_processed' folder
#TODO: FIX THIS  
csv_processed_files = csv_processor.process_csv_files(csv_raw_files, csv_processed_folder) # "./data/dataExtraction/csv_processed"
print("CSV processing completed. Processed CSV files:")
for csv_processed_file in csv_processed_files:
    print(csv_processed_file)

# csv_merger.py
# Merge the processed CSV files into a single file
csv_merger.merge_csv_files(csv_processed_folder, merged_csv_file)
print("CSV merging completed. Merged CSV files:" + " " + merged_csv_file)
