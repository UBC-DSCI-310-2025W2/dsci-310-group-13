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

    # 3. Figure 2: Distribution of all physicochemical features
    plt.figure(figsize=(15, 10))
    train.drop(columns=['quality', 'wine_type'], errors='ignore').hist(
        bins=20, figsize=(15, 10), color='steelblue', edgecolor='black'
    )
    plt.suptitle("Distribution of Physicochemical Variables", fontsize=16)
    plt.tight_layout(rect=[0, 0.03, 1, 0.95])
    
    hist_path = os.path.join(output_dir, "feature_distributions.png")
    plt.savefig(hist_path)
    plt.close()
    print(f"Feature histograms saved to {hist_path}")
    


    # 4. Figure 3: Correlation Heatmap
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

    # 5. Figure 4: Key Chemical Features vs Quality (Alcohol and Volatile Acidity)
    fig, axes = plt.subplots(1, 2, figsize=(15, 6))

    # Alcohol vs Quality
    sns.boxplot(data=train, x='quality', y='alcohol', ax=axes[0])
    axes[0].set_title("Alcohol Content vs. Quality")
    axes[0].set_xlabel("Quality Rating")
    axes[0].set_ylabel("Alcohol (%)")

    # Volatile Acidity vs Quality
    sns.boxplot(data=train, x='quality', y='volatile_acidity', ax=axes[1])
    axes[1].set_title("Volatile Acidity vs. Quality")
    axes[1].set_xlabel("Quality Rating")
    axes[1].set_ylabel("Volatile Acidity (g/dm³)")

    plt.suptitle("Distribution of Key Chemical Features across Quality Ratings", fontsize=16)
    
    key_features_path = os.path.join(output_dir, "key_features_vs_quality.png")
    plt.savefig(key_features_path)
    plt.close()
    print(f"Key features plot saved to {key_features_path}")
    
    # 5. Summary Table
    summary_stats = train.describe()
    summary_path = os.path.join(output_dir, "summary_statistics.csv")
    summary_stats.to_csv(summary_path)
    print(f"Summary statistics saved to {summary_path}")


if __name__ == "__main__":
    eda_visuals()
