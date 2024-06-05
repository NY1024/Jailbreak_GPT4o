import os
import json
import csv


folder_path = 'path/Liu/MM-SafetyBench-main/data/processed_questions/'


for file_name in os.listdir(folder_path):
    if file_name.endswith('.json'):
      
        json_file_path = os.path.join(folder_path, file_name)
        
        
        csv_file_path = os.path.join('path/new', file_name.replace('.json', '.csv'))
        
   
        with open(json_file_path, 'r', encoding='utf-8') as json_file:
            data = json.load(json_file)
        

        with open(csv_file_path, mode='w', newline='', encoding='utf-8') as csv_file:
            csv_writer = csv.writer(csv_file)
    
            csv_writer.writerow(['ID', 'Rephrased Question'])
            
 
            for key, value in data.items():
                if 'Rephrased Question' in value:

                    rephrased_question = value['Rephrased Question']
                    
     
                    csv_writer.writerow([key, rephrased_question])

print("Finished")
