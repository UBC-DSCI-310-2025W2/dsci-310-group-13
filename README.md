# Wine Quality Classification

## Contributors

- Siluni Jayarathne  
- Alexis Widjaja  
- Sungha Choi  
- Karen Siem  

This project investigates how physicochemical properties of wine relate to perceived quality. Using supervised machine learning techniques, we develop a classification model to predict wine quality scores on a scale from 0 to 10.

The dataset consists of red and white variants of Portuguese "Vinho Verde" wine and includes measurements such as acidity, sugar content, sulfur dioxide levels, and alcohol content.

## Research Objective

The primary objective of this study is:

> **Can we accurately predict wine quality based on its chemical properties?**

To address this question, we implemented and evaluated a **k-Nearest Neighbors (kNN)** classification model and analyzed its performance across different quality levels.

## Dataset

- Source: UCI Machine Learning Repository  
- Dataset: *Wine Quality Dataset* (Cortez et al., 2009)  
- Observations: **4,898**  
- Features: **13** (12 predictors + 1 target variable)  
- Missing values: **None**

### Features include

- Fixed acidity  
- Volatile acidity  
- Citric acid  
- Residual sugar  
- Chlorides  
- Free sulfur dioxide  
- Total sulfur dioxide  
- Density  
- pH  
- Sulphates  
- Alcohol  
- Wine type (categorical: red/white)  

Target variable:

- **Quality score (integer: 0–10)**

## Methodology

The analysis follows a structured machine learning pipeline:

1. **Data Collection & Cleaning**

We began by combining the red and white wine datasets to increase the overall sample size and capture a wider range of wine characteristics. Standardizing column names ensured consistency and prevented downstream processing errors. We also introduced a wine_type variable to preserve meaningful categorical information that may influence wine quality. This step ensures the dataset is clean, structured, and ready for analysis.

   - Loaded datasets from UCI repository
   - Standardized column names
   - Merged red and white datasets
   - Added categorical feature: `wine_type`

2. **Exploratory Data Analysis (EDA)**

Exploratory Data Analysis (EDA) was conducted to understand the structure and distribution of the data prior to modeling. We examined feature distributions and relationships between variables to identify patterns and potential predictors of wine quality. In particular, we observed class imbalance in the quality scores, which informed our decision to use evaluation metrics beyond simple accuracy. EDA also helped verify data integrity and guided preprocessing choices.

   - Examined feature distributions
   - Identified class imbalance in quality scores
   - Analyzed relationships between variables

3. **Preprocessing**

Preprocessing was a critical step to ensure the data was suitable for modeling, particularly because kNN relies on distance-based calculations. Numerical features were standardized so that all variables contribute equally to distance computations, preventing features with larger magnitudes from dominating the model. The categorical variable wine_type was encoded to convert it into a numerical format while preserving its structure. These transformations were combined into a single pipeline to ensure consistent and reproducible preprocessing across both training and testing data.

   - Numerical features scaled using `StandardScaler`
   - Categorical variable encoded using `OneHotEncoder`
   - Combined using a `ColumnTransformer`

4. **Model Development**

We selected k-Nearest Neighbors (kNN) as our classification model due to its simplicity, interpretability, and minimal assumptions about the data distribution. As a non-parametric method, kNN allows us to model complex relationships without specifying a functional form. It is particularly suitable for this task, as it tests the assumption that wines with similar chemical properties will have similar quality scores. We performed hyperparameter tuning using cross-validation to identify the optimal number of neighbors, balancing model bias and variance while improving generalization performance.

   - Model: k-Nearest Neighbors (kNN)
   - Hyperparameter tuning using `GridSearchCV`
   - Cross-validation: **5-fold StratifiedKFold**
   - Tuned parameter: `n_neighbors`

5. **Model Evaluation**

Model evaluation was conducted using multiple metrics to provide a comprehensive assessment of performance. While accuracy offers a general measure of correctness, it can be misleading in the presence of class imbalance. Therefore, we focused on precision, recall, and the weighted F1-score to better capture performance across all quality levels. Additionally, the confusion matrix was used to analyze specific misclassification patterns, particularly for underrepresented classes. This approach ensures that model performance is evaluated in a way that reflects both overall accuracy and class-specific behavior.

   - Metrics:
     - Accuracy
     - Precision, Recall, F1-score
     - Confusion Matrix
   - Focus on **weighted F1-score** due to class imbalance

## Results

- **Accuracy:** 0.55  
- **Weighted F1-score:** 0.54  

### Key Findings

