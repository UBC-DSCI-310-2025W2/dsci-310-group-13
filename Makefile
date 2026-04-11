# authors: Group 13

.PHONY: all clean

export PYTHONPATH := $(shell pwd)

all: data/raw/winequality-red.csv \
    data/processed/wine_cleaned.csv \
    data/processed/wine_validated.csv \
    data/processed/train.csv \
    data/processed/test.csv \
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

# script 02 - clean data
data/processed/wine_cleaned.csv: scripts/02_clean_data.py \
                                  data/raw/winequality-red.csv \
                                  data/raw/winequality-white.csv
	mkdir -p data/processed
	python scripts/02_clean_data.py \
		--red-input "data/raw/winequality-red.csv" \
		--white-input "data/raw/winequality-white.csv" \
		--output-file "data/processed/wine_cleaned.csv"

# script 06 - validate data
data/processed/wine_validated.csv: scripts/06_validate_data.py \
                                    data/processed/wine_cleaned.csv
	python scripts/06_validate_data.py \
		--input-file "data/processed/wine_cleaned.csv" \
		--output-file "data/processed/wine_validated.csv"

# script 03 - split data
data/processed/train.csv data/processed/test.csv: scripts/03_split_data.py \
                                                   data/processed/wine_validated.csv
	python scripts/03_split_data.py \
		--input-file "data/processed/wine_validated.csv" \
		--train-output "data/processed/train.csv" \
		--test-output "data/processed/test.csv"

# script 04 - generate EDA figures
results/figures/quality_distribution.png: scripts/04_eda_visuals.py \
                                           data/processed/train.csv
	mkdir -p results/figures
	python scripts/04_eda_visuals.py \
		--input-file "data/processed/train.csv" \
		--output-dir "results/figures"

# script 05 - run model analysis
results/metrics.txt results/figures/confusion_matrix.png: scripts/05_model_analysis.py \
        data/processed/wine_validated.csv \
        data/processed/train.csv \
        data/processed/test.csv
	python scripts/05_model_analysis.py \
		--df-input "data/processed/wine_validated.csv" \
		--train-input "data/processed/train.csv" \
		--test-input "data/processed/test.csv" \
		--metrics-output "results/metrics.txt" \
		--plot-output "results/figures/confusion_matrix.png"

# report
reports/wine-quality-classification.html: reports/wine-quality-classification.qmd \
                                          results/figures/quality_distribution.png \
                                          results/figures/confusion_matrix.png \
                                          results/metrics.txt
	quarto render reports/wine-quality-classification.qmd

# clean
clean:
	rm -rf data
	rm -rf results