#This is a program for analyzing the detection of smoke from a smoke detector.

import math
import numpy as np
import pandas as pd

#Data is separated into training and testing data by dataseparate.py into the files testdata.csv and traindata.csv in the data file. 

testfile = 'data/testdata.csv'
testdata = pd.read_csv(testfile)

trainfile = 'data/traindata.csv'
traindata = pd.read_csv(trainfile)

shape = traindata.shape
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

#Logistic regression algorithm.  Binary classification, 1 for smoke detected, 0 for no smoke detected.

#Coefficients of each column. cf[0:12] are coefficients for the variable input from the columns. cf[13] is the coefficient not associated with a variable.
cf = [1,1,1,1,1,1,1,1,1,1,1,1,1,1]
colavg = []

def rd(n):
    try:
        return(round(n,4))
    except (RuntimeError, RuntimeWarning):
        print(n)
        return(0)

for col in traindata.columns:
    colavg.append(rd(traindata[col].mean()))

def logreg(s):
    #Input s of a list length 13 created from the 13 variable outputs of the smoke detector
    v0 = rd(cf[0]*s[0])
    v1 = rd(cf[1]*s[1])
    v2 = rd(cf[2]*s[2])
    v3 = rd(cf[3]*s[3])
    v4 = rd(cf[4]*s[4])
    v5 = rd(cf[5]*s[5])
    v6 = rd(cf[6]*s[6])
    v7 = rd(cf[7]*s[7])
    v8 = rd(cf[8]*s[8])
    v9 = rd(cf[9]*s[9])
    v10 = rd(cf[10]*s[10])
    v11 = rd(cf[11]*s[11])
    v12 = rd(cf[12]*s[12])
    v13 = cf[13]
    var = [v0,v1,v2,v3,v4,v5,v6,v7,v8,v9,v10,v11,v12,v13]
    poly = v0+v1+v2+v3+v4+v5+v6+v7+v8+v9+v10+v11+v12+v13
    #if poly < 0.000001:
        #poly = 0
    #else:
       # poly = rd(poly)
    denom = 1 + np.exp(-poly)
    p = rd(1/denom)
    return(p)

def inputproc(row):
    #Input the row and return a list for use in training and testing
    new = []
    flag = row[15]
    row = row[2:15]
    i = 0
    while i < 13:
        n = row[i]/colavg[i]
        new.append(rd(n))
        i+=1
    new.append(flag)
    return(new)


def train():
    i = 0
    #when its working (rownum-1)
    while i < 1500:
        var = inputproc(traindata.loc[i])
        aflag = var[13]

        initlg = logreg(var)
        if aflag==0 and initlg>0.001:
            #change the coefficients until they reflect a lower logreg result
            j=0
            while j < 13:
                diff = abs(var[j]-cf[j])
                new = cf[j]-(diff*0.01)
                cf[j] = rd(new)
                j+=1
            cf[13] = rd(cf[13] - (abs(1-initlg)*0.01))
        elif aflag==1 and initlg<0.999:
            #change the coefficients until they reflect a larger logreg result
            j=0
            while j < 14:
                diff = abs(var[j]-cf[j])
                new = cf[j]-(diff*0.01)
                cf[j] = rd(new)
                j+=1
            cf[13] = rd(cf[13] + (abs(1-initlg)*0.01))
        else:
            i+=1
print(cf)
train()
print(cf)

#Testing statistics

shape = testdata.shape
rownum = shape[0]

def test():
    scounter = 0 #counter for successes
    fcounter = 0 #counter for failures
    flag1 = 0
    flag0 = 0
    i = 0
    while i < (rownum-1):
        var = inputproc(traindata.loc[i])
        result = var[13]
        guess = logreg(var)
        if result==0:
            flag0+=1
        else:
            flag1+=1
        if guess==result:
            scounter+=1
        else:
            fcounter+=1
        i+=1
    print("Successes: {}".format(scounter))
    print("Failures: {}".format(fcounter))
    print("Total alarms: {}".format(flag1))

test()



