import sys
import glob

input=sys.argv[1]

NEG_files = glob.glob1(input,'[NEG]*.txt')
POS_files = glob.glob1(input,'[POS]*.txt')


with open("sentiment_train.txt", "w") as fout:
  for fileName in NEG_files:
    with open(fileName, "r") as f:
                  fout.write ("NEG ")
                  fout.write (" ".join(line.strip() for line in f) )
                  fout.write ('\r\n')
  for fileName in POS_files:
    with open(fileName, "r") as f:
                  fout.write ("POS ")
                  fout.write (" ".join(line.strip() for line in f) )
                  fout.write ('\r\n')
