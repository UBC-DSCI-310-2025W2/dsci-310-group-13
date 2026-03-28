import pandas as pd


def clean_data(red_input, white_input, output_file):
    """
    Clean and merge wine datasets.

    Returns:
        pd.DataFrame: cleaned combined dataset
    """

    # load
    red = load_csv(red_input)
    white = load_csv(white_input)

    # clean columns
    red = clean_column_names(red)
    white = clean_column_names(white)

    # add labels
    red = add_wine_type(red, "red")
    white = add_wine_type(white, "white")

    # merge
    combined = merge_datasets(red, white)

    # save
    save_csv(combined, output_file)

    return combined

# helper functions

def load_csv(file_path):
    """Load a CSV file into a DataFrame."""
    if not isinstance(file_path, str) or file_path.strip() == "":
        raise ValueError("file_path must be a non-empty string.")

    try:
        df = pd.read_csv(file_path)
    except Exception as e:
        raise ValueError(f"Could not read file {file_path}: {e}")

    return df


def clean_column_names(df):
    """Standardize column names: lowercase, strip, replace spaces with underscores."""
    if not isinstance(df, pd.DataFrame):
        raise ValueError("Input must be a pandas DataFrame.")

    df = df.copy()
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    return df


def add_wine_type(df, wine_type):
    """Add a wine_type column to the DataFrame."""
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas DataFrame.")
    if wine_type not in ["red", "white"]:
        raise ValueError("wine_type must be 'red' or 'white'.")

    df = df.copy()
    df["wine_type"] = wine_type
    return df


def merge_datasets(df1, df2):
    """Merge two DataFrames."""
    if not all(isinstance(df, pd.DataFrame) for df in [df1, df2]):
        raise ValueError("Both inputs must be pandas DataFrames.")

    return pd.concat([df1, df2], ignore_index=True)


def save_csv(df, output_path):
    """Save a DataFrame to a CSV file."""
    if not isinstance(df, pd.DataFrame):
        raise ValueError("df must be a pandas DataFrame.")
    if not isinstance(output_path, str) or output_path.strip() == "":
        raise ValueError("output_path must be a non-empty string.")

    df.to_csv(output_path, index=False)
    return output_path