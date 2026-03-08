# Wine Quality Analysis

## Contributors

1. Siluni Jayarathne
2. Alexis Widjaja
3. Sungha Choi
4. Karen Siem

## Project Summary

Our goal of the project is to classify the quality of the wine as a number between 0 and 10 depending on chemical properties such as fixed acidity, volatile acidity, citric acid, residual sugar,chlorides, free sulfur dioxide, total sulfur dioxide, density, pH and sulphates.

We will be using the Wine Quality dataset (Cortez et al., 2009) on the UC Irvine Machine Learning Repository. There are 13 variables and 4898 records. There are no missing values.

We will be building a kNN classification model on chemical attributes of wine from the dataset.

## how to run the data analysis

Using supervised machine learning classification models (Pedregosa et al., 2011), we analyze how chemical characteristics influence perceived wine quality and evaluate model performance using standard classification metrics.

The analysis follows these steps:

1. Data loading and cleaning
2. Exploratory data analysis (EDA)
3. Model training (classification algorithms)
4. Model evaluation and comparison
5. Results visualization

## Dependencies

    pandas==2.2.2   
    numpy==1.26.4 
    scikit-learn==1.4.2 
    matplotlib==3.8.4 
    seaborn==0.13.2
    jinja2==3.1.2 
    requests==2.31.0

## Results

Our kNN model classifying the wine quality score using the chemical property variables had an accuracy of 55% and a weighted F1 score of 54%. The results indicate that the kNN model can reasonably predict the most common wine quality scores, but struggles with rare scores such as 3, 8, and 9. This suggests that additional data or alternative models might improve performance for extreme quality levels.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE.md) file for details.
