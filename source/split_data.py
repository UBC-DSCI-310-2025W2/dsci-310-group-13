import pandas as pd
from sklearn.model_selection import train_test_split


def load_data(filepath):
    """
    Load dataset from a CSV file.

    Parameters
    ----------
    filepath : str

    Returns
    -------
    pandas.DataFrame
    """
    return pd.read_csv(filepath)


def stratified_split(df, target_col, test_size=0.3, random_state=42):
    """
    Perform stratified train-test split.

    Parameters
    ----------
    df : pandas.DataFrame
    target_col : str
    test_size : float
    random_state : int

    Returns
    -------
    (train_df, test_df)
    """
    if target_col not in df.columns:
        raise KeyError(f"{target_col} not found in dataframe")

    train, test = train_test_split(
        df,
        test_size=test_size,
        random_state=random_state,
        stratify=df[target_col]
    )

    return train, test


def save_data(df, filepath):
    """
    Save DataFrame to CSV.

    Parameters
    ----------
    df : pandas.DataFrame
    filepath : str
    """
    df.to_csv(filepath, index=False)