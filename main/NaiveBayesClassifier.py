import numpy as np
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

def train(pos_reviews, doc, label, num_docs, num_unique_terms):
    prob_positive_review = pos_reviews/float(num_docs)
    print prob_positive_review


if __name__ == "__main__":
    commander = Commander()
    document_extractor = DocumentExtractor()
    tokenizer = Tokenizer()
    # docs, labels = commander.get_corpus_as_lists('training.txt')
    vocabDict = commander.readVocabulary('training.txt')
    vocab_size = len(vocabDict)
    count = 0
    trainMat = []
    docs, labels = commander.get_corpus_as_numpy('training.txt')
    # num_docs = corpus.shape[0]
    num_docs = len(docs)
    print num_docs
    positive_reviews = sum(labels)
    for doc, label in zip(docs,labels):
        terms = tokenizer.tokenize_sentence(doc)
        term_freq_in_doc_vector = document_extractor.bag_of_words_term_freq_dict(vocabDict,terms)
        prob = train(positive_reviews, doc=doc, label=label, num_docs=num_docs, num_unique_terms=vocab_size)
        # if count % 100 == 0:
        #     print term_freq_in_doc_vector
        # count += 1