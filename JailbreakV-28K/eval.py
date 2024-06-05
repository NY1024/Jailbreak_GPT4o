from easyjailbreak.models.openai_model import OpenaiModel


target_model_4o = OpenaiModel(model_name='gpt-4o',
                         api_keys='**')

def query_4o(query):
    return target_model_4o.generate(messages=[query])

import csv
import time


import csv


def process_csv_file(input_csv_file_path, output_csv_file_path):
    with open(input_csv_file_path, 'r', newline='') as input_csv_file, open(output_csv_file_path, 'w', newline='') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        csv_writer = csv.writer(output_csv_file)
        for row in csv_reader:
            for data in row:
                try:
                    ans = query_4o(data)
                except Exception as e:
                    ans = f"Error processing data {data}: {e}"
                csv_writer.writerow([data, ans])

input_csv_file_path = 'path/dataset/final.csv' 
output_csv_file_path = '28kout.csv'  

process_csv_file(input_csv_file_path, output_csv_file_path)

