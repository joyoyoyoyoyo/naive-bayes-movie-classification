import subprocess
import csv
import numpy as np
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
    def readVocabulary(self, filename, pathDirectory='./resources/'):
        command = "tr 'A-Z' 'a-z' < " + pathDirectory + filename + " | " + "tr -sc 'A-Za-z' '\\n' | sort | uniq -c | sort -n -r"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        retcode = proc.poll()
        freqMat = []
        vocabMat = []
        for line in iter(proc.stdout.readline, b''):
            frequencyCount, word = line.decode('utf-8').split()
            freqMat.append(frequencyCount)
            vocabMat.append(word)
        proc.stdout.close()
        proc.stdin.close()
        self.vocabSize = len(vocabMat)
        return np.array(freqMat), np.array(vocabMat)

    def getDocuments(self, filename, pathDirectory='./resources/'):
        with open(pathDirectory + filename, 'rb') as csvfile:
            moviereader = csv.reader(csvfile, delimiter='\t')
            for row in moviereader:
                yield (row[0], row[1])

if __name__ == "__main__":
    commander = Commander()
    freqVec, vocabVec = commander.readVocabulary('training.txt')
    for doc, label in commander.getDocuments('training.txt'):
        print label + ":\t\t" + doc
        # print label
    # print(freqVec)
    # print(vocabVec)

    # def tokenizeSentence(self, sentence):


