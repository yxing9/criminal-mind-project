import os
import tabula

def pdf_to_csv(pdf_file, csv_file):
    try:
        tabula.convert_into(pdf_file, csv_file, output_format="csv", pages='all')
    except Exception as e:
        print(f"Error converting {pdf_file} to CSV: {e}")

def convert_pdfs_to_csvs(pdf_files, output_csv_folder):
    if not os.path.exists(output_csv_folder):
        os.makedirs(output_csv_folder)

    csv_files = []
    for pdf_file in pdf_files:
        file_name = os.path.splitext(os.path.basename(pdf_file))[0] + '.csv'
        csv_file = os.path.join(output_csv_folder, file_name)
        pdf_to_csv(pdf_file, csv_file)
        csv_files.append(csv_file)

    return csv_files
