import unittest
import numpy as np

from main.Commander import Commander


class IntegrationTest(unittest.TestCase):

    def setUp(self):
        self.commander = Commander()

    def tearDown(self):
        self
    def test_read_vocab_freq_mat(self):
        vocab_freq_mat = self.commander.readVocabulary('training.txt')
        print vocab_freq_mat
        print vocab_freq_mat.shape
        # trainMat =

    def test_read_corpus(self):
        docs = []
        labels = []
        for doc, label in self.commander.getDocumentsYield('training.txt'):
            docs.append(doc)
            labels.append(label)

        # return docs, labels
        corpus = np.column_stack((docs, labels))
        print corpus
        return corpus

    def testClassify(self):
        self
