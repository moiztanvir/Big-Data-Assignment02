#!/usr/bin/env python3
import sys
import math

# Initialize a dictionary to store the document frequency for each word
document_frequency = {}

# Read input from standard input (stdin)
for line in sys.stdin:
    # Split the input line into word and count
    word, count = line.strip().split('\t')
    # Increment the document frequency for this word
    document_frequency[word] = document_frequency.get(word, 0) + 1

# Calculate the total number of documents
total_documents = len(document_frequency)

# Calculate and print the IDF for each word
for word, freq in document_frequency.items():
    idf = math.log(total_documents / freq)
    print(f'{word}\t{idf}')