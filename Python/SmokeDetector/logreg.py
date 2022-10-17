#This is a program for analyzing the detection of smoke from a smoke detector.

import numpy as np
import pandas as pd

#Data is separated into training and testing data by dataseparate.py into the files testdata.csv and traindata.csv in the data file. 

testfile = 'data/testdata.csv'
testdata = pd.read_csv(testfile)

trainfile = 'data/traindata.csv'
traindata = pd.read_csv(trainfile)

#print(testdata.describe())
#print(traindata.describe())
#8 rows by 16 columns

def avg(s):
    total = sum(s)
    print(total)
    print(len(s))
    return(total/len(s))

i=0
while i<16:
    t = traindata.iat[0,i]
    print(t)
    i+=1


#Logistic regression algorithm.  Binary classification, 1 for smoke detected, 0 for not.


#Testing statistics
