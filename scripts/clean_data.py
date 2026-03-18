import click
import pandas as pd


@click.command()
@click.option('--red-input', type=str, required=True, help="Path to raw red wine CSV")
@click.option('--white-input', type=str, required=True, help="Path to raw white wine CSV")
@click.option('--output-file', type=str, required=True, help="Path to save processed dataset")
def clean_data(red_input, white_input, output_file):
    """
    Clean and merge the wine datasets.
    """

    # load raw datasets
    red = pd.read_csv(red_input)
    white = pd.read_csv(white_input)

    # clean column names
    red.columns = red.columns.str.strip().str.lower().str.replace(" ", "_")
    white.columns = white.columns.str.strip().str.lower().str.replace(" ", "_")

    # add wine type labels
    red["wine_type"] = "red"
    white["wine_type"] = "white"

    # merge datasets
    wine = pd.concat([red, white], ignore_index=True)

    # save processed dataset
    wine.to_csv(output_file, index=False)

    print(f"Processed dataset saved to {output_file}")


if __name__ == "__main__":
    clean_data()