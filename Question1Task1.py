import pandas as pd
import os

csv_directory = r'C:\Users\Christiano\Documents\CSV_Files' 

all_text = []

for filename in os.listdir(csv_directory):
    if filename.endswith('.csv'):
        
        csv_path = os.path.join(csv_directory, filename)
        df = pd.read_csv(csv_path)
        
        
        print(f"Processing file: {filename}")
        print(f"Column names: {df.columns.tolist()}")
        
        if 'TEXT' in df.columns:
            all_text.extend(df['TEXT'].dropna().tolist())
        elif 'SHORT-TEXT' in df.columns:
            all_text.extend(df['SHORT-TEXT'].dropna().tolist())
        else:
            print(f"No 'TEXT' or 'SHORT-TEXT' column found in {filename}")

output_file = r'C:\Users\Christiano\Documents\combined_text.txt' 
with open(output_file, 'w', encoding='utf-8') as f:
    for line in all_text:
        f.write(f"{line}\n") 

print(f"Text from all CSV files has been saved to: {output_file}")