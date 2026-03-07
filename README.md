# Wine Quality Analysis

## Contributors

1. Siluni Jayarathne
2. Alexis Widjaja
3. Sungha Choi
4. Karen Siem

## Project Summary

Our goal of the project is to classify the quality of the wine as a number between 0 and 10 depending on chemical properties such as fixed acidity, volatile acidity, citric acid, residual sugar,chlorides, free sulfur dioxide, total sulfur dioxide, density, pH and sulphates.

We will be using the Wine Quality dataset (Cortez et al., 2009) on the UC Irvine Machine Learning Repository. There are 13 variables related to chemical properties of red and white wine and 4898 records. The two datasets ( for Red and White wine) were merged for the analysis. There are no missing values in the data.

We will perform exploratory data analysis on the data to identify patterns and correlations in the data and build a kNN classification model to classify the numerical wine quality score (1-10).

## how to run the data analysis

Using supervised machine learning classification models, we analyze how chemical characteristics influence perceived wine quality and evaluate model performance using standard classification metrics.

The analysis follows these steps:

1. Data loading and cleaning
2. Exploratory data analysis (EDA)
3. Model training (classification algorithms)
4. Model evaluation and comparison
5. Results and Discussion

## Dependencies

pandas==2.2.2 \
    numpy==1.26.4 \
    scikit-learn==1.4.2 \
    matplotlib==3.8.4 \
    seaborn==0.13.2\
    jinja2==3.1.2 \
    requests==2.31.0

## Results

The kNN model built on the chemical attributes of wine to predict the quality score resulted in a weighted F1 score of 0.54 and an accuracy of 0.55. The model performed best at predicting wines with quality scores of 5 and 6, which were the most frequent in the dataset. Lower and higher quality wines were predicted less accurately, likely due to fewer examples in the training set.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
