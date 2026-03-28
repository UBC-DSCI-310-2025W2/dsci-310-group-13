import matplotlib.pyplot as plt
import seaborn as sns

def generate_correlation_heatmap(data, title="Correlation Matrix"):
    """
    Generates a heatmap of correlations for all numeric columns.
    """
    numeric_df = data.select_dtypes(include=['float64', 'int64'])
    if numeric_df.empty:
        raise ValueError("No numeric columns available to correlate.")

    fig = plt.figure(figsize=(12, 10))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title(title)
    return fig
  
