import click
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import os


@click.command()
@click.option('--input-file', type=str, required=True, 
              help="Path to the training dataset (e.g., data/train.csv)")
@click.option('--output-dir', type=str, required=True, 
              help="Directory to save the generated plots")
def eda_visuals(input_file, output_dir):
    """
    Perform Exploratory Data Analysis and save visualizations.
    """

    # 1. Load the training dataset
    train = pd.read_csv(input_file)

    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)

    # Set the aesthetic style of the plots
    sns.set_theme(style="whitegrid")

    # 2. Figure 1: Distribution of Wine Quality
    plt.figure(figsize=(10, 6))
    sns.countplot(data=train, x='quality', palette='viridis')
    plt.title('Distribution of Wine Quality Scores')
    plt.xlabel('Quality Rating')
    plt.ylabel('Count')
    
    quality_dist_path = os.path.join(output_dir, "quality_distribution.png")
    plt.savefig(quality_dist_path)
    plt.close()
    print(f"Quality distribution plot saved to {quality_dist_path}")

    # 3. Figure 2: Correlation Heatmap
    # We select only numeric columns for correlation (ignoring 'wine_type')
    numeric_df = train.select_dtypes(include=['float64', 'int64'])
    plt.figure(figsize=(12, 10))
    corr_matrix = numeric_df.corr()
    sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title('Correlation Matrix of Physicochemical Properties')
    
    corr_map_path = os.path.join(output_dir, "correlation_heatmap.png")
    plt.savefig(corr_map_path)
    plt.close()
    print(f"Correlation heatmap saved to {corr_map_path}")

    # 4. Figure 3: Alcohol vs Quality 
    plt.figure(figsize=(10, 6))
    sns.boxplot(data=train, x='quality', y='alcohol', palette='Set2')
    plt.title('Alcohol Content by Wine Quality')
    plt.xlabel('Quality Rating')
    plt.ylabel('Alcohol (%)')
    
    alcohol_plot_path = os.path.join(output_dir, "alcohol_vs_quality.png")
    plt.savefig(alcohol_plot_path)
    plt.close()
    print(f"Alcohol vs Quality plot saved to {alcohol_plot_path}")

    # 5. Summary Table
    summary_stats = train.describe()
    summary_path = os.path.join(output_dir, "summary_statistics.csv")
    summary_stats.to_csv(summary_path)
    print(f"Summary statistics saved to {summary_path}")


if __name__ == "__main__":
    eda_visuals()
