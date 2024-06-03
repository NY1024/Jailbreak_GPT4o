import csv
import re
def extract_numbers_from_third_column(input_file, output_file):
    with open(input_file, mode='r', newline='') as infile, open(output_file, mode='w', newline='') as outfile:
        reader = csv.reader(infile)
        writer = csv.writer(outfile)

        for row in reader:
            if len(row) < 3:
                continue  
            
            third_column_content = row[2]
            
            numbers = re.findall(r'\d+', third_column_content)
            
            new_row = row[:2]  
            new_row.extend(numbers)  
            writer.writerow(new_row)

input_file = 'path/28k_gpt4o_result.csv'
output_file = 'path/28k_gpt4o_result2.csv'
extract_numbers_from_third_column(input_file, output_file)
