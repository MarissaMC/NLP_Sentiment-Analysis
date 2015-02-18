import sys
import re, string
import math
import operator

model = sys.argv[1]
testfile = sys.argv[2]
#output=sys.argv[3]

from collections import defaultdict
import json

dic = json.load(open(model))


# P_wc
length=len(dic['N_rank'])
dic['Num_Work_class']=[0]*length

for c in dic['N_rank']:

    r_c=dic['N_rank'][c]
    for w in dic:
        if w!='N_rank' and w!='Num_class' and w!='Num_Work_class':
           dic['Num_Work_class'][r_c]+=dic[w][r_c]

    for w in dic:
        if w!='N_rank' and w!='Num_class' and w!='Num_Work_class':
           dic[w][r_c]=dic[w][r_c]/float(dic['Num_Work_class'][r_c])  


#with open(output,'w') as outp:
with open(testfile,'r',errors='ignore') as f:
     for line in f:

         judge=defaultdict()

         for c in dic['N_rank']:
             r_c=dic['N_rank'][c]
             judge[c]=math.log(dic['Num_class'][r_c])
             for word in line.split():
                 if word in dic:
                    judge[c]+=math.log(dic[word][r_c])
          
         sys.stdout.write(max(judge, key=judge.get))
         sys.stdout.write('\n')
 

