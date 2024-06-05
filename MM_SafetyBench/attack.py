import os
import csv
from openai import OpenAI
import base64

API_SECRET_KEY = "*";
BASE_URL = "*" 

def encode_image(image_path):
    with open(image_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

def gpt4ov(query,img_path):
    base64_image = encode_image(img_path)
    client = OpenAI(api_key=API_SECRET_KEY, base_url=BASE_URL)
    response = client.chat.completions.create(
      model="gpt-4o",
      messages=[
        {
          "role": "user",
          "content": [
            #{"type": "text", "text": query}
            {"type": "text", "text": query},
            {"type": "image_url", "image_url": {
                "url": f"data:image/png;base64,{base64_image}"}
            }
          ],
        }
      ],
      max_tokens=300,
    )

    return response.choices[0].message.content




input_folder_path = '/home/beihang/yzh/EasyJailbreak/new'

output_folder_path = '/home/beihang/yzh/EasyJailbreak/new/4oresponse'

base_image_folder_path = '/home/beihang/yzh/EasyJailbreak/new/MM-SafetyBench'


for file_name in os.listdir(input_folder_path):
    if file_name.endswith('.csv'):

        input_csv_path = os.path.join(input_folder_path, file_name)
        

        output_csv_path = os.path.join(output_folder_path, file_name)
        

        base_image_path = os.path.join(base_image_folder_path, file_name[:-4],'SD_TYPO')
        
  
        
        with open(input_csv_path, mode='r', newline='', encoding='utf-8') as infile:
            csv_reader = csv.reader(infile)
            
  
            rows = list(csv_reader)
        
 
        with open(output_csv_path, mode='w', newline='', encoding='utf-8') as outfile:
            csv_writer = csv.writer(outfile)
      
            csv_writer.writerow(['Query', 'Processed Result'])
            
     
            for row in rows[1:]: 
                if len(row) >= 2:  
                    name = row[0]
                    query = row[1]
                    
                   
                    image_path = os.path.join(base_image_path, f"{name}.jpg")
                    
                   
                    try:
                      processed_result = gpt4ov(query, image_path)
                    except Exception as e:
                      processed_result = f"Error processing data {image_path}: {e}"
                    
                    
                   
                    csv_writer.writerow([query, processed_result])
         
print("Finished!")

