PYTHON=python3.8

.PHONY: build test clean

build: test
	mkdir build -p
	$(PYTHON) src/folder.py data/pima.csv > data/pima-folds.csv
	zip -uj build/MyClassifier.zip \
		src/*.py \
		data/pima.csv data/pima-CFS.csv data/pima-discretised-CFS.csv data/pima-folds.csv \
		docs/report.pdf

test:
	./test.sh

clean:
	rm build/*
