import os
import csv

import downloader
import pdf_converter_to_csv
import csv_processor
import csv_merger


'''

Steps: (1 of 1)
1. Run main.py to see the final result.

Hidden steps: (Sequence function calls under main.py)
1. downloader.py
    downloads pdf files from a csv file as a list of urls
2. pdf_converter_to_csv.py
    converts from the downloaded pdf files to csv files
3. csv_processor.py
    select column names in the csv files
4. csv_merger.py
    merge multiple csv files to one csv file

'''


# Generate a list of urls from a csv file of urls
def read_csv_file(input_csv_file):
    pdf_urls = []
    with open(csv_file, newline='') as input_csv_file:
        reader = csv.reader(input_csv_file)
        for row in reader:
            pdf_urls.append(row[0])
    return pdf_urls

if __name__ == "__main__":

    # Using full links
    csv_file = "./data/links.csv"
    
    # Using test links
    # csv_file = "./data/sample_links.csv"
    pdf_urls = read_csv_file(csv_file)

# Create file paths by replacing hard-coded paths
root_folder = "data"
first_layer_folder = "website_to_csv"

pdfs_raw_folder = os.path.join(root_folder, first_layer_folder, "pdfs_raw")
csv_raw_folder = os.path.join(root_folder, first_layer_folder, "csv_raw")
csv_processed_folder = os.path.join(root_folder, first_layer_folder, "csv_processed") # csv_processed_folder = './data/dataExtraction/csv_processed/'
merged_csv_file = os.path.join(root_folder, first_layer_folder, "final_csv", "killers.csv") # './data/dataExtraction/final_csv/killers.csv'

# Call downloader.py
# Download the PDF files to the specified folder
pdf_raw_files = downloader.download_pdfs(pdf_urls, pdfs_raw_folder) # "./data/dataExtraction/pdfs"
print(pdf_raw_files)

# Call pdf_converter_to_csv.py
# Convert the downloaded PDF files to CSV files (raw)
csv_raw_files = pdf_converter_to_csv.convert_pdfs_to_csvs(pdf_raw_files, csv_raw_folder) # "./data/dataExtraction/csv_raw"
print("PDF to CSV conversion completed. CSV files generated:")
for csv_raw_file in csv_raw_files:
    print(csv_raw_files)

# Call csv_processor.py
# Process the raw CSV files and write the output to the 'csv_processed' folder
csv_processed_files = csv_processor.process_csv_files(csv_raw_files, csv_processed_folder) # "./data/dataExtraction/csv_processed"
print("CSV processing completed. Processed CSV files:")
for csv_processed_file in csv_processed_files:
    print(csv_processed_file)

# Call csv_merger.py
# Merge the processed CSV files into a single file
csv_merger.merge_csv_files(csv_processed_folder, merged_csv_file)
print("CSV merging completed. Merged CSV files:" + " " + merged_csv_file)
