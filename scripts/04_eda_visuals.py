import click
import pandas as pd
import os
import sys

sys.path.append(os.path.join(os.path.dirname(__file__), '..'))

from source.generate_histograms import generate_histograms
from source.generate_correlation_heatmap import generate_correlation_heatmap
from source.generate_boxplot_comparison import generate_boxplot_comparison
from source.save_figure import save_figure

@click.command()
@click.option('--input-file', type=str, required=True)
@click.option('--output-dir', type=str, required=True)
def eda_visuals(input_file, output_dir):
    train = pd.read_csv(input_file)

    # 1. Quality Distribution (Categorical Histogram)
    fig1 = generate_histograms(train, 'quality', is_categorical=True, title='Wine Quality Distribution')
    save_figure(fig1, os.path.join(output_dir, "quality_distribution.png"))

    # 2. Physicochemical Features (Numeric Histograms)
    features = train.drop(columns=['quality', 'wine_type'], errors='ignore').columns.tolist()
    fig2 = generate_histograms(train, features, title='Physicochemical Variables')
    save_figure(fig2, os.path.join(output_dir, "feature_distributions.png"))

    # 3. Correlation Heatmap
    fig3 = generate_correlation_heatmap(train)
    save_figure(fig3, os.path.join(output_dir, "correlation_heatmap.png"))

    # 4. Key Features vs Quality
    fig4 = generate_boxplot_comparison(train, 'quality', ['alcohol', 'volatile_acidity'])
    save_figure(fig4, os.path.join(output_dir, "key_features_vs_quality.png"))

    # 5. Summary Table (Simple enough to keep inline or abstract if preferred)
    train.describe().to_csv(os.path.join(output_dir, "summary_statistics.csv"))

if __name__ == "__main__":
    eda_visuals()
