import subprocess
import csv
import numpy as np
from functools import reduce

# import shlex # args = shlex.split(command)
# https://docs.python.org/2/tutorial/datastructures.html
# https://docs.python.org/2/library/subprocess.html
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html
from extract.Tokenizer import Tokenizer


class Commander():

    def __init__(self):
        self.vocab_size = 0
        self.doc_count = 0
        self.pos_review_count = 0
        self.neg_review_count = 0
        self._tokenizer = Tokenizer()

    # Training data vocabulary size: 35918
    # Testing  data vocabulary size: 11123
    def readVocabulary(self, filename, pathDirectory='../resources/'):
        command = "tr 'A-Z' 'a-z' < " + pathDirectory + filename + " | " + "tr -sc 'A-Za-z' '\\n' | sort | uniq -c | sort -n -r"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        retcode = proc.poll()
        freq_list = []
        vocab_list = []
        # dictVocabFreq = {}
        for line in iter(proc.stdout.readline, b''):
            frequencyCount, word = line.decode('utf-8').split()
            freq_list.append(int(str(frequencyCount)))
            vocab_list.append(str(word))
        proc.stdout.close()
        proc.stdin.close()
        self.vocab_size = len(vocab_list)
        return vocab_list, freq_list
        # return np.array(freqMat), np.array(vocabMat)
        # vocabFreqMat = np.column_stack((vocabMat, freqMat))
        # num_docs = corpus.shape[0]
        # return vocabFreqMat

    def getDocumentsYield(self, vocab, freq, filename, pathDirectory='../resources/'):
        self.doc_count = 0

        with open(pathDirectory + filename, 'rb') as csvfile:
            moviereader = csv.reader(csvfile, delimiter='\t')
            for row in moviereader:
                self.doc_count += 1
                if int(row[-1]) is 1:
                    self.pos_review_count += 1
                else:
                    self.neg_review_count += 1
                tokens = self._tokenizer.tokenize_sentence(row[0])
                doc_vector = [0] * self.vocab_size
                for term in tokens:
                    if term in vocab:
                        index = vocab.index(term)
                        doc_vector[index] += 1
                        # term_frequency = freq[index]
                        # doc_vector[vocab.index(term)] = term_frequency
                # if word in vocabList:
                #     returnVec[vocabList.index(word)] = 1
                yield (row[0], int(row[-1]), doc_vector)
        csvfile.close()

    def get_corpus_as_lists(self, vocab, freq, filename, path_directory='../resources/'):
        labels = []
        docs = []
        doc_vectors = []
        for doc, label, doc_vector in self.getDocumentsYield(vocab, freq, filename, path_directory):
            docs.append(doc)
            labels.append(label)
            doc_vectors.append(doc_vector)
        return docs, labels, doc_vectors

    def get_corpus_as_numpy(self, vocab, freq, filename, path_directory='../resources/'):
        docs = []
        labels = []
        doc_vectors = []
        for doc, label, doc_vector in self.getDocumentsYield(vocab, freq, filename,path_directory):
            docs.append(doc)  # doc is a string doc
            labels.append(label)  # label is an int (1 or 0)
            doc_vectors.append(doc_vector)

        # docs = np.array(docs)
        # labels = np.array(labels)
        # corpus = np.empty(shape=(docs.))
        # docs, labels = np.array(docs), np.array(labels)
        return docs, labels, doc_vectors
        # corpus = np.column_stack((docs, labels))
        # return corpus

    # def init_vocabulary_from_corpus(self, filename, path_directory='../resources/'):
    #     vocab_freq_mat = self.readVocabulary(filename, path_directory)
    #     print len(vocab_freq_mat)
    #     print len(vocab_freq_mat[:,0])
    #
    #     # >> np.union1d([-1, 0, 1], [-2, 0, 2])
    #     union = reduce(np.union1d, (vocab_freq_mat[:,0], ['zzzzzzzzzzzzzz']))
    #     print len(union)
    #     # print len(union[:,0]) # potential bug
    #     print union.size
    #     print union[union.size-1][0]
    #     # print len(union[:,0])
    #     return union

            # did not work
    #   try this
    #
    #   for doc, label in commander.getDocumentsYield('training.txt'):
    #       print label + ":\t\t" + doc
    #
    # def get_corpus_as_numpy(self, filename, path_directory='../resources/'):
    #     corpus = np.genfromtxt(path_directory + filename,
    #                            dtype=[('mystr', 'S5'), ('myint', 'i8')],
    #                            usecols=np.arange(0, 1),
    #                            delimiter='\t')
    #     return corpus


if __name__ == "__main__":
    commander = Commander()
    # freqVec, vocabVec = commander.readVocabulary('training.txt')
    posReview = 0
    negReview = 0
    reviewCount = 0

    # or use unix
    # 'wc -l resources/training.txt'                # of each doc
    # 'grep -i word resources/training.txt | wc -l' # term freq count in each doc
    for doc, label in commander.getDocumentsYield('training.txt'):
        reviewCount += 1
        if label is 1:
            posReview += 1
        else:
            negReview += 1
        # print label + ":\t\t" + doc
        # print label
    print("Positive Reviews\t" + str(posReview))
    print("Negative Reviews\t" + str(negReview))
    print("TotalNum Reviews\t" + str(reviewCount))
    # def tokenizeSentence(self, sentence):


