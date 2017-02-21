import re


class Tokenizer():
    def __init__(self):
        self._regex = re.compile('\\W+')

    def tokenize_sentence(self, sentence, min_word_len, blacklist=[]):
        tokens = set([token.lower() for token in self._regex.split(sentence) if len(token) >= min_word_len
                      and token not in blacklist])


# set([token.lower()
#      for token in re.findall('\w+', text)
#      if min_len <= len(token) <= max_len and
#      token not in kw['ignore_list']])
# def vectorizeSentence(self, sentence):
