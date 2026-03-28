import pandas as pd
from pathlib import Path
import os


def load_csv_from_url(url, sep=";"):
    """Load a CSV dataset from a URL."""
    validate_string(url, "url")
    
    try:
        df = pd.read_csv(url, sep=sep)
    except Exception as e:
        raise ValueError(f"Could not load data from {url}: {e}")
    
    return df


def save_dataframe(df, file_path):
    """Save a DataFrame to a CSV file."""
    if isinstance(file_path, Path):
        file_path = str(file_path)

    # Now validate
    validate_string(file_path, "file_path")

    df.to_csv(file_path, index=False)
    return file_path


# utility functions
def validate_string(value, name):
    """Validate that a value is a string."""
    if not isinstance(value, str) or value.strip() == "":
        raise ValueError(f"{name} must be a non-empty string.")


def create_directory(path):
    """Create a directory if it does not exist."""
    validate_string(path, "output_dir")
    os.makedirs(path, exist_ok=True)
    return path


def load_csv_from_url(url, sep=";"):
    """Load a CSV dataset from a URL."""
    validate_string(url, "url")
    
    try:
        df = pd.read_csv(url, sep=sep)
    except Exception as e:
        raise ValueError(f"Could not load data from {url}: {e}")
    
    return df


def save_dataframe(df, file_path):
    """Save a DataFrame to a CSV file."""
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas DataFrame.")
    
    validate_string(file_path, "file_path")

    df.to_csv(file_path, index=False)
    return file_path