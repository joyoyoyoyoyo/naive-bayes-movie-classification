import numpy as np
import math
import sys
import timeit

startTesting = timeit.default_timer()
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
    files = sys.argv[1:]
    trainingFileName = sys.argv[1]
    testingFileName = sys.argv[2]

    # docs, labels = commander.get_corpus_as_lists('training.txt')
    vocab, freq = commander.readVocabulary(trainingFileName, testingFileName)
    trainMat = []
    labels, doc_vectors = commander.get_corpus_as_numpy(vocab, freq, trainingFileName)
    prob_positive_review = commander.pos_review_count / float(commander.doc_count)
    term_freq_in_positive_reviews = np.ones(commander.vocab_size)
    term_freq_in_negative_reviews = np.ones(commander.vocab_size)  # numerators
    total_word_count_in_negative_reviews = 2.0  # avoid divide by 0 & 1
    total_word_count_in_positive_reviews = 2.0  # denominators
    count = 0

    # Train
    startTraining = timeit.default_timer()
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
    prob_pos_vector = np.log(term_freq_in_positive_reviews / total_word_count_in_positive_reviews)
    prob_neg_vector = np.log(term_freq_in_negative_reviews / total_word_count_in_negative_reviews)
    stopTraining = timeit.default_timer()


    training_labels, training_doc_vectors = commander.get_test_corpus_as_numpy(vocab, trainingFileName)

    # Classify training set
    correctTraining = 0
    total_train_docs = 0
    startLabeling = timeit.default_timer()
    for training_label, training_doc_vec in zip(training_labels, training_doc_vectors):
        classified = commander.classify(training_doc_vec, prob_pos_vector, prob_neg_vector,prob_positive_review)
        if training_label is classified:
            correctTraining += 1
        total_train_docs += 1
        # print classified
    stopLabeling = timeit.default_timer()


    testing_labels, testing_doc_vectors = commander.get_test_corpus_as_numpy(vocab, testingFileName)

    # classify the testing docs
    correctTesting = 0
    total_testing_docs = 0
    startTesting = timeit.default_timer()
    for testing_label, test_doc_vec in zip(testing_labels, testing_doc_vectors):
        classified = commander.classify(test_doc_vec, prob_pos_vector, prob_neg_vector,prob_positive_review)
        if testing_label is classified:
            correctTesting += 1
        total_testing_docs += 1
        print classified

    stopTesting = timeit.default_timer()
    print str(stopTraining - startTraining) + " seconds (training)"
    print str(stopTesting - startLabeling) + " seconds (labeling)"
    print str(correctTraining/float(total_train_docs)) + " (training)"
    print str(correctTesting/float(total_testing_docs)) + " (testing)"
