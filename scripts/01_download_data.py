import click
import pandas as pd
import os

@click.command()
@click.option('--red-url', type=str, required=True, help="URL for red wine dataset")
@click.option('--white-url', type=str, required=True, help="URL for white wine dataset")
@click.option('--output-dir', type=str, required=True, help="Directory to save raw data")

def download_data(red_url, white_url, output_dir):
    """Download wine datasets and save them to the raw data directory."""

    os.makedirs(output_dir, exist_ok=True)

    red = pd.read_csv(red_url, sep=";")
    white = pd.read_csv(white_url, sep=";")

    red_path = os.path.join(output_dir, "winequality-red.csv")
    white_path = os.path.join(output_dir, "winequality-white.csv")

    red.to_csv(red_path, index=False)
    white.to_csv(white_path, index=False)

    print(f"Red wine data saved to {red_path}")
    print(f"White wine data saved to {white_path}")


if __name__ == "__main__":
    download_data()