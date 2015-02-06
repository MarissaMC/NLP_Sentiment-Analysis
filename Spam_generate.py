import sys
import glob

input=sys.argv[1]

HAM_files = glob.glob1(input,'[HAM]*.txt')
SPAM_files = glob.glob1(input,'[SPAM]*.txt')


with open("spam_train.txt", "w") as fout:
  for fileName in HAM_files:
    with open(fileName, "r") as f:
                  fout.write ("HAM ")
                  fout.write (" ".join(line.strip() for line in f) )
                  fout.write ('\r\n')
  for fileName in SPAM_files:
    with open(fileName, "r") as f:
                  fout.write ("SPAM ")
                  fout.write (" ".join(line.strip() for line in f) )
                  fout.write ('\r\n')