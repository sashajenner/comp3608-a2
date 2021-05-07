import sys

# Arguments
train_fname, test_fname, alg = sys.argv[1:4]

train_f = open(train_fname)
test_f = open(test_fname)

train_data = [row.split(',') for row in train_f.readlines()]
test_data = [row.split(',') for row in test_f.readlines()]
