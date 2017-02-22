import numpy
# Steps for Tokenization

# Matrix representation

# Frequency Count

# Document Frequency

# word vector

# corpus vector

# Naive Bayes Probability
from extract.DocumentExtractor import DocumentExtractor
from extract.Tokenizer import Tokenizer
from main.Commander import Commander

if __name__ == "__main__":
    commander = Commander()
    document_extractor = DocumentExtractor()
    tokenizer = Tokenizer()
    docs, labels = commander.get_corpus_as_lists('training.txt')
    vocabDict = commander.readVocabulary('training.txt')
    count = 0
    for doc in docs:
        terms = tokenizer.tokenize_sentence(doc)
        term_freq_in_doc_vector = document_extractor.bag_of_words_term_freq_dict(vocabDict,terms)
        # if count % 100 == 0:
        #     print term_freq_in_doc_vector
        count += 1