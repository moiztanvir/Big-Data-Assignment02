# Document Search Engine built using Apache Hadoop and Vector Space Model

### Group members:
- [Moiz Tanvir](https://github.com/moiztanvir) _(i221932@nu.edu.pk)_
- [Talha Ali](https://github.com/Talha-Ali-5365) _(i221971@nu.edu.pk)_
- [Irtaza Ahmed](https://github.com/irtazajawad) _(i221975@nu.edu.pk)_

## Introduction
In this repository, a Naïve Search Engine is implemented utilizing **MapReduce** technology and **Vector Space Model** following a systematic approach comprising _data preprocessing, indexing, and query processing_. Initially, documents undergo preprocessing. Indexing involves creating an inverted index where terms map to documents containing them, executed through Map and Reduce stages in the MapReduce paradigm. Query processing entails issuing MapReduce jobs to search for documents matching query terms, with Map tasks handling term processing and Reduce tasks aggregating document lists. Ultimately, users receive a ranked list of relevant documents, leveraging the parallel processing capabilities of MapReduce for efficient search across large document collections. 
The dependencies used in the project are as follows:

## Dependencies:
- [Regular Expression](https://docs.python.org/3/library/re.html)
- [CSV](https://docs.python.org/3/library/csv.html)
- [Sys](https://docs.python.org/3/library/sys.html)
- [Itertools](https://docs.python.org/3/library/itertools.html)
- [Pandas](https://pandas.pydata.org/docs/)

## Dataset Used:
We used a portion of the English Wikipedia dump, which is provided in CSV format and can be downloaded at: https://drive.google.com/file/d/1lGVGqzF5CNWaoV-zoz8_mlThvHwMgcsP/view 

## Our Approach:
The following steps were implemented while working on this project:
### 1. Data Cleaning:
Data was read from a CSV file and cleaned to remove any inconsistencies, noise, or irrelevant columns and information. This step ensured that the data was in a suitable format for further processing. Then we collected a sample of data for further processing.

### 2. Vocabulary Separation:
The vocabulary was extracted from the cleaned data. This involved identifying unique terms present in the documents, which would later be used for calculating term frequency and inverse document frequency.

### 3. Term Frequency (TF) Calculation: 
For each document, the **Term Frequency (TF)** was calculated. Term frequency represents the frequency of occurrence of each term within a document. This information was stored in a dictionary, where each key represents a document and its corresponding value is another dictionary containing _term-frequency pairs_.

### 4. Inverse Document Frequency (IDF) Calculation: 
The **Inverse Document Frequency (IDF)** was calculated for each term in the vocabulary. Inverse document frequency measures how rare a term is across all documents. This information was stored in a dictionary, where each term is associated with its IDF value.

### 5. Vector Representation: 
Each document was represented as a vector, where each dimension corresponds to a term in the vocabulary. The value of each dimension is the product of term frequency and inverse document frequency for that term in the document.

### 6. Search Engine Implementation: 
Finally, a search engine was implemented using the Hadoop framework. Given a set of query terms or documents, the search engine retrieves relevant documents based on their similarity to the query. This similarity is calculated using the cosine similarity measure between the query vector and the document vectors.

## References:
- Hadoop Documentation: https://hadoop.apache.org/docs/stable/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html
- Cholissodin, Imam & Seruni, Diajeng & Zulqornain, Junda & Hanafi, Audi & Ghofur, Afwan & Alexander, Mikhael & Hasan, Muhammad. (2020). [Development of Big Data App for Classification based on Map Reduce of Naive Bayes with or without Web and Mobile Interface by RESTful API Using Hadoop and Spark](https://www.researchgate.net/publication/348110835_Development_of_Big_Data_App_for_Classification_based_on_Map_Reduce_of_Naive_Bayes_with_or_without_Web_and_Mobile_Interface_by_RESTful_API_Using_Hadoop_and_Spark). Journal of Information Technology and Computer Science. 
- Vector Space Model: https://towardsdatascience.com/lets-understand-the-vector-space-model-in-machine-learning-by-modelling-cars-b60a8df6684f
