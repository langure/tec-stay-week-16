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
