import subprocess
import shlex # args = shlex.split(command)


class Commander:

    # def __init__(self):

    # Training data vocabulary size: 35918
    # Testing  data vocabulary size: 11123
    def readVocabulary(self, filename, pathDirectory='./resources/'):
        command = "tr 'A-Z' 'a-z' < " + pathDirectory + filename + " | " + "tr -sc 'A-Za-z' '\\n' | sort | uniq -c"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        retcode = proc.poll()
        freqMat = []
        vocabMat = []
        for line in iter(proc.stdout.readline, b''):
            frequencyCount, word = line.decode('utf-8').split()
            freqMat.append(frequencyCount)
            vocabMat.append(word)
            # print(frequencyCount + ':\t\t' + word)
            # print(label)
            # print(test)
        proc.stdout.close()
        proc.stdin.close()
        return freqMat, vocabMat

if __name__ == "__main__":
    # commander = Commander(filename='traning.txt')
    # print(commander._args)
    commander = Commander()
    freqVec, vocabVec = commander.readVocabulary('training.txt')
    print(freqVec)
    print(vocabVec)


    # def tokenizeSentence(self, sentence):
    #
    #
    # String
    # mergeAndDel = "tr 'A-Z' 'a-z' < " + pathDirectory + filename + " | " + "tr -sc 'A-Za-z' '\\n' | sort | uniq -c";
    #
    # Process
    # p = Runtime.getRuntime().exec(new
    # String[]
    # {"bash", "-c", mergeAndDel});
    #
    # // p.waitFor();
    # BufferedReader
    # buf = new
    # BufferedReader(new
    # InputStreamReader(p.getInputStream()));
    # String
    # line = "";
    # int
    # vocabularyCount = 0;
    # while ((line=buf.readLine()) != null) {
    # ++vocabularyCount;
    # System.out.println(line);
    # }
    # System.out.println(vocabularyCount);


