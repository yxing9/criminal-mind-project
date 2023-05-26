import os
import csv
import glob

def merge_csv_files(input_folder, output_file):
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    csv_files = glob.glob(os.path.join(input_folder, '*.csv'))
    header_written = False

    with open(output_file, 'w', newline='') as outfile:
        writer = csv.writer(outfile)
        for csv_file in csv_files:
            with open(csv_file, newline='') as infile:
                reader = csv.reader(infile)
                header = next(reader)
                if not header_written:
                    writer.writerow(header)
                    header_written = True

                for row in reader:
                    writer.writerow(row)
