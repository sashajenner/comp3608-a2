from DT import DT

DATA_FILE = "data/pima-indians-diabetes.discrete"
COLUMNS = [
    "npreg",
    "glucose",
    "blood",
    "triceps",
    "insulin",
    "bmi",
    "pedigree",
    "age"
]

train_f = open(DATA_FILE)
train_data = [row.rstrip().split(',') for row in train_f.readlines()]
train_f.close()

dt = DT()
dt.train(train_data)

dt.print(COLUMNS, dt.tree)


