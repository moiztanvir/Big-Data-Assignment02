#!/usr/bin/env python3
import sys

# Initialize variables
current_article_id = None
result = {}

# Read input from standard input (stdin)
for line in sys.stdin:
    # Split the input line into article_id and word_id:frequency
    article_id, word_frequency = line.strip().split('\t')
    result[article_id] = word_frequency

for i, j in result.items():
    print(f"{i}\t{j}")
