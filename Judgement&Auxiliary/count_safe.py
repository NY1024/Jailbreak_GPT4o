import csv
import os

def count_safe_unsafe(csv_file_path):
    safe_count = 0
    unsafe_count = 0
    
    with open(csv_file_path, mode='r', newline='') as csvfile:
        csvreader = csv.reader(csvfile)
        
        for row in csvreader:
            if len(row) >= 3:  # Ensure the row has at least 3 columns
                third_column_value = row[2].strip().lower()
                if 'safe' in third_column_value:
                    safe_count += 1
                if 'unsafe' in third_column_value:
                    unsafe_count += 1
    print(f'csv_file_path:{csv_file_path}')
    print(f'Safe count: {safe_count}')
    print(f'Unsafe count: {unsafe_count}')


def process_all_files_in_folder(input_folder_path):

    for filename in os.listdir(input_folder_path):
        if filename.endswith(".csv"):
            input_file_path = os.path.join(input_folder_path, filename)
            #output_file_path = os.path.join(output_folder_path, filename)
            count_safe_unsafe(input_file_path)

input_folder_path = 'path/Judge/lastdata2'
output_folder_path = 'path/Judge/lastdata3'
process_all_files_in_folder(input_folder_path)





