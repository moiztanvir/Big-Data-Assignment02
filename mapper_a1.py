#!/usr/bin/env python3
import sys
import csv
import re

# Regular expression pattern to tokenize words
word_pattern = re.compile(r'\b\w+\b')

# Initialize a dictionary to store the term frequency for each ARTICLE_ID
t2 = {}
# Read input from standard input (stdin)
reader = csv.reader(sys.stdin)
next(reader)
t = []
# Iterate over each row in the CSV file
for row in reader:
    if len(row) == 2:
        article_id, section_text = row
        m = set() 
        s = section_text.split()
        s = sorted(s)
        for word in s:
            if word not in t:
                t.append(word)
        for word in s:
            if s.count(word)>1:
                if word not in m:
                    m.add((t.index(word), s.count(word)))
            else:
                m.add((t.index(word), 1))
        t2[article_id] = m


# Print the matching words dictionary
for article_id, words_set in t2.items():
    print(f"{article_id}\t{words_set}")

