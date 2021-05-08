.PHONY: build test clean

build: test
	mkdir build -p
	zip -u build/MyClassifier.zip \
		src/*.py \
		data/pima.csv \
		docs/report.pdf
		#data/pima-folds.csv data/pima-CFS.csv data/pima-discretised-CFS.csv

test:
	./test.sh

clean:
	rm build/*
