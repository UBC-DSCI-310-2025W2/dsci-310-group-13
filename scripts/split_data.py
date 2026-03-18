import click
import pandas as pd
from sklearn.model_selection import train_test_split


@click.command()
@click.option('--input-file', type=str, required=True,
              help="Path to cleaned dataset")
@click.option('--train-output', type=str, required=True,
              help="Path to save training dataset")
@click.option('--test-output', type=str, required=True,
              help="Path to save testing dataset")

def split_data(input_file, train_output, test_output):
    """
    Split cleaned dataset into training and testing sets.
    """

    # load cleaned dataset
    wine = pd.read_csv(input_file)

    # perform train-test split
    train, test = train_test_split(
        wine,
        test_size=0.30,
        random_state=42,
        stratify=wine["quality"]
    )

    # save datasets
    train.to_csv(train_output, index=False)
    test.to_csv(test_output, index=False)

    print(f"Training data saved to {train_output}")
    print(f"Testing data saved to {test_output}")


if __name__ == "__main__":
    split_data()