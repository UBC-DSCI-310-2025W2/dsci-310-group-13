import click
from wine_quality_tools import load_data, stratified_split, save_data


@click.command()
@click.option('--input-file', type=str, required=True, help="Path to cleaned dataset")
@click.option('--train-output', type=str, required=True, help="Path to save training dataset")
@click.option('--test-output', type=str, required=True, help="Path to save testing dataset")
def split_data(input_file, train_output, test_output):
    """Split cleaned dataset into training and testing sets."""
    wine = load_data(input_file)
    train, test = stratified_split(wine, target_col="quality", test_size=0.30, random_state=42)
    save_data(train, train_output)
    save_data(test, test_output)
    print(f"Training data saved to {train_output}")
    print(f"Testing data saved to {test_output}")


if __name__ == "__main__":
    split_data()
