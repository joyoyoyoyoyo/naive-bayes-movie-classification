import numpy as np

def collect_training_data_mat(cardinality_vocab, cardinality_features):
    train_mat = np.zeros((cardinality_vocab, cardinality_features))
    return train_mat

def collect_prediction_vector(cardinality_documents, cardinality_classes):
    train_prediction_vector = np.zeros((cardinality_documents, cardinality_classes))
    return train_prediction_vector

def probability_document_is_a_positive_review(training_classification_vector, cardinality_training_documents):
    # probability of a positive review is:
    #       the sum of a positive reviews in the total number of training documents / (dividedBy) the total number of training documents
    p_positive_review = sum(training_classification_vector)/float(cardinality_training_documents)
    p_positive_vocab = np.zeros(len(cardinality_vocab))

def frequency_addition_bag_of_words(bag_of_words_vector):
    [0,1,1,...,0] # v0
    [1,1,0,...,1] # v1
    [1,2,1,...,2] # sum(v0,v1)