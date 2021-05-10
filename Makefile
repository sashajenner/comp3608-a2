PYTHON=python3

.PHONY: test clean

build/MyClassifier.zip: src/*.py data/pima.csv data/pima-CFS.csv data/pima-discretised-CFS.csv data/pima-folds.csv docs/report.pdf
	mkdir build -p
	zip -uj $@ $^

data/pima-folds.csv: src/folder.py data/pima.csv
	$(PYTHON) $^ > $@

data/pima-folds-discretised.csv: src/folder.py data/pima-indians-diabetes.discrete
	$(PYTHON) $^ > $@

data/pima-folds-CFS.csv: src/folder.py data/pima-CFS.csv
	$(PYTHON) $^ > $@

data/pima-folds-discretised-CFS.csv: src/folder.py data/pima-discretised-CFS.csv
	$(PYTHON) $^ > $@

docs/report.pdf: docs/*.tex docs/*.bib
	cd docs && \
		xelatex report && \
		bibtex report && \
		makeindex -s nomencl.ist -o report.nls report.nlo && \
		xelatex report && \
		xelatex report && \
		cd ../

test:
	sh test.sh

clean:
	rm -r build; \
		cd docs && \
		rm *.aux *.log *.bbl *.blg *.lof *.lot *.out *.toc *.ilg *.nlo *.nls report.pdf && \
		cd ../
