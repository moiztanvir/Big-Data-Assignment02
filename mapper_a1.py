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
t2 = {}
# Read input from standard input (stdin)
reader = csv.reader(sys.stdin)
next(reader)
voc = []
vec = {}
for row in reader:
    if len(row) == 2:
        article_id, section_text = row
        m = []
        s = section_text.split()
        s = sorted(s)
        for word in s:
            if word not in voc:
                voc.append(word)
        m1 = []
        for i in range(len(voc)):
            m1.append(0)
        for word in s:
            if s.count(word)>1:
                if word not in m:
                    temp = [int(voc.index(word)), (int(s.count(word)))]
                    m1[int(voc.index(word))] = int(s.count(word))/2
                    m.append(temp)
                    if m.count(m[len(m)-1]) > 1:
                        m.pop()
            else:
                temp = [int(voc.index(word)), 1]
                m1[int(voc.index(word))] = int(s.count(word))/2
                m1[int(voc.index(word))] = int(s.count(word))
                m.append(temp)
        vec[article_id] = m1
        t2[article_id] = m

# Write the dictionary data to the file
write_dict_to_file(vec, "vectors.txt")
write_dict_to_file(t2, "tf.txt")

# Print the matching words dictionary
for article_id, words_set in t2.items():
    print(f"{article_id}\t{words_set}")

