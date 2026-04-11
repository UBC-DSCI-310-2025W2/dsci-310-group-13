# authors: Group 13

.PHONY: all clean

export PYTHONPATH := $(shell pwd)

all: data/raw/winequality-red.csv \
	data/processed/wine_cleaned.csv \
	data/processed/train.csv \
	data/processed/test.csv \
	results/validation_report.txt \
	results/figures/quality_distribution.png \
	results/metrics.txt \
	reports/wine-quality-classification.html

# script 01 - download raw data
data/raw/winequality-red.csv data/raw/winequality-white.csv: scripts/01_download_data.py
	mkdir -p data/raw
	python scripts/01_download_data.py \
		--red-url "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-red.csv" \
		--white-url "https://archive.ics.uci.edu/ml/machine-learning-databases/wine-quality/winequality-white.csv" \
		--output-dir "data/raw"

# script 02 - clean and merge data
data/processed/wine_cleaned.csv: scripts/02_clean_data.py data/raw/winequality-red.csv data/raw/winequality-white.csv
	mkdir -p data/processed
	python scripts/02_clean_data.py \
		--red-input "data/raw/winequality-red.csv" \
		--white-input "data/raw/winequality-white.csv" \
		--output-file "data/processed/wine_cleaned.csv"

# script 03 - split data
data/processed/train.csv data/processed/test.csv: scripts/03_split_data.py data/processed/wine_cleaned.csv
	python scripts/03_split_data.py \
		--input-file "data/processed/wine_cleaned.csv" \
		--train-output "data/processed/train.csv" \
		--test-output "data/processed/test.csv"

# script 00 - validate data (runs after split; checks both cleaned and split data)
results/validation_report.txt: scripts/00_validate_data.py data/processed/wine_cleaned.csv data/processed/train.csv data/processed/test.csv
	mkdir -p results
	python scripts/00_validate_data.py \
		--cleaned-data "data/processed/wine_cleaned.csv" \
		--train-data "data/processed/train.csv" \
		--test-data "data/processed/test.csv" \
		| tee results/validation_report.txt

# script 04 - generate EDA figures (depends on validation passing)
results/figures/quality_distribution.png: scripts/04_eda_visuals.py data/processed/train.csv results/validation_report.txt
	mkdir -p results/figures
	python scripts/04_eda_visuals.py \
		--input-file "data/processed/train.csv" \
		--output-dir "results/figures"

# script 05 - run model analysis (depends on validation passing)
results/metrics.txt results/figures/confusion_matrix.png: data/processed/wine_cleaned.csv data/processed/train.csv data/processed/test.csv scripts/05_model_analysis.py results/validation_report.txt
	python scripts/05_model_analysis.py \
		--df-input "data/processed/wine_cleaned.csv" \
		--train-input "data/processed/train.csv" \
		--test-input "data/processed/test.csv" \
		--metrics-output "results/metrics.txt" \
		--plot-output="results/figures/confusion_matrix.png"

reports/wine-quality-classification.html: reports/wine-quality-classification.qmd \
                                          results/figures/quality_distribution.png \
                                          results/metrics.txt
	quarto render reports/wine-quality-classification.qmd

# clean
clean:
	rm -rf data
	rm -rf results
