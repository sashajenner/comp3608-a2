import sys
from DT import DT
from NB import NB

assert len(sys.argv) == 3, "Invalid Args"

data_fname = sys.argv[1]
data_f = open(data_fname)


# parse file to get folds
folds = []
for row in data_f.readlines():
    row = row.rstrip()
    if row == "": continue

    if row.startswith("fold"):
        fold_num = int(row[4:])
        folds.append([])
        continue

    row = row.split(",")
    folds[fold_num-1].append(row)

data_f.close()




alg = sys.argv[2]
if alg == 'NB':
    classy_class = NB
elif alg == 'DT':
    classy_class = DT


# cross validate on each fold
accuracies = []

for k in range(len(folds)):
    #print([i for i in range(len(folds)) if i != k])
    #print(len([folds[i] for i in range(len(folds)) if i != k]))

    rows_train = sum([folds[i] for i in range(len(folds)) if i != k], [])
    rows_test = folds[k]

    print(rows_test[0])

    #print(len(rows_train), len(rows_test))

    classy = classy_class()
    classy.train(rows_train)

    attr_test = [row[:-1] for row in rows_test]
    class_test = [row[-1] for row in rows_test]

    results = classy.test(attr_test)

    correct = [i==j for i,j in zip(class_test, results)]
    correct_prop = sum(correct) / len(results)
    print(k, correct_prop)

    accuracies.append(correct_prop)


print(sum(accuracies) / len(accuracies))
