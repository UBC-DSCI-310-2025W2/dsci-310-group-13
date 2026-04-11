import click
import pandas as pd
import os
from wine_quality_tools import (
    generate_histograms,
    generate_correlation_heatmap,
    generate_boxplot_comparison,
    save_figure,
)


@click.command()
@click.option('--input-file', type=str, required=True)
@click.option('--output-dir', type=str, required=True)
def eda_visuals(input_file, output_dir):
    train = pd.read_csv(input_file)

    fig1 = generate_histograms(train, 'quality', is_categorical=True, title='Wine Quality Distribution')
    save_figure(fig1, os.path.join(output_dir, "quality_distribution.png"))

    features = train.drop(columns=['quality', 'wine_type'], errors='ignore').columns.tolist()
    fig2 = generate_histograms(train, features, title='Physicochemical Variables')
    save_figure(fig2, os.path.join(output_dir, "feature_distributions.png"))

    fig3 = generate_correlation_heatmap(train)
    save_figure(fig3, os.path.join(output_dir, "correlation_heatmap.png"))

    fig4 = generate_boxplot_comparison(train, 'quality', ['alcohol', 'volatile_acidity'])
    save_figure(fig4, os.path.join(output_dir, "key_features_vs_quality.png"))

    train.describe().to_csv(os.path.join(output_dir, "summary_statistics.csv"))


if __name__ == "__main__":
    eda_visuals()
