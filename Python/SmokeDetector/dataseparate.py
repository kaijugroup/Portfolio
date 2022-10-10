#Short program to separate the original data into two datasets, one to train the algorithm and one to test.

import csv

train = []
test = []
headers = 0

with open('data/smoke_detection_iot.csv', newline='') as fulldata:
    rdr = csv.reader(fulldata, delimiter=',')
    i=0
    for row in rdr:
        if i==0:
            test.append(row)
            train.append(row)
        elif i%2==0:
            train.append(row)
        else:
            test.append(row)
        i=i+1

print(headers)

with open('data/testdata.csv', 'w', newline='') as testfile:
    wtr = csv.writer(testfile)
    for row in test:
        wtr.writerow(row)

with open('data/traindata.csv', 'w', newline='') as trainfile:
    wtr = csv.writer(trainfile)
    for row in train:
        wtr.writerow(row)

