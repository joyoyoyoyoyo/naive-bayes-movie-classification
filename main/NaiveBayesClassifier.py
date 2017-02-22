import numpy
# Steps for Tokenization

# Matrix representation

# Frequency Count

# Document Frequency

# word vector

# corpus vector

# Naive Bayes Probability

from main.Commander import Commander

if __name__ == "__main__":
    commander = Commander()
    docs, labels = commander.get_corpus_as_lists('training.txt')
    vocabDict = commander.readVocabulary('training.txt')
