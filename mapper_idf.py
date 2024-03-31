#!/usr/bin/env python3
import sys

# Read input from standard input (stdin)
for line in sys.stdin:
    # Split the line into words
    words = line.strip().split()
    # Emit each word and the document ID (in this case, the line number)
    for word in words:
        print(f'{word}\t1')