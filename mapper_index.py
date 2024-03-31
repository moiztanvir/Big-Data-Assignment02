#!/usr/bin/env python3
import sys
import csv

def read_dict_from_file(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into key-value pairs
            key, value = line.strip().split(":")
            data[key.strip()] = value.strip()
    return data


# Read the dictionary data from the file
voc = read_dict_from_file("vocabulary.txt")
#tf = read_dict_from_file("tf.txt")
#idf = read_dict_from_file("idf_ratio.txt")
#vector = read_dict_from_file("vectors.txt")
query = []

for line in sys.stdin:
    query = line.split()

#query = query.split()
result = {}
j = 0
for x, y in voc.items():
    i = 0
    if j==10:
        break
    for words in query:
        if words in y:
             i = i+1
    if i>=(len(query)/2):
        result[x] = y
        j = j+1
        continue

for x, y in result.items():
    print(f"{x}\t{y}")
