import subprocess
import shlex # args = shlex.split(command)


class Commander:

    # def __init__(self):


    def readVocabulary(self, filename, pathDirectory='./resources/'):
        command = "tr 'A-Z' 'a-z' < " + pathDirectory + filename + " | " + "tr -sc 'A-Za-z' '\\n' | sort | uniq -c"
        proc = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE, shell=True)
        retcode = proc.poll()
        for line in iter(proc.stdout.readline, b''):
            frequencyCount, word = line.decode('utf-8').split()
            print(frequencyCount + ':\t\t' + word)
            # print(label)
            # print(test)

        proc.stdout.close()
        proc.stdin.close()

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
    print(commander.readVocabulary('training.txt'))


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


