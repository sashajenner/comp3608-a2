'''
Build the Naive Bayes or Decision Tree classifier using the train data.
Print out the predicted class for each test data example.

Usage: python3.8 $0 <TRAIN_DATA_PATH> <TEST_DATA_PATH> NB|DT [FLAG]
'''

import sys
from NB import NB
from DT import DT

# Parse arguments
train_fname, test_fname, alg = sys.argv[1:4]
if len(sys.argv) > 4:
    flag = sys.argv[4]
else:
    flag = None

train_f = open(train_fname)
test_f = open(test_fname)

train_data = [row.rstrip().split(',') for row in train_f.readlines()]
test_data = [row.rstrip().split(',') for row in test_f.readlines()]


if alg == 'NB':
    classy = NB()
elif alg == 'DT':
    classy = DT()

classy.train(train_data)

for result in classy.test(test_data):
    print(result)


train_f.close()
test_f.close()
