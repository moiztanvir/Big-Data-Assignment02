# Big-Data-Assignment02

###Group members:
Moiz Tanvir
Talha Ali
Irtaza Ahmed

##Introduction
In this repository, a Naïve Search Engine is implemented utilizing MapReduce technology. The process involved the following steps steps:

##Data Cleaning:
Data was read from a CSV file and cleaned to remove any inconsistencies, noise, or irrelevant columns and information. This step ensured that the data was in a suitable format for further processing. Then we collected a sample of data for further processing.

##Vocabulary Separation:
The vocabulary was extracted from the cleaned data. This involved identifying unique terms present in the documents, which would later be used for calculating term frequency and inverse document frequency.

##Term Frequency (TF) Calculation: 
For each document, the term frequency was calculated. Term frequency represents the frequency of occurrence of each term within a document. This information was stored in a dictionary, where each key represents a document and its corresponding value is another dictionary containing term-frequency pairs.

##Inverse Document Frequency (IDF) Calculation: 
The inverse document frequency was calculated for each term in the vocabulary. Inverse document frequency measures how rare a term is across all documents. This information was stored in a dictionary, where each term is associated with its IDF value.

##Vector Representation: 
Each document was represented as a vector, where each dimension corresponds to a term in the vocabulary. The value of each dimension is the product of term frequency and inverse document frequency for that term in the document.

##Search Engine Implementation: 
Finally, a search engine was implemented using the Hadoop framework. Given a set of query terms or documents, the search engine retrieves relevant documents based on their similarity to the query. This similarity is calculated using the cosine similarity measure between the query vector and the document vectors.

Overall, this project demonstrates the application of MapReduce technology in building a search engine capable of efficiently retrieving relevant documents from a large corpus based on user queries. By leveraging the TF-IDF representation and cosine similarity measure, the search engine provides accurate and efficient document retrieval functionality.
