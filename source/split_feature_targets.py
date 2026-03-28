import pandas as pd
import os

def split_features_target(df: pd.DataFrame, target_col: str):
    """
    Split a pandas DataFrame into features and target components.
    
    Parameters
    ----------
    df : pandas.DataFrame
        The input DataFrame containing both features and the target column.
    target_col : str
        The name of the column in df to use as the target (y).
    
    Returns
    -------
    dict
        Dictionary with keys 'X' (features) and 'y' (target).
    
    Raises
    ------
    ValueError
        If target_col is not a column in df.
    """
    if target_col not in df.columns:
        raise ValueError(f"Target column '{target_col}' not found in DataFrame.")
    X = df.drop(columns=[target_col])
    y = df[target_col]
    return X, y
