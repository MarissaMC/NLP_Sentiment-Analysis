import sys
import re, string

input = sys.argv[1]
output = sys.argv[2]

from collections import defaultdict
import json

# find the number of classes
total_class=[]
input1=open(input,'r',errors='ignore')

n_file=0     # number of files
for sen in input1:
    cl=sen.split()[0]
    total_class.append(cl)
    n_file+=1

Class=set(total_class)
length=len(Class)

dic=defaultdict()
dic['N_rank']={}

r=0
for c in Class:
    dic['N_rank'][c]=r
    r+=1

dic['Num_class']=[0]*length

# delete part of preposition
pun = set(string.punctuation)
pun = pun.difference('$')


input2=open(input,'r',errors='ignore')
for sen in input2:
    cl=sen.split()[0]
    r_c=dic['N_rank'][cl]
    dic['Num_class'][r_c]+=1

    for word in sen.split():
        if word not in pun:
           if word in dic:
              dic[word][r_c]+=1
           if word not in dic:
              dic[word]=[0]*length
              dic[word][r_c]=1



# smoothing
dic_final=defaultdict()

for w in dic:
    judge=0
    if w!='N_rank' and w!='Num_class' and w!='Num_Work_class':
       for i in range(length):
           if dic[w][i]==0:
              dic[w][i]=1
              for j in range(length):
                  if j!=i:
                     dic[w][j]+=1

           judge+=dic[w][i]

       dic_final[w]=dic[w]    

# P_class
for c in Class:
    r_c=dic['N_rank'][c]
    dic['Num_class'][r_c]=dic['Num_class'][r_c]/float(n_file)

dic_final['N_rank']=dic['N_rank']
dic_final['Num_class']=dic['Num_class']


# write into spam.nb
json.dump(dic_final, open(output,'w'))


