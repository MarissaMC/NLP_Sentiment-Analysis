import sys
import re, string


input = sys.argv[1]
output = sys.argv[2]

from collections import defaultdict
import json

HAM_data_o=[]
SPAM_data_o=[] 
HAM_data=[]
SPAM_data=[] 

# add switch to judge sentiment and spam
switch=0

with open(input,'r') as f:
    for line in f:
        if line[0]=='H' or line[0]=='P':
        	HAM_data_o.append(line)
        if line[0]=='S' or line[0]=='N':
            SPAM_data_o.append(line)
            if line[0]=='N':
                switch=1

# calculate P(class)

P_ham = float(len(HAM_data_o))/float(len(HAM_data_o)+len(SPAM_data_o))
P_spam = 1 - P_ham

for sent in HAM_data_o:
    HAM_data+=sent.split()

# number of words in ham
d_ham_sum=len(HAM_data)

for sent in SPAM_data_o:
    SPAM_data+=sent.split()

d_spam_sum=len(SPAM_data)

# start calculate frequency
# dict

# delete punctuation
pun = set(string.punctuation)
pun = pun.difference('$')
# delete part of preposition
pre = set(['are','the','this','that','and','ect','with','under','from','for','HAM','SPAM','you','your','her','his','him','Subject:','Subject','has','have','already','had','mean','some','been','our','hello','june','off','being','then','here','there','such','where','who','when','which','its','into','how','may','upon'])
verb=set(['provide','run','including','not','will','any','what','were','did','didn','done'])
month=set(['march','october','oct','november','nov','july','week','august','day','tuesday','monday','wednesday','thursday','friday','year','years','after','along','summer','december','january'])
nun=set(['information','jones','smith','jeffrey','other','joe','they','james','jim','their','them','europe','india','mary','canada','sally','london','mike','jeff','bob','john'])

# exception in dic
pun.update(pre,verb,month,nun)

d_ham = defaultdict(int)
for word in HAM_data:
    if word not in pun and not str(word).isdigit() and len(word)>2:
        d_ham[word] += 1


d_spam = defaultdict(int)
for word in SPAM_data:
    if word not in pun and not str(word).isdigit() and len(word)>2:
        d_spam[word] += 1 


# clean dic
dn_ham=defaultdict(int)
dn_spam=defaultdict(int)

# buffer dic
b_dic=dict(list(d_ham.items())+list(d_spam.items()))

for i in b_dic:
    if d_ham[i]+d_spam[i]>50:
        new_h='h_'+i
        new_s='s_'+i
        dn_ham[new_h]=d_ham[i]
        dn_spam[new_s]=d_spam[i]

for j in dn_ham:
    if dn_ham[j]==0:
        dn_ham[j]=1

for j in dn_spam:
    if dn_spam[j]==0:
        dn_spam[j]=1

dn_ham['num_ham']=d_ham_sum
dn_ham['num_spam']=d_spam_sum
dn_ham['pro_ham']=P_ham
dn_ham['pro_spam']=P_spam

if switch==1:
    dn_ham['switch']=1

new_dict=dict(list(dn_ham.items())+list(dn_spam.items()))

# write into spam.nb
json.dump(new_dict, open(output,'w'))


# Naive Bayes

# d_ham=d_ham/d_spam_sum

