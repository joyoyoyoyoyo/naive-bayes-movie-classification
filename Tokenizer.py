import re


class Tokenizer():
    def __init__(self):
        self._regex = re.compile('\\W+')

    def tokenize_sentence(self, sentence, min_word_len=0, blacklist=[]):
        tokens = set([token.lower() for token in self._regex.split(sentence) if len(token) >= min_word_len
                      and token not in blacklist])
        return tokens

if __name__ == "__main__":
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize_sentence('Hello, my name is Paul')
    test = tokens | {'hgdfey'}
    print test

# set([token.lower()
#      for token in re.findall('\w+', text)
#      if min_len <= len(token) <= max_len and
#      token not in kw['ignore_list']])
# def vectorizeSentence(self, sentence):
