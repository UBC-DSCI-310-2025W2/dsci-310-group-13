import matplotlib.pyplot as plt
import seaborn as sns

def generate_boxplot_comparison(data, x, y_cols, title=None):
    """
    Creates side-by-side boxplots for multiple y-variables against a single x-variable.

    Parameters
    ----------
    data : pandas.DataFrame
        The dataframe containing the variables to plot.
    x : str
        The column name to be used for the x-axis (usually a categorical variable like 'quality').
    y_cols : list of str
        A list of column names for the y-axis (numerical features like 'alcohol' or 'pH').
    title : str, optional
        The main title for the entire figure. Defaults to "Comparison across {x}".

    Returns
    -------
    matplotlib.figure.Figure
        The figure object containing the generated boxplots.

    Raises
    ------
    KeyError
        If any of the specified columns are not present in the dataframe.
    """
    for col in [x] + y_cols:
        if col not in data.columns:
            raise KeyError(f"Column '{col}' not found in DataFrame.")

    fig, axes = plt.subplots(1, len(y_cols), figsize=(15, 6))
    if len(y_cols) == 1: axes = [axes]

    for i, y in enumerate(y_cols):
        sns.boxplot(data=data, x=x, y=y, ax=axes[i])
        axes[i].set_title(f"{y.replace('_', ' ').title()} vs {x.title()}")

    plt.suptitle(title or f"Comparison across {x}", fontsize=16)
    return fig
