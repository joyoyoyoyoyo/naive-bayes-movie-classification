
import csv

RESOURCES_DIR = '../resoucres/'
TRAINING_FILE = 'training.txt'

def populate_training_mat():
    train_mat


def getDocuments(self, filename, pathDirectory='./resources/'):
    with open(pathDirectory + TRAINING_FILE, 'rb') as csvfile:
        moviereader = csv.reader(csvfile, delimiter='\t')
        for row in moviereader:
            yield (row[0], row[1])