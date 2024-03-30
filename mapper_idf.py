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

# Initialize a dictionary to store the term frequency for each ARTICLE_ID

idf_ratio = {}
# Read input from standard input (stdin)
reader = csv.reader(sys.stdin)
next(reader)
voc = []
voc2 = []
# Iterate over each row in the CSV file
for row in reader:
    if len(row) == 2:
        article_id, section_text = row
        s = section_text.split()
        s = sorted(s)
        for word in s:
            if word not in voc:
                voc.append(word)
            voc2.append(word)
        m2 = []
        for word in s:
            if s.count(word)>1:
                if word not in m2:
                    if len(m2)>0 and m2[len(m2)-2]!=m2[len(m2)-1]:
                        temp1 = [int(voc.index(word)), (int(s.count(word))/voc2.count(word))]
                        if m2.count(m2[len(m2)-1]) > 1:
                            m2.pop()
                        m2.append(temp1) 
            else:
                temp1 = [int(voc.index(word)), (int(s.count(word))/voc2.count(word))]
                m2.append(temp1)
        idf_ratio[article_id] = m2

# Write the dictionary data to the file
write_dict_to_file(idf_ratio, "idf_ratio.txt")

# Print the matching words dictionary
for article_id, words_set in idf_ratio.items():
    print(f"{article_id}\t{words_set}")

