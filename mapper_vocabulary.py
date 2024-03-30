#!/usr/bin/env python3
import sys
import csv
import re

# Regular expression pattern to tokenize words
word_pattern = re.compile(r'\b\w+\b')

def write_dict_to_file(dictionary, file_path):
    with open(file_path, 'w') as file:
        for key, value in dictionary.items():
            file.write(f"{key}: {value}\n")

# Read input from standard input (stdin)
reader = csv.reader(sys.stdin)
next(reader)
voc = {}
# Iterate over each row in the CSV file
for row in reader:
    if len(row) == 2:
        article_id, section_text = row
        s = section_text.split()
        s = sorted(s)
        voc[article_id] = s

# Write the dictionary data to the file
write_dict_to_file(voc, "vocabulary.txt")

# Print the matching words dictionary
for article_id, words_set in voc.items():
    print(f"{article_id}\t{words_set}")

