import click
import pandas as pd
import os
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline
from sklearn.compose import make_column_transformer
from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from source.preprocessing import build_preprocessor

@click.command()
@click.option('--df-input', type=str, required=True,
              help="Path to cleaned dataset")
@click.option('--train-input', type=str, required=True,
              help="Path to training dataset")
@click.option('--test-input', type=str, required=True,
              help="Path to testing dataset")
@click.option('--metrics-output', type=str, required=True,
              help="Path to save evaluation metrics")
@click.option('--plot-output', type=str, required=True, 
              help="Path to save confusion matrix plot")
              
def model_analysis(df_input, train_input, test_input, metrics_output, plot_output):
    """
    Train and evaluate a kNN classifier for wine quality prediction.
    """

    # load data
    df = pd.read_csv(df_input)
    train = pd.read_csv(train_input)
    test = pd.read_csv(test_input)

    # split features and target
    X_train = train.drop(columns=["quality"])
    y_train = train["quality"]

    X_test = test.drop(columns=["quality"])
    y_test = test["quality"]
    
    # Preprocessor
    categorical_variable = ["wine_type"]
    numerical_variable = ["fixed_acidity",
                        "volatile_acidity", 
                        "citric_acid",
                        "residual_sugar",
                        "chlorides", 
                        "free_sulfur_dioxide", 
                        "total_sulfur_dioxide", 
                        "density", 
                        "ph", 
                        "sulphates",
                        "alcohol"]
                        
    preprocessor = build_preprocessor(df, categorical_variable, numerical_variable)
        
    # pipeline: scaling + KNN
    model = Pipeline([
        ("preprocessor", preprocessor),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ])

    # train model
    model.fit(X_train, y_train)

    # predictions
    y_pred = model.predict(X_test)

    # evaluation
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, zero_division=0)

    # Create and Save Confusion Matrix
    cm = confusion_matrix(y_test, y_pred, labels=model.classes_)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    
    fig, ax = plt.subplots(figsize=(10, 8))
    disp.plot(cmap='Blues', ax=ax)
    plt.title("Confusion Matrix of Wine Quality Predictions")
    
    # Ensure the directory exists
    os.makedirs(os.path.dirname(plot_output), exist_ok=True)
    plt.savefig(plot_output)
    plt.close()

    # save results (existing code)
    with open(metrics_output, "w") as f:
        f.write(f"Accuracy: {accuracy}\n\n")
        f.write(report)


if __name__ == "__main__":
    model_analysis()
