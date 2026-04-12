import click
import pandas as pd
from wine_quality_tools import clean_data


@click.command()
@click.option('--red-input', type=str, required=True, help="Path to raw red wine CSV")
@click.option('--white-input', type=str, required=True, help="Path to raw white wine CSV")
@click.option('--output-file', type=str, required=True, help="Path to save processed dataset")
def clean_csv(red_input, white_input, output_file):
    """Clean and merge the wine datasets."""
    clean_data(red_input, white_input, output_file)
    
    # remove duplicates after cleaning
    df = pd.read_csv(output_file)
    before = len(df)
    df = df.drop_duplicates()
    after = len(df)
    print(f"Removed {before - after} duplicate rows ({before} -> {after})")
    df.to_csv(output_file, index=False)


if __name__ == "__main__":
    clean_csv()
