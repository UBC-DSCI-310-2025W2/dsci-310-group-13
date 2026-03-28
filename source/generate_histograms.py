import matplotlib.pyplot as plt
import seaborn as sns

def generate_histograms(data, columns, is_categorical=False, title=None):
    """
    Creates a distribution plot for specified columns.
    """
    if data.empty:
        raise ValueError("The provided DataFrame is empty.")
    
    fig = plt.figure(figsize=(12, 8))
    sns.set_theme(style="whitegrid")

    if is_categorical:
        # If columns is a list, take the first one for countplot
        col = columns[0] if isinstance(columns, list) else columns
        sns.countplot(data=data, x=col, palette='viridis', hue=col, legend=False)
    else:
        data[columns].hist(bins=20, figsize=(15, 10), color='steelblue', edgecolor='black')
        fig = plt.gcf()
        plt.tight_layout(rect=[0, 0.03, 1, 0.95])

    plt.suptitle(title or "Distribution Plot", fontsize=16)
    return fig
