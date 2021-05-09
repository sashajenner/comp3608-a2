PYTHON=python3

.PHONY: test clean

build/MyClassifier.zip: src/*.py data/pima.csv data/pima-CFS.csv data/pima-discretised-CFS.csv data/pima-folds.csv docs/report.pdf
	mkdir build -p
	zip -uj $@ $^

data/pima-folds.csv: src/folder.py data/pima.csv
	$(PYTHON) $^ > $@

#docs/report.pdf: docs/*.tex
#	cd docs && xelatex report.tex && cd ../

test:
	sh test.sh

clean:
	#rm docs/*.aux docs/*.log docs/*.out docs/report.pdf; rm -r build
	rm -r build
