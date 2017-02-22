import subprocess
import csv
import numpy as np
from functools import reduce

# import shlex # args = shlex.split(command)
# https://docs.python.org/2/tutorial/datastructures.html
# https://docs.python.org/2/library/subprocess.html
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.genfromtxt.html
# https://docs.scipy.org/doc/numpy/reference/generated/numpy.loadtxt.html

class Commander():

    def __init__(self):
        vocabSize = 0

    # Training data vocabulary size: 35918
    # Testing  data vocabulary size: 11123
    def readVocabulary(self, filename, pathDirectory='../resources/'):
        command = "tr 'A-Z' 'a-z' < " + pathDirectory + filename + " | " + "tr -sc 'A-Za-z' '\\n' | sort | uniq -c | sort -n -r"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        retcode = proc.poll()
        freqSet = set([])
        vocabSet = set([])
        dictVocabFreq = {}
        for line in iter(proc.stdout.readline, b''):
            frequencyCount, word = line.decode('utf-8').split()
            freqSet.add(frequencyCount)
            vocabSet.add(word)
            dictVocabFreq[word] = frequencyCount
        proc.stdout.close()
        proc.stdin.close()
        self.vocabSize = len(vocabSet)
        return dictVocabFreq
        # return freqSet, vocabSet, dictVocabFreq
        # return np.array(freqMat), np.array(vocabMat)
        # vocabFreqMat = np.column_stack((vocabMat, freqMat))
        # return vocabFreqMat

    def getDocumentsYield(self, filename, pathDirectory='../resources/'):
        with open(pathDirectory + filename, 'rb') as csvfile:
            moviereader = csv.reader(csvfile, delimiter='\t')
            for row in moviereader:
                yield (row[0], row[1])

    def get_corpus_as_numpy(self, filename, path_directory='../resources/'):
        docs = []
        labels = []
        for doc, label in self.getDocumentsYield(filename,path_directory):
            docs.append(doc)
            labels.append(label)

        # return (docs, labels)
        corpus = np.column_stack((docs, labels))
        return corpus

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
    freqVec, vocabVec = commander.readVocabulary('training.txt')
    for doc, label in commander.getDocumentsYield('training.txt'):
        print label + ":\t\t" + doc
        # print label
    # print(freqVec)
    # print(vocabVec)

    # def tokenizeSentence(self, sentence):


