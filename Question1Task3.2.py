from transformers import AutoTokenizer
from collections import Counter
import csv
import gc

tokenizer = AutoTokenizer.from_pretrained("distilbert-base-uncased")

def process_in_chunks(file_path, chunk_size=5000):
    with open(file_path, 'r', encoding='utf-8') as file:
        while True:
            chunk = file.read(chunk_size)
            if not chunk:
                break
            yield chunk

token_counts = Counter()

input_file = r'C:\Users\Christiano\Documents\combined_text.txt'  
for chunk in process_in_chunks(input_file):
    
    tokens = tokenizer.tokenize(chunk)
    
    token_counts.update(tokens)

    gc.collect()

top_30_tokens = token_counts.most_common(30)

output_file = r'C:\Users\Christiano\Documents\top_30_tokens.csv'  
with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Token', 'Count'])
    writer.writerows(top_30_tokens)

print(f"Top 30 tokens and their counts have been saved to: {output_file}")
