import click
import pandas as pd
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from source.validate_data import validate_data  # move your validate_data fn to source/

@click.command()
@click.option('--input-file', type=str, required=True, help="Path to cleaned CSV")
@click.option('--output-file', type=str, required=True, help="Path to save validated CSV")
def validate_csv(input_file, output_file):
    """Validate cleaned wine data using Pandera schema."""
    df = pd.read_csv(input_file)
    validated_df = validate_data(df)
    validated_df.to_csv(output_file, index=False)
    print(f"Validated data saved to {output_file}")

if __name__ == "__main__":
    validate_csv()