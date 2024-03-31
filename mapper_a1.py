#!/usr/bin/env python3
import sys
import csv
from collections import defaultdict

# Initialize a dictionary to store the term frequency for each ARTICLE_ID
term_frequency = defaultdict(set)

# Read input from standard input (stdin)
reader = csv.reader(sys.stdin)
next(reader)  # Skip the header

# Iterate over each row in the CSV file
for row in reader:
    if len(row) == 2:
        article_id, section_text = row
        word_counts = defaultdict(int)
        for word in section_text.split():
            word_counts[word] += 1
        for word, count in word_counts.items():
            term_frequency[article_id].add((word, count))

# Print the matching words dictionary
for article_id, words_set in term_frequency.items():
    print(f"{article_id}\t{words_set}")