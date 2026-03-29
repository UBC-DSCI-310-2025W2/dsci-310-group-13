import pandas as pd
from pandas.errors import EmptyDataError
from pathlib import Path



def clean_data(red_input, white_input, output_file):
    """
    Load, clean, merge, and save wine datasets.

    Parameters
    ----------
    red_input : str or Path
        Path to red wine CSV file
    white_input : str or Path
        Path to white wine CSV file
    output_file : str or Path
        Path to save cleaned dataset

    Returns
    -------
    pd.DataFrame
        Cleaned and merged dataset

    Raises
    ------
    ValueError
        If inputs are invalid or files cannot be read
    """

    # ---- Convert Path to string ----
    if isinstance(red_input, Path):
        red_input = str(red_input)
    if isinstance(white_input, Path):
        white_input = str(white_input)
    if isinstance(output_file, Path):
        output_file = str(output_file)

    # ---- Validate inputs ----
    for name, path in [("red_input", red_input), ("white_input", white_input), ("output_file", output_file)]:
        if not isinstance(path, str) or path.strip() == "":
            raise ValueError(f"{name} must be a non-empty string.")

    # ---- Load data ----
    try:
        red = pd.read_csv(red_input)
    except EmptyDataError:
        red = pd.DataFrame()
    except Exception as e:
        raise ValueError(f"Error reading red_input: {e}")

    try:
        white = pd.read_csv(white_input)
    except EmptyDataError:
        white = pd.DataFrame()
    except Exception as e:
        raise ValueError(f"Error reading white_input: {e}")

    # ---- Clean column names ----
    red.columns = red.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)
    white.columns = white.columns.str.strip().str.lower().str.replace(" ", "_", regex=False)

    # ---- Add wine type ----
    red["wine_type"] = "red"
    white["wine_type"] = "white"

    # ---- Merge datasets ----
    combined = pd.concat([red, white], ignore_index=True)

    # ---- Save output ----
    try:
        combined.to_csv(output_file, index=False)
    except Exception as e:
        raise ValueError(f"Error saving file: {e}")

    return combined