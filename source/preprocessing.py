import click
import pandas as pd
import os
from sklearn.preprocessing import OneHotEncoder, StandardScaler
from sklearn.compose import make_column_transformer
import pandas.api.types as pd_types

def build_preprocessor(df, categorical_cols, numeric_cols):
    """
    Build a preprocessing transformer for numeric and categorical columns.

    Parameters
    ----------
    df : pandas.DataFrame
        The dataframe containing the columns to check.
    categorical_cols : list of str
        List of categorical column names to one-hot encode.
    numeric_cols : list of str
        List of numeric column names to standardize.

    Returns
    -------
    sklearn.compose.ColumnTransformer
        A transformer pipeline that:
        - Applies StandardScaler to numeric columns
        - Applies OneHotEncoder(drop='if_binary') to categorical columns

    Raises
    ------
    ValueError
        - If both `numeric_cols` and `categorical_cols` are empty
        - If specified columns don't exist in `df`
        - If numeric columns contain non-numeric data
        
    Warnings
    --------
    Prints warning if categorical columns contain numeric data
    (suggests moving them to numeric_cols).
    
    Examples
    --------
    >>> import pandas as pd
    >>> df = pd.DataFrame({'age': [25, 30], 'city': ['A', 'B']})
    >>> preprocessor = build_preprocessor(df, ['city'], ['age'])
    >>> X_transformed = preprocessor.fit_transform(df)
    """
    
    if not numeric_cols and not categorical_cols:
        raise ValueError("At least one non-empty column must be provided.")

    # Check that all provided columns exist in df
    missing_cols = [col for col in numeric_cols + categorical_cols if col not in df.columns]
    if missing_cols:
        raise ValueError(f"Columns not found in dataframe: {missing_cols}")

    # Validate numeric columns contain only numeric data (ERROR if not)
    for col in numeric_cols:
        if not pd.api.types.is_numeric_dtype(df[col]):
            raise ValueError(f"Non-numeric values found in numeric column '{col}'")

    # Warn about numeric data in categorical columns (can still proceed)
    for col in categorical_cols:
        if pd.api.types.is_numeric_dtype(df[col]):
            print(
                f"WARNING: Numeric data detected in categorical column '{col}'. "
                f"Consider moving it to numeric_cols."
            )

    # Build and return column transformer
    transformer = make_column_transformer(
        (StandardScaler(), numeric_cols),
        (OneHotEncoder(drop="if_binary"), categorical_cols))

    return transformer