- The model performs best on **quality scores 5 and 6**, which dominate the dataset.
- Performance is significantly lower for **rare classes** (e.g., 3, 8, 9).
- This indicates a strong effect of **class imbalance** on model performance.

### Interpretation

While the model captures general trends in the data, it struggles to generalize to underrepresented classes. This suggests that:

- Additional data collection may improve performance  
- Alternative models (e.g., Random Forest, Gradient Boosting) could yield better results  
- Techniques such as **resampling or class weighting** may help address imbalance  

## Project Structure

Before running `make all` :

```
.
├── .github/workflows/
│ 
├── data/
│    ├── raw/
│        └── .gitkeep 
│    └── processed/
│        └── .gitkeep
│ 
├── results/
│    ├── figures/
│         └── .gitkeep
│
├── scripts/
│    ├── 01_download_data.py/
│    ├── 02_clean_data.py/
│    ├── 03_split_data.py/
│    ├── 04_eda_visuals.py/
│    └── 05_model_analysis.py/
│
├── reports/
│    ├── references.bib
│    ├── wine-quality-classification.html
│    ├── wine-quality-classification.ipynb
│    └── wine-quality-classification.qmd
│
├── .dockerignore
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE.md
├── Makefile
├── README.md
├── requirements.txt
└── docker-compose.yml
```

After running `make all` :

```
.
├── .github/workflows/
│ 
├── data/
│    ├── raw/
│        ├── winequality-red.csv
│        ├── winequality-white.csv
│        └── .gitkeep 
│    └── processed/
│        ├── test.csv
│        ├── train.csv
│        ├── wine_cleaned.csv
│        └── .gitkeep
│ 
├── results/
│    ├── figures/
│        ├── confusion_matrix.png
│        ├── correlation_heatmap.png
│        ├── feature_distributions.png
│        ├── key_feature_vs_quality.png
│        ├── quality_distribution.png
│        ├── summary_statistics.csv
│        └── .gitkeep
│    └── metrics.txt
│
├── scripts/
│    ├── 01_download_data.py/
│    ├── 02_clean_data.py/
│    ├── 03_split_data.py/
│    ├── 04_eda_visuals.py/
│    └── 05_model_analysis.py/
│
├── reports/
│    ├── references.bib
│    ├── wine-quality-classification.html
│    ├── wine-quality-classification.ipynb
│    └── wine-quality-classification.qmd
│
├── .dockerignore
├── .gitignore
├── CODE_OF_CONDUCT.md
├── CONTRIBUTING.md
├── Dockerfile
├── LICENSE.md
├── Makefile
├── README.md
├── requirements.txt
└── docker-compose.yml
```

## Dependencies

    pandas==2.2.2   
    numpy==1.26.4 
    scikit-learn==1.4.2 
    matplotlib==3.8.4 
    seaborn==0.13.2
    jinja2==3.1.2 
    requests==2.31.0

## Run the project

### 1. Clone Repository
Clone the repistory and go to its root directory in the terminal by pasting on the terminal: 
```bash
git clone https://github.com/UBC-DSCI-310-2025W2/dsci-310-group-13.git
cd dsci-310-group-13
```
### 2. Build the image:

```bash
# Build the image
docker build -t wine-analysis .
```

### 3. Run the container:

```bash
# Run the container
docker run -p 8888:8888 -v $(pwd):/home/jovyan/work wine-analysis
```

### 4. Open the link to access local Jupyter Lab:

After running the container, open:

http://localhost:8888

If a token is required, copy it from the terminal output and paste it into the browser.

NOTE: It will appear the format of token=<token>

### Without Docker (optional)

Local Environment

### 1. Install dependencies:

```bash
pip install -r requirements.txt
```

### 2. Make file:

Run the Script to Download Data, Process Data, Generate Results and Render Report:

```bash
make all
```

### 3. Clean Makefile:

Reset the Project to its Original State:

```bash
make clean
```

## How to run tests

### 1. Go to the tests directory

```bash
cd tests
```

### 2. run:

### All tests: 
```bash
pytest tests/ -v
```
### Specific tests:
```bash
pytest <name of the test file> -v
```


## Reproducibility

All experiments are reproducible using the provided code and Docker environment.
Random states are controlled where applicable.
Data is sourced directly from a public repository.

## Results

Our kNN model classifying the wine quality score using the chemical property variables had an accuracy of 55% and a weighted F1 score of 54%. The results indicate that the kNN model can reasonably predict the most common wine quality scores, but struggles with rare scores such as 3, 8, and 9. This suggests that additional data or alternative models might improve performance for extreme quality levels.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
