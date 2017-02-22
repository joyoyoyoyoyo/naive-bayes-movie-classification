import unittest

from main.Commander import Commander


class IntegrationTest(unittest.TestCase):

    def setUp(self):
        self.commander = Commander()

    def tearDown(self):
        self
    def testTrain(self):
        trainingMat = self.commander.readVocabulary('training.txt')
        print trainingMat
        print trainingMat.shape
        # trainMat =
    def testClassify(self):
        self
