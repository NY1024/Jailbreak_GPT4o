import os
import pandas as pd

def count_fail_success_in_csv(folder_path):
    
    for file_name in os.listdir(folder_path):
        
        if file_name.endswith('.csv'):
            file_path = os.path.join(folder_path, file_name)
            try:
               
                df = pd.read_csv(file_path)
              
                if df.shape[1] < 2:
                    print(f"{file_name}")
                    continue
                
                second_column = df.iloc[:, 1].astype(str)
               
                fail_count = second_column.str.contains('fail', case=False).sum()
                success_count = second_column.str.contains('success', case=False).sum()
                
                print(f"{file_name}: fail = {fail_count}, success = {success_count}")
            except Exception as e:
                print(f"error {file_name} : {e}")

folder_path = '/home/beihang/yzh/EasyJailbreak/Judge/string_4o'


count_fail_success_in_csv(folder_path)
