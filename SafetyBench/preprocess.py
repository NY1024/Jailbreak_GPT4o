import re
import os
#import openai
import requests
import time
import json
import time
#from openai import OpenAI
import csv 

def extract_numbers(input_string):

    numbers = re.findall(r'\d+', input_string)

    return [int(num) for num in numbers]




def process_csv_file(input_csv_file_path, output_csv_file_path):
    with open(input_csv_file_path, 'r', newline='') as input_csv_file, open(output_csv_file_path, 'w', newline='') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        csv_writer = csv.writer(output_csv_file)
        
        for row in csv_reader:
            param1 = row[0]  
            numbers = extract_numbers(param1)
            
            if len(numbers) >= 2:
              
                first_number = numbers[0]
                second_number = numbers[1]
            else:
              
                first_number = numbers[0] if len(numbers) > 0 else None
                second_number = None
            
            csv_writer.writerow([first_number, second_number])


def process_all_files_in_folder(input_folder_path, output_folder_path):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    for filename in os.listdir(input_folder_path):
        if filename.endswith(".csv"):
            input_file_path = os.path.join(input_folder_path, filename)
            output_file_path = os.path.join(output_folder_path, filename)
            process_csv_file(input_file_path, output_file_path)


input_folder_path = 'path/Judge/delete'
output_folder_path = 'path/Judge/delete1'
process_all_files_in_folder(input_folder_path, output_folder_path)



