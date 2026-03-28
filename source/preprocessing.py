from sklearn.metrics import accuracy_score, classification_report, confusion_matrix, ConfusionMatrixDisplay

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

def split_features_target(df: pd.DataFrame, target_col: str):
    """Split a DataFrame into features X and target y."""
    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found in DataFrame.")
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y


def build_preprocessor(categorical_cols, numeric_cols):
    """Build a column transformer for numeric scaling and categorical encoding."""
    if not numeric_cols and not categorical_cols:
        raise ValueError("At least one numeric or categorical column must be provided.")
    return make_column_transformer(
        (StandardScaler(), numeric_cols),
        (OneHotEncoder(drop="if_binary"), categorical_cols),
    )


def build_pipeline(preprocessor, n_neighbors: int = 5):
    """Create a pipeline with a preprocessor and KNN classifier."""
    if not isinstance(n_neighbors, int) or n_neighbors <= 0:
        raise ValueError("n_neighbors must be a positive integer.")
    return Pipeline(
        [
            ("preprocessor", preprocessor),
            ("knn", KNeighborsClassifier(n_neighbors=n_neighbors)),
        ]
    )


def train_and_predict(model, X_train, y_train, X_test):
    """Fit the model on training data and return predictions for X_test."""
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    return y_pred


def evaluate_predictions(y_test, y_pred):
    """Compute accuracy, text report, and confusion-matrix display."""
    if len(y_test) == 0:
        raise ValueError("y_test must not be empty.")
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred)
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm)
    return accuracy, report, disp


def save_confusion_matrix_plot(disp, plot_output: str):
    """Save confusion matrix plot to the given path."""
    os.makedirs(os.path.dirname(plot_output), exist_ok=True)
    fig, ax = plt.subplots(figsize=(10, 8))
    disp.plot(cmap="Blues", ax=ax)
    plt.title("Confusion Matrix of Wine Quality Predictions")
    plt.savefig(plot_output)
    plt.close(fig)


def save_metrics(accuracy: float, report: str, metrics_output: str):
    """Save accuracy and classification report to a text file."""
    os.makedirs(os.path.dirname(metrics_output), exist_ok=True)
    with open(metrics_output, "w") as f:
        f.write(f"Accuracy: {accuracy}\n\n")
        f.write(report)
