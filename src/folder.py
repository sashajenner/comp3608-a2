'''
Split a dataset into 10 folds for stratified cross-validation.
Number of instances per fold doesn't vary by more than one.
Ratio of yes and no examples approximately equal for each fold.
Print out the result.

Usage: python3.8 $0 <DATA_PATH>
'''

import sys
import math

data_fname = sys.argv[1]
data_f = open(data_fname)
data = [row.rstrip().split(',') for row in data_f.readlines()]

n_folds = 10
folds = [[] for i in range(n_folds)]


n_rows = len(data)
n_yes = 0
n_no = 0
for row in data:
    if row[-1] == 'yes':
        n_yes += 1
    elif row[-1] == 'no':
        n_no += 1

# Find the number of instances in each fold
lower = math.floor(n_rows / n_folds)
upper = math.ceil(n_rows / n_folds)
n_upper = round((n_rows / n_folds - lower) * n_folds)
folds_num = [upper if i < n_upper else lower for i in range(n_folds)]

# Find the number of yes in each fold
lower_y = math.floor(n_yes / n_folds)
upper_y = math.ceil(n_yes / n_folds)
n_upper_y = round((n_yes / n_folds - lower_y) * n_folds)
folds_num_y = [upper_y if i < n_upper_y else lower_y for i in range(n_folds)]

# Fill in folds
for row in data:
    for i in range(n_folds):
        if folds_num_y[i] != 0 and row[-1] == 'yes':
            folds_num_y[i] -= 1
            folds_num[i] -= 1
            folds[i].append(row)
        elif folds_num[i] != 0 and row[-1] == 'no':
            folds_num[i] -= 1
            folds[i].append(row)

# Print folds
for i in range(n_folds):
    print(f'fold{i+1}')
    for instance in folds[i]:
        print(','.join(instance))
    if i != n_folds - 1:
        print()


data_f.close()
