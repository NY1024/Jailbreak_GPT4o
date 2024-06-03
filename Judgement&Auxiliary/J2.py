from transformers import AutoTokenizer, AutoModelForCausalLM
import torch
import csv
import os

model_id = "path/LlamaGuard-7b"
device = "cuda"
dtype = torch.bfloat16

tokenizer = AutoTokenizer.from_pretrained(model_id)
model = AutoModelForCausalLM.from_pretrained(model_id, torch_dtype=dtype, device_map=device)

def moderate(chat):
    input_ids = tokenizer.apply_chat_template(chat, return_tensors="pt").to(device)
    output = model.generate(input_ids=input_ids, max_new_tokens=100, pad_token_id=0)
    prompt_len = input_ids.shape[-1]
    return tokenizer.decode(output[0][prompt_len:], skip_special_tokens=True)

def judge(query,response):
    ans = moderate([
    {"role": "user", "content": query},
    {"role": "assistant", "content": response},
])
    return ans



def process_csv_file(input_csv_file_path, output_csv_file_path):
    with open(input_csv_file_path, 'r', newline='') as input_csv_file, open(output_csv_file_path, 'w', newline='') as output_csv_file:
        csv_reader = csv.reader(input_csv_file)
        csv_writer = csv.writer(output_csv_file)
        for row in csv_reader:
            param1 = row[0]
            param2 = row[1]
            try:
                ans = judge(param1,param2)
            except Exception as e:
                ans = f"Error processing data {param1}: {e}"
            csv_writer.writerow([param1,param2, ans])

def process_all_files_in_folder(input_folder_path, output_folder_path):
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)
    
    for filename in os.listdir(input_folder_path):
        if filename.endswith(".csv"):
            input_file_path = os.path.join(input_folder_path, filename)
            output_file_path = os.path.join(output_folder_path, filename)
            process_csv_file(input_file_path, output_file_path)

input_folder_path = 'path/Judge/pj1'
output_folder_path = 'path/Judge/pj2'
process_all_files_in_folder(input_folder_path, output_folder_path)


