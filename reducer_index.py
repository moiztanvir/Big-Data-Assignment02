#!/usr/bin/env python3
import sys

def write_dict_to_file(dictionary, file_path):
    with open(file_path, 'w') as file:
        for key, value in dictionary.items():
            file.write(f"{key}: {value}\n")

def read_dict_from_file(file_path):
    data = {}
    with open(file_path, 'r') as file:
        for line in file:
            # Split each line into key-value pairs
            key, value = line.strip().split(":")
            data[key] = value
    return data

vec = read_dict_from_file("vectors.txt")
vec2 = {}
# Initialize variables
tf = {}

# Read input from standard input (stdin)
for line in sys.stdin:
    # Split the input line into article_id and word_id:frequency
    article_id, word_frequency = line.strip().split('\t')
    tf[article_id] = word_frequency
    sum = 0
    for i in vec[article_id]:
        if i not in [' ', '0', ',', '[', ']', '.']:
            sum = sum + int(i)/3
#            print(i)
    vec2[article_id] = sum/10

write_dict_to_file(tf, "final_vocabulary.txt")
write_dict_to_file(vec2, "final_vectors.txt")

print("Relevant Documents")
for i, j in tf.items():
    print(f"{i}\t{j}")
    print(f"{i}\t", vec[i])

print("Relevant document vectors similarity result")
for i, j in vec2.items():
    print(f"{i}\t{j}")
