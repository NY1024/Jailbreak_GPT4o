import json
import csv


input_file = 'path/advbench/llama2_autodan.json'
output_file = 'autodan.csv'


with open(input_file, 'r', encoding='utf-8') as file:
    data = json.load(file)


with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    csvwriter = csv.writer(csvfile)
    

    for key, value in data.items():
        if 'goal' in value and 'final_suffix' in value:
            combined_text = f"{value['goal']} {value['final_suffix']}"
            csvwriter.writerow([combined_text])

print(f"saving to {output_file}")
