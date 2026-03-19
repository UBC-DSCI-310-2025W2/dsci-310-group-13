import click
import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score, classification_report
from sklearn.pipeline import Pipeline


@click.command()
@click.option('--train-input', type=str, required=True,
              help="Path to training dataset")
@click.option('--test-input', type=str, required=True,
              help="Path to testing dataset")
@click.option('--metrics-output', type=str, required=True,
              help="Path to save evaluation metrics")
def model_analysis(train_input, test_input, metrics_output):
    """
    Train and evaluate a kNN classifier for wine quality prediction.
    """

    # load data
    train = pd.read_csv(train_input)
    test = pd.read_csv(test_input)

    # split features and target
    X_train = train.drop(columns=["quality"])
    y_train = train["quality"]

    X_test = test.drop(columns=["quality"])
    y_test = test["quality"]

    # pipeline: scaling + KNN
    model = Pipeline([
        ("scaler", StandardScaler()),
        ("knn", KNeighborsClassifier(n_neighbors=5))
    ])

    # train model
    model.fit(X_train, y_train)

    # predictions
    y_pred = model.predict(X_test)

    # evaluation
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)

    # save results
    with open(metrics_output, "w") as f:
        f.write(f"Accuracy: {accuracy}\n\n")
        f.write(report)

    print(f"Model evaluation saved to {metrics_output}")


if __name__ == "__main__":
    model_analysis()