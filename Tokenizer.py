import re

from Commander import Commander


class Tokenizer():
    def __init__(self):
        self._regex = re.compile('\\W+')

    def tokenize_sentence(self, sentence, min_word_len=0, blacklist=[]):
        tokens = set([token.lower() for token in self._regex.split(sentence) if len(token) >= min_word_len
                      and token not in blacklist])
        return tokens

    def wordCountInCorpus(self, word):
        word

    def wordCountInDocument(self, document):
        document

if __name__ == "__main__":
    commander = Commander()
    freqVec, vocabVec = commander.readVocabulary('training.txt')
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize_sentence('Hello, my name is Paul')
    test = tokens | {'hgdfey'}
    word_vec = [0] * commander.vocabSize
    sentence_vec = [0] * len(tokens)
    print sentence_vec

# set([token.lower()
#      for token in re.findall('\w+', text)
#      if min_len <= len(token) <= max_len and
#      token not in kw['ignore_list']])
# def vectorizeSentence(self, sentence):
