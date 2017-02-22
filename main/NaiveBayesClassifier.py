import numpy as np
import math
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

# def train(pos_reviews, term_freq_in_doc_vector, doc, label, num_docs, num_unique_terms, num_terms_in_doc):



    # print prob_positive_review


if __name__ == "__main__":
    commander = Commander()
    document_extractor = DocumentExtractor()
    tokenizer = Tokenizer()
    # docs, labels = commander.get_corpus_as_lists('training.txt')
    vocabDict, vocab_set, freq_set = commander.readVocabulary('training.txt')
    vocab_size = len(vocabDict)
    vocab = list(vocab_set)
    count = 0
    trainMat = []
    docs, labels = commander.get_corpus_as_numpy('training.txt')
    # num_docs = corpus.shape[0]
    num_docs = len(docs)
    print num_docs
    positive_reviews = sum(labels)

    prob_positive_review = positive_reviews / float(num_docs)
    freq_positive = np.zeros(vocab_size)
    freq_negative = np.zeros(vocab_size)  # numerators
    prob_positive_given_collection =  2.0
    prob_negative_given_collection =  2.0  # denominators
    count = 0
    for doc, label in zip(docs,labels):
        terms = tokenizer.tokenize_sentence(doc)
        num_terms_in_doc = len(terms)
        term_freq_in_doc_vector = document_extractor.bag_of_words_term_freq_dict(vocabDict, terms)
        # prob = train(positive_reviews, term_freq_in_doc_vector, doc=doc, label=label, num_docs=num_docs, num_unique_terms=vocab_size, num_terms_in_doc=num_terms_in_doc)

        if label == 1:
            freq_positive += term_freq_in_doc_vector
            prob_positive_given_collection += num_terms_in_doc
        else:
            freq_negative += term_freq_in_doc_vector
            prob_negative_given_collection += num_terms_in_doc
    print prob_positive_given_collection
    print prob_positive_given_collection
    prob_pos_vector = np.log((freq_positive + 1) / prob_positive_given_collection)
    prob_neg_vector = np.log((freq_negative + 1)/ prob_negative_given_collection)
    print prob_positive_review, prob_pos_vector, prob_neg_vector
        # return prob_positive_review, prob_pos_vector, prob_neg_vector

        # if count % 100 == 0:
        #     print term_freq_in_doc_vector
        # count += 1