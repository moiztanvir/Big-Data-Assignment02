#!/usr/bin/env python3
import sys
import csv
import re

# Regular expression pattern to tokenize words
word_pattern = re.compile(r'\b\w+\b')

# Initialize a dictionary to store the term frequency for each ARTICLE_ID
term_frequency = {}
t2 = {}
# Read input from standard input (stdin)
reader = csv.reader(sys.stdin)
i = 0
j = 0
next(reader)

# Iterate over each row in the CSV file
for row in reader:
    if len(row) == 2:
        article_id, section_text = row
        m = set() 
        s = section_text.split()
        s = sorted(s)
        for word in s:
            if s.count(word)>1:
                if word not in m:
                    m.add((i, s.count(word)))
            else:
                term_frequency[i] = word
                m.add((i, 1))
                i = i+1
        t2[article_id] = m


# Print the matching words dictionary
for article_id, words_set in t2.items():
    print(f"{article_id}\t{words_set}")

