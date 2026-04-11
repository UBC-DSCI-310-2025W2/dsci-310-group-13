"""Data validation script for the wine quality analysis pipeline.

Runs structural and domain checks on the cleaned dataset and train/test split.
Exits with code 1 if any checks fail, stopping the pipeline.
"""
import click
import pandas as pd
import sys


EXPECTED_COLUMNS = [
    "fixed_acidity", "volatile_acidity", "citric_acid",
    "residual_sugar", "chlorides", "free_sulfur_dioxide",
    "total_sulfur_dioxide", "density", "ph", "sulphates",
    "alcohol", "quality", "wine_type",
]

NUMERIC_COLUMNS = [
    "fixed_acidity", "volatile_acidity", "citric_acid",
    "residual_sugar", "chlorides", "free_sulfur_dioxide",
    "total_sulfur_dioxide", "density", "ph", "sulphates",
    "alcohol", "quality",
]

NON_NEGATIVE_COLUMNS = [
    "fixed_acidity", "citric_acid", "residual_sugar",
    "chlorides", "free_sulfur_dioxide", "total_sulfur_dioxide",
    "density", "sulphates", "alcohol",
]

COLUMN_RANGES = {
    "quality":  (3, 9),
    "alcohol":  (8.0, 15.0),
    "ph":       (2.5, 4.5),
    "density":  (0.98, 1.04),
}

VALID_WINE_TYPES = {"red", "white"}


def validate_cleaned_data(df: pd.DataFrame) -> list:
    """Run structural and domain checks on the cleaned merged dataset."""
    errors = []

    if df.empty:
        errors.append("FAIL [Check 1]: Dataset is empty.")
    else:
        print("PASS [Check 1]: Dataset is not empty.")

    missing_cols = [c for c in EXPECTED_COLUMNS if c not in df.columns]
    if missing_cols:
        errors.append(f"FAIL [Check 2]: Missing expected columns: {missing_cols}")
    else:
        print("PASS [Check 2]: All expected columns are present.")

    non_numeric = [
        c for c in NUMERIC_COLUMNS
        if c in df.columns and not pd.api.types.is_numeric_dtype(df[c])
    ]
    if non_numeric:
        errors.append(f"FAIL [Check 3]: Non-numeric dtype in numeric columns: {non_numeric}")
    else:
        print("PASS [Check 3]: All numeric columns have correct dtypes.")

    key_cols = [c for c in EXPECTED_COLUMNS if c in df.columns]
    null_counts = df[key_cols].isnull().sum()
    cols_with_nulls = null_counts[null_counts > 0].index.tolist()
    if cols_with_nulls:
        errors.append(f"FAIL [Check 4]: Missing values found in columns: {cols_with_nulls}")
    else:
        print("PASS [Check 4]: No missing values in key columns.")

    n_dups = df.duplicated().sum()
    if n_dups > 0:
        errors.append(f"FAIL [Check 5]: {n_dups} duplicate rows found.")
    else:
        print("PASS [Check 5]: No duplicate rows detected.")

    if "wine_type" in df.columns:
        invalid_types = set(df["wine_type"].dropna().unique()) - VALID_WINE_TYPES
        if invalid_types:
            errors.append(f"FAIL [Check 6]: Invalid wine_type values: {invalid_types}")
        else:
            print("PASS [Check 6]: wine_type contains only 'red' and 'white'.")

    for col, (lo, hi) in COLUMN_RANGES.items():
        if col in df.columns:
            out_of_range = df[(df[col] < lo) | (df[col] > hi)]
            if len(out_of_range) > 0:
                errors.append(f"FAIL [Check 7]: {len(out_of_range)} rows in '{col}' outside [{lo}, {hi}].")
            else:
                print(f"PASS [Check 7]: '{col}' values within [{lo}, {hi}].")

    for col in NON_NEGATIVE_COLUMNS:
        if col in df.columns:
            n_neg = (df[col] < 0).sum()
            if n_neg > 0:
                errors.append(f"FAIL [Check 8]: {n_neg} negative values in '{col}'.")
            else:
                print(f"PASS [Check 8]: No negative values in '{col}'.")

    return errors


def validate_split(train_df: pd.DataFrame, test_df: pd.DataFrame,
                   cleaned_df: pd.DataFrame) -> list:
    """Validate that the train/test split is correct and free of data leakage."""
    errors = []

    merged = train_df.reset_index(drop=True).merge(test_df.reset_index(drop=True), how="inner")
    if len(merged) > 0:
        errors.append(f"FAIL [Check 9]: {len(merged)} rows appear in both train and test — data leakage.")
    else:
        print("PASS [Check 9]: No row overlap between training and test sets.")

    split_total = len(train_df) + len(test_df)
    if split_total != len(cleaned_df):
        errors.append(f"FAIL [Check 10]: Train+Test={split_total} does not equal cleaned rows ({len(cleaned_df)}).")
    else:
        print(f"PASS [Check 10]: Train ({len(train_df)}) + Test ({len(test_df)}) = {split_total} matches total.")

    for name, df in [("train", train_df), ("test", test_df)]:
        if "quality" not in df.columns:
            errors.append(f"FAIL [Check 11]: 'quality' column missing from {name} set.")
        else:
            print(f"PASS [Check 11]: 'quality' column present in {name} set.")

    if "quality" in train_df.columns and "quality" in test_df.columns:
        missing_in_test = set(train_df["quality"].unique()) - set(test_df["quality"].unique())
        if missing_in_test:
            errors.append(f"FAIL [Check 12]: Quality classes in train but not test: {missing_in_test}.")
        else:
            print("PASS [Check 12]: All quality classes in both train and test sets.")

    return errors


@click.command()
@click.option('--cleaned-data', type=str, required=True, help="Path to cleaned dataset CSV")
@click.option('--train-data', type=str, required=True, help="Path to training set CSV")
@click.option('--test-data', type=str, required=True, help="Path to testing set CSV")
def validate(cleaned_data, train_data, test_data):
    """Run 12 data validation checks. Exits with code 1 if any fail."""
    print("=" * 60)
    print("DATA VALIDATION REPORT")
    print("=" * 60)

    cleaned_df = pd.read_csv(cleaned_data)
    train_df = pd.read_csv(train_data)
    test_df = pd.read_csv(test_data)

    print(f"\nCleaned: {len(cleaned_df):,} rows | Train: {len(train_df):,} rows | Test: {len(test_df):,} rows\n")

    errors = validate_cleaned_data(cleaned_df)
    errors += validate_split(train_df, test_df, cleaned_df)

    print("\n" + "=" * 60)
    if errors:
        print(f"VALIDATION FAILED: {len(errors)} check(s) did not pass.\n")
        for err in errors:
            print(f"  {err}")
        sys.exit(1)
    else:
        print("ALL 12 VALIDATION CHECKS PASSED.")
    print("=" * 60)


if __name__ == "__main__":
    validate()