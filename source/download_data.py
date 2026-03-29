import pandas as pd
from pathlib import Path
import os


def download_data(red_url, white_url, output_dir, sep=";"):
    """
    Download wine datasets from URLs and save them locally.

    Parameters
    ----------
    red_url : str or Path
        URL for red wine dataset
    white_url : str or Path
        URL for white wine dataset
    output_dir : str or Path
        Directory to save downloaded CSV files
    sep : str
        Separator used in CSV files (default ';')

    Returns
    -------
    tuple
        (red_df, white_df, red_path, white_path)

    Raises
    ------
    ValueError
        If inputs are invalid or download fails
    """

    # ---- Convert Path to string ----
    for name, value in [("red_url", red_url), ("white_url", white_url), ("output_dir", output_dir)]:
        if isinstance(value, Path):
            value = str(value)

        if not isinstance(value, str) or value.strip() == "":
            raise ValueError(f"{name} must be a non-empty string.")

    red_url = str(red_url)
    white_url = str(white_url)
    output_dir = str(output_dir)

    # ---- Create directory ----
    os.makedirs(output_dir, exist_ok=True)

    # ---- Load data ----
    try:
        red_df = pd.read_csv(red_url, sep=sep)
        white_df = pd.read_csv(white_url, sep=sep)
    except Exception as e:
        raise ValueError(f"Error downloading data: {e}")

    # ---- Save files ----
    red_path = os.path.join(output_dir, "winequality-red.csv")
    white_path = os.path.join(output_dir, "winequality-white.csv")

    red_df.to_csv(red_path, index=False)
    white_df.to_csv(white_path, index=False)

    return red_df, white_df, red_path, white_path