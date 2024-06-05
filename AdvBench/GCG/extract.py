import json
import csv


input_file = 'path/advbench/llama2_gcg.json'
output_file = 'gcg.csv'

with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)

with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    
    for item in data:
        if 'nested_prompt' in item:
            csvwriter.writerow([item['nested_prompt']])

print(f"saving to  {output_file}")
