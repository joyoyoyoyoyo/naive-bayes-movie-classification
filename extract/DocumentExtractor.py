import numpy as np
import re

# assumption: we are working with a document
from extract.Tokenizer import Tokenizer


class DocumentExtractor():
    def __init__(self, doc_generator, wordSplit):
        self._generator = doc_generator
        self._tokenizer = Tokenizer()

    def extract_term_counts(self, term, doc):
        tokens = self._tokenizer.tokenize_sentence(doc)
        normalizedTerm = term
        termFrequency = tokens.count(normalizedTerm)
        return term, termFrequency

    def count_terms(self, doc):
        tokens = self._tokenizer.tokenize_sentence(doc)
        return len(tokens)

    def count_unique_terms(self, doc):
        tokens = set(self._tokenizer.tokenize_sentence(doc))
        return len(tokens)

# if __name__ == "__main__":