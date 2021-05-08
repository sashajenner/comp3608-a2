.PHONY: build test clean

build: test
	mkdir build -p
	zip -uj build/MyClassifier.zip \
		src/*.py \
		data/pima.csv data/pima-CFS.csv data/pima-discretised-CFS.csv \
		docs/report.pdf
		#data/pima-folds.csv

test:
	./test.sh

clean:
	rm build/*
