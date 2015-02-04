import sys
import re, string
import math

model = sys.argv[1]
testfile = sys.argv[2]

from collections import defaultdict
import json

dic = json.load(open(model))

# get the prob of class, conditional prob

P_ham=dic['pro_ham']
P_spam=dic['pro_spam']

wc_ham=dic['num_ham']
wc_spam=dic['num_spam']


if model=='spam.nb':
    switch=0
if model=='sentiment.nb':
    switch=1
   
if switch==0:
    a="HAM"
    b="SPAM"
if switch==1:
    a="POS"
    b="NEG"

x=0

pun = set(string.punctuation)


with open(testfile,'r') as f:
     for line in f:
         ham_cp=1
         spam_cp=1

         for word in line.split():
             if word not in pun:
        	     ham_word='h_'+word
        	     spam_word='s_'+word
        	
             if ham_word in dic:
                ham_cp+=math.log(float(dic[ham_word])/float(wc_ham))        
                if spam_word in dic:
                      spam_cp+=math.log(float(dic[spam_word])/float(wc_spam))
            
         #classify_ham=float(P_ham*ham_cp)/float(P_ham*ham_cp+P_spam*spam_cp)
         
         if math.log(1)+math.log(P_ham)+ham_cp > math.log(P_spam)+spam_cp:
            print(a)
         else:
            print(b)
 

