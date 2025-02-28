import os

input_folder = "/home/data"  # Ensure this is the correct path inside the container

file1_path = os.path.join(input_folder, "IF-1.txt")
file2_path = os.path.join(input_folder, "AlwaysRememberUsThisWay-1.txt")

def count_words(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            words = file.read().split()
            return words
    except FileNotFoundError:
        print(f"Error: {file_path} not found!")
        return []

file1_words = count_words(file1_path)
file2_words = count_words(file2_path)

if file1_words and file2_words:
    print(f"IF-1.txt has {len(file1_words)} words")
    print(f"AlwaysRememberUsThisWay-1.txt has {len(file2_words)} words")
else:
    print("One or both files are missing.")
