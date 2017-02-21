import numpy as np
# assumptions: we have whole training set


def count_pos_reviews(training_mat=np.random.choice([0, 1], size=(3,5), p=[.9, .1])):

    # values
    row_count = training_mat.shape[0]
    column_count = training_mat.shape[1]
    training_mat[0, column_count - 1] = 1
    training_mat[1, column_count - 1] = 1
    num_pos_reviews = sum(training_mat[:, column_count - 1])

    # vectors
    pos_review_vector = training_mat[:, column_count - 1]

    print training_mat
    print row_count
    print column_count
    print num_pos_reviews
    print pos_review_vector



count_pos_reviews()