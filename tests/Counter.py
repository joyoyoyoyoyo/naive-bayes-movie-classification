import unittest

class Counter(unittest.TestCase):
    def setUp(self):
        self

    def tearDown(self):
        self

    def testWordCountInDocument(self):
        sentence = "Bromwell High is a cartoon comedy. It ran at the same time as some other programs about school life, such as \"Teachers\". My 35 years in the teaching profession lead me to believe that Bromwell High's satire is much closer to reality than is \"Teachers\". The scramble to survive financially, the insightful students who can see right through their pathetic teachers' pomp, the pettiness of the whole situation, all remind me of the schools I knew and their students. When I saw the episode in which a student repeatedly tried to burn down the school, I immediately recalled ......... at .......... High. A classic line: INSPECTOR: I'm here to sack one of your teachers. STUDENT: Welcome to Bromwell High. I expect that many adults of my age think that Bromwell High is far fetched. What a pity that it isn't!	1"
        word = 'comedy'
        self

    def testWordNotInVocab(self):
        self

    def testWordInVocab(self):
        self

    def testProbWithWordNotInVocab(self):
        self

    def testProbWithWordInVocab(self):
        self

    def testUnionNewWord(self):
        self

    def testUnionOldWord(self):
        self

    def testAlwaysTheSameSize(self):
        self

    def testProbabilityIsNotZeroWithLaplaceSmoothing(self):
        self

    def testProbabilityIsZeroWithoutLaplaceSmoothing(self):
        self

    def testStopWordsOmitted(self):
        self

    def testSentenceIsVectorizedToBigrams(self):
        self

    def testTF_IDF(self):
        self

    def testWordsAreStemmed(self):
        self


if __name__ == '__main__':
    unittest.main()