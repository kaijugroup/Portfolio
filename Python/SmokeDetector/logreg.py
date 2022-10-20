#This is a program for analyzing the detection of smoke from a smoke detector.

import math
import numpy as np
import pandas as pd

#Data is separated into training and testing data by dataseparate.py into the files testdata.csv and traindata.csv in the data file. 

testfile = 'data/testdata.csv'
testdata = pd.read_csv(testfile)

trainfile = 'data/traindata.csv'
traindata = pd.read_csv(trainfile)

shape = testdata.shape
rownum = shape[0] #Number of rows for test data
colnum = shape[1] #Number of columns for test data

#Summary of the data elements:
#Col 0: Index
#Col 1: UTC timestamp
#Col 2: Temperature (C)
#Col 3: Humidity (%)
#Col 4: Total Volatile Organic Compounds (ppb)
#Col 5: eCO2 (ppm)
#Col 6: Raw H2
#Col 7: Raw Ethanol
#Col 8: Pressure (hPa)
#Col 9: Particulant Matter 1.0
#Col 10: Particulant Matter 2.5
#Col 11: NC0.5
#Col 12: NC1.0
#Col 13: NC2.5
#Col 14: CNT
#Col 15: Alarm Flag

#The columns that will be used as variables for the logistic regression algorithm will be columns 2-14,
#13 in total.

#Creating a dataframe of the columns to be used for training and then normalizing.

temptd = testdata.iloc[:, [2,3,4,5,6,7,8,9,10,11,12,13,14]]

i=0
for col in temptd.columns:
    powcol = temptd[col].apply(lambda x: x*x)
    sumcol = sum(powcol)
    sqcol = math.sqrt(sumcol)
    newcol = temptd.iloc[i].apply(lambda x: x/sqcol)
    temptd.assign(col=newcol)
    i+=1

#Logistic regression algorithm.  Binary classification, 1 for smoke detected, 0 for no smoke detected.

#Coefficients of each column. cf[0:12] are coefficients for the variable input from the columns. cf[13] is the coefficient not associated with a variable.
cf = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]

def logreg(s):
    #Input s of a list length 13 created from the 13 variable outputs of the smoke detector
   poly = (cf[0]*s[0])+(cf[1]*s[1])+(cf[2]*s[2])+(cf[3]*s[3])+(cf[4]*s[4])+(cf[5]*s[5])+(cf[6]+s[6])+(cf[7]*s[7])+(cf[8]*s[8])+(cf[9]*s[9])+(cf[10]*s[10])+(cf[11]*s[11])+(cf[12]*s[12])+cf[13]
   denom = 1 + math.exp(-poly)
   p = 1/denom
   return(p)

def train():
    i = 1
    while i < 10:
        row = testdata.iloc[[i]].to_numpy()
        aflag = row[0,15]
        var = row[0, 2:15]
        var.flatten()

        initlg = logreg(var)
        j=0
        if aflag==0 and initlg>0.02:
            #change the coefficients until they reflect a lower logreg result
            while j < 13:
                diff = abs(var[j]-cf[j])
                new = cf[j]-(diff*0.1)
                cf[j] = new
                j+=1
            i+=1
            continue
        elif aflag==1 and initlg<0.98:
            #change the coefficients until they reflect a larger logreg result
            while j < 14:
                diff = abs(var[j]-cf[j])
                new = cf[j]-(diff*0.1)
                cf[j] = new
                j+=1
            i+=1
            continue
        else:
            i+=1
            continue

print(cf)

train()

print(cf)

#Testing statistics








