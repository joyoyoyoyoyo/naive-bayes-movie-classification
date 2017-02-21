import numpy as np

def collect_training_data_mat(cardinality_vocab, cardinality_features):
    train_mat = np.zeros((cardinality_vocab, cardinality_features))
    return train_mat

def collect_prediction_vector(cardinality_documents, cardinality_classes):
    train_prediction_vector = np.zeros((cardinality_documents, cardinality_classes))
    return train_prediction_vector

