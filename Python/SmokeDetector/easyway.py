
import pandas as pd
import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split

trainfile = 'data/trainfile.csv'
train = pd.read_csv(trainfile)
testfile = 'data/testfile.csv'
test = pd.read_csv(testfile)



