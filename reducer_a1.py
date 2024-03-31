#!/usr/bin/env python3
import sys
import ast

# Initialize variables
tf_representation = {}

def calculate_ratio(set1, set2):
    intersection = len(set1.intersection(set2))
    union = len(set1.union(set2))
    if union == 0:
        return 0
    return intersection / union

def compare_sets(dict_data):
    result = {}
    for key1, sets1 in dict_data.items():
        ratios = []
        for key2, sets2 in dict_data.items():
            if key1 == key2:
                ratios.append(1)  # Same key, so ratio is 1
                continue
            max_ratio = 0
            for s1 in sets1:
                for s2 in sets2:
                    ratio = calculate_ratio(s1, s2)
                    max_ratio = max(max_ratio, ratio)
            ratios.append(max_ratio)
        result[key1] = ratios
    return result

# Read input from standard input (stdin)
for line in sys.stdin:
    # Split the input line into article_id and word_id:frequency
    article_id, word_frequency = line.strip().split('\t')
    # Convert string representation of set to actual set
    tf_representation[article_id] = ast.literal_eval(word_frequency)

# Compare sets after all data has been read
result = compare_sets(tf_representation)

for i, j in result.items():
    print(f"{i}\t{j}")