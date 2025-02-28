import os
import collections
import socket
import re

# Define input and output paths
input_folder = "/home/data"
output_folder = os.path.join(input_folder, "output")
output_file = os.path.join(output_folder, "result.txt")

# Ensure output directory exists
os.makedirs(output_folder, exist_ok=True)

# Define file paths
file1_path = os.path.join(input_folder, "IF-1.txt")
file2_path = os.path.join(input_folder, "AlwaysRememberUsThisWay-1.txt")

# Function to clean and split words, handling contractions
def preprocess_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9' ]", "", text)  # Remove special characters except apostrophes
    words = text.split()
    
    # Handling contractions (splitting)
    expanded_words = []
    for word in words:
        if "'" in word:  # Possible contraction
            expanded_words.extend(re.split(r"'", word))
        else:
            expanded_words.append(word)
    
    return expanded_words

# Function to count words in a file
def count_words(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = preprocess_text(file.read())
            return words
    except FileNotFoundError:
        print(f"Error: {file_path} not found!")
        return []

# Get words from both files
file1_words = count_words(file1_path)
file2_words = count_words(file2_path)

# Word count calculations
file1_word_count = len(file1_words)
file2_word_count = len(file2_words)
grand_total_words = file1_word_count + file2_word_count

# Compute top 3 words
top3_file1 = collections.Counter(file1_words).most_common(3)
top3_file2 = collections.Counter(file2_words).most_common(3)

# Get container's IP address
ip_address = socket.gethostbyname(socket.gethostname())

# Format output
output_text = f"""
Word count for IF-1.txt: {file1_word_count}
Word count for AlwaysRememberUsThisWay-1.txt: {file2_word_count}
Grand total of words: {grand_total_words}
Top 3 words in IF-1.txt: {top3_file1}
Top 3 words in AlwaysRememberUsThisWay-1.txt: {top3_file2}
Container IP Address: {ip_address}
"""

# Write to output file
with open(output_file, "w", encoding="utf-8") as result_file:
    result_file.write(output_text.strip())

# Print results to console
print(output_text.strip())
