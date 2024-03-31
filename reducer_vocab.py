#!/usr/bin/env python3
import sys

# Initialize a set to store the vocabulary
vocabulary = set()

# Read input from standard input (stdin)
for line in sys.stdin:
    # Split the input line into word and document_id
    word, document_id = line.strip().split('\t')
    # Add the word to the vocabulary
    vocabulary.add(word)

# Print the vocabulary
for word in vocabulary:
    print(word)