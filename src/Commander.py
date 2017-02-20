import os
import subprocess
import shlex

class Commander:

    # def __init__(self):


    def testReadInput(self, filename, pathDirectory='./resources/'):
        command = "tr 'A-Z' 'a-z' < " + pathDirectory + filename + " | " + "tr -sc 'A-Za-z' '\\n' | sort | uniq -c";
        args = shlex.split(command)
        proc = subprocess.Popen(command, stdin=subprocess.PIPE, shell=True)
        out = proc.communicate()
        # print(out.rstrip().decode('UTF-8'))
        # proc.communicate(b"input data\n")
        # out, err = proc.communicate()
        # with open
        # while True:
        #     # line = proc.stdout.readline()
        #     if line != '':
        #         # the real code does filtering here
        #         print("test:", line.rstrip().decode('UTF-8'))
        #     else:
        #         break
        # # args = shlex.split(_path)
        # if pathDir is './resources/':
        #
        # process = subprocess.Popen()

if __name__ == "__main__":
    # commander = Commander(filename='traning.txt')
    # print(commander._args)
    commander = Commander()
    print(commander.testReadInput('training.txt'))


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


