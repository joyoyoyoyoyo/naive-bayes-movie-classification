The validate program tests if the output of a NaiveBayesClassifier program is correctly formatted. To run the validation program you need to have java 7 installed (available in CSIL). To execute a jar file you must type:
java -jar <jar_file>

The validation program reads from the standard input so you can redirect the output of your program into it like this:
C/C++: ./NaiveBayesClassifier training.txt testing.txt | java -jar validate.jar
Java: java NaiveBayesClassifier training.txt testing.txt | java -jar validate.jar
Python: python NaiveBayesClassifier.py training.txt testing.txt | java -jar validate.jar

If the validation program prints an error, then the output of your program is wrongly formatted and you will need to fix it. If the program gives a success message then the output format is correct.
