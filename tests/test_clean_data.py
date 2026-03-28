import pytest
import pandas as pd
from source.clean_data import clean_column_names, add_wine_type, merge_datasets


# clean_column_names

def test_clean_column_names_simple():
    """Simple case: columns with spaces and capitals are standardized."""
    df = pd.DataFrame(columns=["Fixed Acidity", "pH"])
    cleaned = clean_column_names(df)
    
    assert list(cleaned.columns) == ["fixed_acidity", "ph"]


def test_clean_column_names_edge():
    """Edge case: columns already clean should stay the same."""
    df = pd.DataFrame(columns=["fixed_acidity", "pH"])
    cleaned = clean_column_names(df)
    
    assert list(cleaned.columns) == ["fixed_acidity", "ph"]


def test_clean_column_names_error():
    """Error case: input is not a DataFrame."""
    with pytest.raises(ValueError):
        clean_column_names("not_a_df")


# -----------------------------
# add_wine_type
# -----------------------------

def test_add_wine_type_simple():
    """Simple case: adds 'red' label to dataframe."""
    df = pd.DataFrame({"a": [1, 2]})
    labeled = add_wine_type(df, "red")
    assert "wine_type" in labeled.columns
    assert all(labeled["wine_type"] == "red")


def test_add_wine_type_edge():
    """Edge case: empty DataFrame still adds wine_type column."""
    df = pd.DataFrame()
    labeled = add_wine_type(df, "white")
    assert "wine_type" in labeled.columns
    assert labeled.empty or all(labeled["wine_type"] == "white")


def test_add_wine_type_error():
    """Error case: invalid wine_type string."""
    df = pd.DataFrame({"a": [1]})
    with pytest.raises(ValueError):
        add_wine_type(df, "rose")  # invalid type


# merge_datasets

def test_merge_datasets_simple():
    """Simple case: merges two small DataFrames."""
    df1 = pd.DataFrame({"a": [1, 2]})
    df2 = pd.DataFrame({"a": [3, 4]})
    merged = merge_datasets(df1, df2)
    assert merged.shape[0] == 4
    assert list(merged["a"]) == [1, 2, 3, 4]


def test_merge_datasets_edge():
    """Edge case: one empty DataFrame merged with a non-empty DataFrame."""
    df1 = pd.DataFrame()
    df2 = pd.DataFrame({"a": [1, 2]})
    merged = merge_datasets(df1, df2)
    assert merged.shape[0] == 2
    assert list(merged["a"]) == [1, 2]


def test_merge_datasets_error():
    """Error case: input is not a DataFrame."""
    with pytest.raises(ValueError):
        merge_datasets("not_a_df", pd.DataFrame({"a": [1]}))