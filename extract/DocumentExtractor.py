import numpy as np
import re

# assumption: we are working with a document
class DocumentExtractor():
    def __init__(self, doc_generator, wordSplit):
        self._generator = doc_generator
        self._tokenizer = Tokenizer()

    def extract_term_counts(self, term, doc, min_word_len=0, blacklist=[]):
        tokens = set([token.lower() for token in self._regex.split(doc) if len(token) >= min_word_len
                      and token not in blacklist])
        return tokens

# if __name__ == "__main__":