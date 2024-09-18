import csv
from collections import Counter

def process_file_in_chunks(file_path, chunk_size=1024):
    """
    Generator function that yields chunks of the file.
    :param file_path: The path to the large text file.
    :param chunk_size: The size of each chunk to read (in bytes). Default is 1KB.
    :yield: A chunk of text.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            while True:
                chunk = file.read(chunk_size)
                if not chunk:
                    break
                yield chunk
    except FileNotFoundError:
        print(f"File {file_path} not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

word_counts = Counter()

for chunk in process_file_in_chunks('C:/Users/Christiano/Documents/HIT137 - Assesment 2/Question 1 Task 1.txt'):
    words = chunk.lower().split()
    word_counts.update(words) 

top_30_words = word_counts.most_common(30)

with open('top_30_words.csv', 'w', newline='', encoding='utf-8') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Word', 'Count'])
    writer.writerows(top_30_words)

print("Top 30 words and their counts have been written to top_30_words.csv")