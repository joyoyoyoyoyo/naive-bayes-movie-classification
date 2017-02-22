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

# def train(doc, label, num_docs, num_unique_terms):



if __name__ == "__main__":
    commander = Commander()
    document_extractor = DocumentExtractor()
    tokenizer = Tokenizer()
    # docs, labels = commander.get_corpus_as_lists('training.txt')
    vocabDict = commander.readVocabulary('training.txt')
    vocab_size = len(vocabDict)
    count = 0
    trainMat = []
    corpus = commander.get_corpus_as_numpy('training.txt')
    num_docs = corpus.shape[0]
    print num_docs
    for row in corpus:
        terms = tokenizer.tokenize_sentence(row[0])
        term_freq_in_doc_vector = document_extractor.bag_of_words_term_freq_dict(vocabDict,terms)
        # prob = train(doc=row[0], label=row[1], num_docs=num_docs, num_unique_terms=vocab_size)
        # if count % 100 == 0:
        #     print term_freq_in_doc_vector
        # count += 1