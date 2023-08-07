# Week 16: Dependency Parsing Algorithms and Libraries
Dependency parsing is a task in Natural Language Processing (NLP) that involves analyzing the grammatical structure of a sentence based on the dependencies between its words. Each word (or token) in the sentence is linked to another, indicating their grammatical relationship and the role they play in the sentence. The result of dependency parsing is typically a dependency tree or graph, where nodes represent the words, and the directed edges represent the grammatical relations.

Dependency Parsing Algorithms
There are several algorithms used for dependency parsing, each with its own strengths and limitations:

Transition-Based Parsing (Shift-Reduce Parsing): In this approach, the parsing process is viewed as a series of transitions, or operations, that transform the input sentence into its correct parse tree. The parse tree is built incrementally, and decisions are made greedily at each step based on a classifier.

Graph-Based Parsing: Graph-based algorithms treat dependency parsing as a graph problem, where the goal is to find the optimal tree in a graph that represents all possible parse trees. The optimal tree is typically defined as the tree that maximizes the sum of the scores of its edges.

Eisner's Algorithm: Eisner's algorithm is a specific graph-based parsing algorithm for projective dependencies. It's efficient and guarantees to find the optimal projective parse tree.

Libraries for Dependency Parsing
Several libraries and tools provide functionality for dependency parsing:

SpaCy: SpaCy is an open-source library for NLP in Python. It provides dependency parsing out of the box and is known for its speed and accuracy.

Stanford NLP: The Stanford NLP Group's software provides robust implementations of various NLP tasks, including dependency parsing. It supports several languages and provides both transition-based and graph-based parsers.

NLTK (Natural Language Toolkit): NLTK is a leading platform for building Python programs to work with human language data. It provides interfaces to over 50 corpora and lexical resources and includes packages for different NLP tasks, including dependency parsing.

SyntaxNet: Developed by Google, SyntaxNet is a neural network framework for TensorFlow that provides a foundation for building machine learning models that can understand the semantic structure of sentences, including dependency parsing. Its pre-trained model for English, Parsey McParseface, is known for its high accuracy.

# Readings

[Dependency parsing](https://citeseerx.ist.psu.edu/document?repid=rep1&type=pdf&doi=6d2960b5818e4df0c61ba390f70ecf962079e165)

[A survey of unsupervised dependency parsing](https://arxiv.org/pdf/2010.01535.pdf)

[Sentiment analysis via dependency parsing](https://d1wqtxts1xzle7.cloudfront.net/31306204/elsarticle-template-harv-libre.pdf?1392389550=&response-content-disposition=inline%3B+filename%3DSentiment_analysis_via_dependency_parsin.pdf&Expires=1691428166&Signature=IxwsSXchapLzSkygUG~MJ07A5TWrt-T-a9A4XcGhvX24Jw624IeXI16d2vZmwmnmyUS0dC0jSh6-oGw4j7Lilh5a2i8dmXoOMdJhB3qyJ4hnWIsF~GIOviruk6bVWRSEHwmsLboqFEj~V4xaKulYvfIGdDCVyqRZOKjlLJ-K286a8aAMxvT-VGp-BhLwpZfom~9pdIPGgmaH~norOjTCPtGY~~tKH6-bL~Aujk3AFtG9AYcpKOft6Fc6tb5QVB3pXKK29Op-dXeDr-xY29mPNqCY~GKN2asBcVFs-rrZermgPQHQV-bACXGakJKo29BkHy5Pd5xOEGZPb9ADRYuHPQ__&Key-Pair-Id=APKAJLOHF5GGSLRBV4ZA)


# Code example

Importing Required Libraries:
The code begins by importing the necessary libraries. We import spacy, the library used for natural language processing tasks, and specifically load the download function from the spacy.cli module, which allows us to download language models.

Downloading the Language Model:
The code defines a function named download_language_model. This function attempts to load the en_core_web_sm language model for English language processing using spacy.load('en_core_web_sm'). If the model is not found (indicated by an OSError), it means the model is not installed on the system. In such a case, the function proceeds to download the en_core_web_sm model using the download('en_core_web_sm') function from the spacy.cli module. After downloading, the function loads the language model and returns the nlp object, which will be used for processing the text.

Dependency Parsing Function:
Next, we define a function called dependency_parsing(text). This function takes an input sentence text and performs dependency parsing on it. It first calls the download_language_model() function to ensure that the required language model is available for processing.

Performing Dependency Parsing:
Inside the dependency_parsing function, we use the nlp object to parse the input text. The nlp object processes the sentence and provides a parsed doc object containing the linguistic analysis.

Displaying Dependency Relationships:
The code then iterates through each word (or token) in the parsed doc object and prints the dependency relationships. For each token, it shows the word itself, the dependency label (e.g., 'nsubj', 'prep', 'dobj'), and the word that governs or governs over the current word (head). This represents the grammatical structure and dependency relationships between the words in the sentence.

Example Sentence:
The code includes an example sentence: "The quick brown fox jumps over the lazy dog."

Running the Example:
Finally, the code calls the dependency_parsing function with the example sentence to demonstrate dependency parsing on this input. The code automatically downloads the required language model if it's not already installed on the system.