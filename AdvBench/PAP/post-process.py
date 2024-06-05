
import csv
import re
import os 

def process_csv_file(input_csv_file_path, output_csv_file_path):
    with open(input_csv_file_path, 'r', newline='') as input_csv_file, open(output_csv_file_path, 'w', newline='') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        csv_writer = csv.writer(output_csv_file)
        
        for row in csv_reader:
            if len(row) >= 3:  # Ensure the row has at least 3 columns
                third_column_value = row[2]
                # Find all numbers in the third column
                extracted_numbers = str(re.findall(r'\d+', third_column_value))
                # Convert extracted numbers to a single string separated by commas
                #extracted_numbers_str = ', '.join(extracted_numbers)
                # Write the original third column value and the extracted numbers to the output CSV
                csv_writer.writerow([third_column_value, extracted_numbers])
    
    print(f'Processed data has been saved to {output_csv_file_path}')


def process_all_files_in_folder(input_folder_path):

    for filename in os.listdir(input_folder_path):
        if filename.endswith(".csv"):
            input_file_path = os.path.join(input_folder_path, filename)
            output_file_path = os.path.join(output_folder_path, filename)
            process_csv_file(input_file_path,output_file_path)

input_folder_path = 'path/Judge/im1'
output_folder_path = 'path/Judge/im2'
process_all_files_in_folder(input_folder_path)

