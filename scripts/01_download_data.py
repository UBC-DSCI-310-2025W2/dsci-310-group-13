import click



from source.download_data import download_data

@click.command()
@click.option('--red-url', type=str, required=True, help="URL for red wine dataset")
@click.option('--white-url', type=str, required=True, help="URL for white wine dataset")
@click.option('--output-dir', type=str, required=True, help="Directory to save raw data")


def download_csv(red_url, white_url, output_dir):
    """Download wine datasets and save them to the raw data directory."""

    download_data(red_url, white_url, output_dir)


if __name__ == "__main__":
    download_csv()