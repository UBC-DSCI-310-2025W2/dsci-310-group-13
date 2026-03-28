import matplotlib.pyplot as plt
import seaborn as sns

def generate_histograms(data, columns, is_categorical=False, title=None):
    """
    Creates distribution plots (histograms or countplots) for specified columns.

    Parameters
    ----------
    data : pandas.DataFrame
        The dataframe containing the data to visualize.
    columns : str or list of str
        The column(s) to plot. If is_categorical is True, only the first column is used.
    is_categorical : bool, optional
        If True, generates a Seaborn countplot. If False, generates Matplotlib 
        histograms for numeric data. Defaults to False.
    title : str, optional
        The main title for the figure. Defaults to "Distribution Plot".

    Returns
    -------
    matplotlib.figure.Figure
        The figure object containing the distribution plots.

    Raises
    ------
    ValueError
        If the provided dataframe is empty.
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
