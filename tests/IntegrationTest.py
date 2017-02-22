import unittest
import numpy as np

from main.Commander import Commander


class IntegrationTest(unittest.TestCase):

    def setUp(self):
        self.commander = Commander()

    def tearDown(self):
        self

    def test_read_vocab_freq_dict(self):
        vocab_freq_dict = self.commander.readVocabulary('training.txt')
        print vocab_freq_dict



    # def test_read_vocab_freq_mat(self):
    #     vocab_freq_mat = self.commander.readVocabulary('training.txt')
    #     print vocab_freq_mat
    #     # print vocab_freq_mat.shape
    #     # trainMat =

    def test_read_corpus(self):
        corpus = self.commander.get_corpus_as_numpy('training.txt')
        print corpus

    # def test_union_dictionary(self):
        # union = self.commander.init_vocabulary_from_corpus('training.txt')


    def testClassify(self):
        self
