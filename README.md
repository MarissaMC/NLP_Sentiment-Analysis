------------------------------------------------------------------------------
Created by Mengchun Wu, 2/4/2015
## Motivation
This homework aims at practice Naive Bayes algorithm.
For Part I, I used dictionary to store model information.
I didn't refer to special source but just basic python programming skill.
------------------------------------------------------------------------------

## Description of files:

-------------------------------------------------------------------------------
Spam_generate.py : to generate the training file from the Spam training documents

Sentiment_generate.py : to generate the training file from the Sentiment training documents

spam.nb : model file for spam dataset

sentiment.nb : model file for sentiment dataset

spam.out : STDOUT output of classification program on the spam test set

sentiment.out : STDOUT output of classification program on the sentiment test set

nblearn.py : use train dataset to build model

nbclassify.py : use model to classify test dataset

----------------------------------------------------------------------------------
In part2:

spam.svm.model : model file for spam dataset using SVM

sentiment.svm.model : model file for sentiment dataset using SVM

spam.megam.model : model file for spam dataset using Megam

sentiment.megam.model : model file for sentiment dataset using Megam
-------------------------------------------------------------------------------
## Code Example
---------------------------------------------------------------------------------
Use Spam_generate.py to generate files like "SPAM.00001.txt" or "HAM.00001.txt" into training file like below:

HAM subject : meeting today hi , could we have a meeting today . thank you . 

SPAM subject : low rates click here to apply for new low rates do not miss this chance !

-----------------------------------------------------------------------------------
You can use Spam_generate.py in this way:

python3 Spam_generate.py PATH/TO/FILES spam_train_file

Sentiment.py is used in the same way to generate sentiment train file.

------------------------------------------------------------------------------------
To learn a classification model from the training data file:

python3 nblearn.py TRAININGFILE MODELFILE

where TRAININGFILE is the name of the training file, MODELFILE is the name of the file that will contain the model that your classifier will learn
(for the spam dataset the file name should be spam.nb, and sentiment.nb for the sentiment dataset).

-------------------------------------------------------------------------------

Next we can classify files like:

FEATURE_11 FEATURE_12 ... FEATURE_1N 

FEATURE_21 FEATURE_22 ... FEATURE_2N 

... 

FEATURE_M1 FEATURE_M2 ... FEATURE_MN 

---------------------------------------------------------------------------------
To classify a file with new documents, use nbclassify.py like below:

python3 nbclassify.py MODELFILE TESTFILE

where MODELFILE is the name of the model file generated by nblearn, TESTFILE is the name of the file containing the features for the new documents to be classified.

-------------------------------------------------------------------------------
## Answer for Part III
-------------------------------------------------------------------------------
# Question 1

Precision for ham is 0.981963927856
Precision for spam is 0.945205479452

Recall for ham is 0.98
Recall for spam is 0.95041322314

F-score for ham is 0.980980980981
F-score for spam is 0.947802197802


Precision for pos is 1
Precision for neg is 0.9558824

Recall for pos is 0.9756098
Recall for neg is 1

F-score for pos is 0.9876543
F-score for neg is 0.9774436

# Question 2

# For SVM

Precision for ham is 0.98997995992
Precision for spam is 0.967123287671

Recall for ham is 0.988
Recall for spam is 0.972451790634

F-score for ham is 0.988988988989
F-score for spam is 0.96978021978

Precision for pos is 0.9038462
Precision for neg is 0.6547619

Recall for pos is 0.7642276
Recall for neg is 0.8461538

F-score for pos is 0.8281938
F-score for neg is 0.738255


# For MegaM

Precision for ham is 0.960591133005
Precision for spam is 0.92774566474

Recall for ham is 0.975
Recall for spam is 0.8891966759

F-score for ham is 0.967741935484
F-score for spam is 0.908062234795

Precision for pos is 0.8859649
Precision for neg is 0.7027027

Recall for pos is 0.8211382
Recall for neg is 0.8

F-score for pos is 0.8523207
F-score for neg is 0.7482014

# Question 3

If only 10% of the training data is used

# For Naive Bayes

Precision for ham is 0.926622765757
Precision for spam is 0.95

Recall for ham is 0.985
Recall for spam is 0.785123966942

F-score for ham is 0.954920019389
F-score for spam is 0.859728506787


Precision for pos is 1
Precision for neg is 0.8666667

Recall for pos is 0.9186992
Recall for neg is 1

F-score for pos is 0.9576271
F-score for neg is 0.9285714


# For SVM

Precision for ham is 0.815333882935
Precision for spam is 0.926666666667

Recall for ham is 0.989
Recall for spam is 0.382920110193

F-score for ham is 0.893809308631
F-score for spam is 0.541910331384

Precision for pos is 0.9027778
Precision for neg is 0.5

Recall for pos is 0.5284553
Recall for neg is 0.8923077

F-score for pos is 0.6666667
F-score for neg is 0.640884

# For MegaM

Precision for ham is 
Precision for spam is 

Recall for ham is 
Recall for spam is 

F-score for ham is 
F-score for spam is 

Precision for pos is 
Precision for neg is 

Recall for pos is 
Recall for neg is 

F-score for pos is 
F-score for neg is 

