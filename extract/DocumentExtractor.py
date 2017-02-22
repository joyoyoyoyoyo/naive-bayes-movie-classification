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
        return termFrequency

# if __name__ == "__main__":