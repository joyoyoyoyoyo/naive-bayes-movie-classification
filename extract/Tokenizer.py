import re

# from main.Commander import Commander


class Tokenizer():
    def __init__(self):
        self._regex = re.compile('\\W+')

    def tokenize_sentence(self, sentence, min_word_len=0, blacklist=[]):
        tokens = [token.lower() for token in self._regex.split(sentence) if len(token) >= min_word_len
                      and token not in blacklist]
        # tokens = set(tokens)
        #TODO: Test for duplication
        return tokens

    def wordCountInCorpus(self, word, corpus):
        corpus

    def wordCountInDocument(self, word, document):
        document

    def wordCountInClass(self, word, classfication):
        classfication

    def computeProbability(self):
        self
        # if in word, use values
        # else, perform laplace smoothing
        # test case (Not zero)

    def bigramCount(self, term_phrase, corpus):
        self # feature

    def sentenceLength(self):
        self # feature, attribute

    def numberOfSentences(self):
        self # stemming

    def numberOfPunctuation(self):
        self # potential feature

    def laplace_smoothing(self):
        self # smooth

    def porterStemming(self, uniqWords):
        self

    def wordCountInCorpusRegEx(self, word, regex_normalize):
        word

    def wordCountInDocumentRegex(self, document, regex_normalize):
        document

# if __name__ == "__main__":
    # commander = Commander()
    # freqVec, vocabVec = commander.readVocabulary('training.txt')
    # tokenizer = Tokenizer()
    # tokens = tokenizer.tokenize_sentence('Hello, my name is Paul')
    # test = tokens | {'hgdfey'}
    # word_vec = [0] * commander.vocabSize
    # sentence_vec = [0] * len(tokens)
    # print sentence_vec

# set([token.lower()
#      for token in re.findall('\w+', text)
#      if min_len <= len(token) <= max_len and
#      token not in kw['ignore_list']])
# def vectorizeSentence(self, sentence):
