from openai import OpenAI

API_SECRET_KEY = "**";
BASE_URL = "**/" 

def gpt4v(query):
    client = OpenAI(api_key=API_SECRET_KEY, base_url=BASE_URL)
    response = client.chat.completions.create(
      model="gpt-4-vision-preview",
      messages=[
        {
          "role": "user",
          "content": [
            {"type": "text", "text": query}
          ],
        }
      ],
      max_tokens=300,
    )

    return response.choices[0].message.content

import csv

    
def process_csv_file(input_csv_file_path, output_csv_file_path):
    with open(input_csv_file_path, 'r', newline='') as input_csv_file, open(output_csv_file_path, 'w', newline='') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        csv_writer = csv.writer(output_csv_file)
        for row in csv_reader:
            for data in row:
                try:
                    ans = gpt4v(data)
                except Exception as e:
                    ans = f"Error processing data {data}: {e}"
                csv_writer.writerow([data, ans])

input_csv_file_path = 'path/advbench/gcg.csv'  
output_csv_file_path = 'gcg_4v.csv'  

process_csv_file(input_csv_file_path, output_csv_file_path)

