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
    vocab, freq = commander.readVocabulary('training.txt')
    trainMat = []
    labels, doc_vectors = commander.get_corpus_as_numpy(vocab, freq, 'training.txt')
    prob_positive_review = commander.pos_review_count / float(commander.doc_count)
    term_freq_in_positive_reviews = np.ones(commander.vocab_size)
    term_freq_in_negative_reviews = np.ones(commander.vocab_size)  # numerators
    total_word_count_in_negative_reviews = 2.0  # avoid divide by 0 & 1
    total_word_count_in_positive_reviews = 2.0  # denominators
    count = 0
    for label, doc_vector in zip(labels, doc_vectors):
        doc_vec_as_array = np.array(doc_vector)
        doc_word_count = sum(doc_vec_as_array)
        if label is 1:
            term_freq_in_positive_reviews += doc_vec_as_array
            total_word_count_in_positive_reviews += doc_word_count
        else:
            term_freq_in_negative_reviews += doc_vec_as_array
            total_word_count_in_negative_reviews += doc_word_count
        count += 1
        print count
    prob_pos_vector = np.log(term_freq_in_positive_reviews / total_word_count_in_positive_reviews)
    prob_neg_vector = np.log(term_freq_in_negative_reviews / total_word_count_in_negative_reviews)

    testing_labels, testing_doc_vectors = commander.get_test_corpus_as_numpy(vocab, 'testing.txt')
    correct = 0
    wrong = 0
    total_test_docs = 0
    for testing_label, test_doc_vec in zip(testing_labels, testing_doc_vectors):
        classified = commander.classify(test_doc_vec, prob_pos_vector, prob_neg_vector,prob_positive_review)
        if testing_label is classified:
            correct += 1
        else:
            wrong += 1
        total_test_docs += 1

        if total_test_docs % 100 == 0:
            print correct/float(total_test_docs)
    print correct/float(total_test_docs)

    # prob_neg_vector = np.log((freq_negative + 1)print/ prob_negative_given_collection)
    # print prob_positive_review, prob_pos_vector, prob_neg_vector
        # return prob_positive_review, prob_pos_vector, prob_neg_vector

        # if count % 100 == 0:
        #     print term_freq_in_doc_vector
        # count += 1