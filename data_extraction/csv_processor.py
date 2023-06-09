import os
import csv
import re

'''

Functionality: Processes and extracts useful information from newly downloaded csv files.

1. Uses search phrases to select column names
2. Convert yes/no to 1/0

'''

def parse_csv(input_csv):
    data = []
    search_phrases = [
        "Sex", "Race", "Number of victims", "Date of birth", "Birth order", 
        "Physically attractive?", "Physical defect?", "Speech defect?", 
        "Physically abused? ", "Psychologically abused?", "Sexually abused?"
        "Animal torture", "Fire setting", "Bed wetting", "Abused drugs?", "Abused alcohol?",
        "Been to a psychologist (prior to killing)?", "Time in forensic hospital (prior to killing)?",
        "Diagnosis", "Rape?", "Tortured victims?", "Overkill?", "Quick & efficient?",
        "Used blindfold?", "Bound the victims?", "Sex with the body?", "Mutilated body?",
        "Ate part of the body?", "Drank victim’s blood?", "Posed the body?",
        "Took totem – body part", "Took totem – personal item", "Robbed victim or location",
        "Left at scene, no attempt to hide", "Left at scene, hidden", "Left at scene, buried",
        "Moved, no attempt to hide", "Moved, buried", "Cut-op and disposed of", "Moved, too home"
    ]

    # Create a regex pattern for each search phrase
    regex_patterns = [re.compile(f'{re.escape(phrase)},([^,]+)', re.IGNORECASE) for phrase in search_phrases]

    row_data = {}
    with open(input_csv, newline='') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            row_str = ','.join(row)  # Convert the row into a single string
            for phrase, pattern in zip(search_phrases, regex_patterns):
                match = pattern.search(row_str)
                if match:
                    value = match.group(1).strip()  # Extract the value after the search phrase
                    if value.lower() == 'yes':
                        row_data[phrase] = 1  # Convert 'Yes' to 1
                    elif value.lower() == 'no':
                        row_data[phrase] = 0  # Convert 'No' to 0
                    else:
                        row_data[phrase] = value  # Keep original value for non Yes/No entries

    killer_name = os.path.basename(input_csv)[:-4]  # Remove '.csv' from the file name
    row_data['Killer name'] = killer_name

    return [row_data]

def write_csv(data, output_csv):
    search_phrases = [
        "Sex", "Race", "Number of victims", "Date of birth", "Birth order", 
        "Physically attractive?", "Physical defect?", "Speech defect?", 
        "Physically abused? ", "Psychologically abused?", "Sexually abused?"
        "Animal torture", "Fire setting", "Bed wetting", "Abused drugs?", "Abused alcohol?",
        "Been to a psychologist (prior to killing)?", "Time in forensic hospital (prior to killing)?",
        "Diagnosis", "Rape?", "Tortured victims?", "Overkill?", "Quick & efficient?",
        "Used blindfold?", "Bound the victims?", "Sex with the body?", "Mutilated body?",
        "Ate part of the body?", "Drank victim’s blood?", "Posed the body?",
        "Took totem – body part", "Took totem – personal item", "Robbed victim or location",
        "Left at scene, no attempt to hide", "Left at scene, hidden", "Left at scene, buried",
        "Moved, no attempt to hide", "Moved, buried", "Cut-op and disposed of", "Moved, too home"
    ]

    fieldnames = ['Killer name'] + search_phrases

    with open(output_csv, 'w', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in data:
            writer.writerow(row)

def process_csv_files(input_csv_files, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    output_csv_files = []
    for input_csv in input_csv_files:
        output_file_name = os.path.splitext(os.path.basename(input_csv))[0] + '_processed.csv'
        output_csv = os.path.join(output_folder, output_file_name)

        data = parse_csv(input_csv)
        write_csv(data, output_csv)

        output_csv_files.append(output_csv)

    return output_csv_files
