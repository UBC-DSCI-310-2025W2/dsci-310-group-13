import matplotlib.pyplot as plt
import seaborn as sns

def generate_correlation_heatmap(data, title="Correlation Matrix"):
    """
    Generates a heatmap of Pearson correlation coefficients for all numeric columns.

    This function automatically filters for numeric data types, calculates the 
    correlation matrix, and visualizes it with a 'coolwarm' color map and annotations.

    Parameters
    ----------
    data : pandas.DataFrame
        The dataframe to analyze.
    title : str, optional
        The title for the heatmap. Defaults to "Correlation Matrix".

    Returns
    -------
    matplotlib.figure.Figure
        The figure object containing the correlation heatmap.

    Raises
    ------
    ValueError
        If the dataframe contains no numeric columns (float64 or int64).
    """
    numeric_df = data.select_dtypes(include=['float64', 'int64'])
    if numeric_df.empty:
        raise ValueError("No numeric columns available to correlate.")

    fig = plt.figure(figsize=(12, 10))
    sns.heatmap(numeric_df.corr(), annot=True, cmap='coolwarm', fmt=".2f", linewidths=0.5)
    plt.title(title)
    return fig
  
