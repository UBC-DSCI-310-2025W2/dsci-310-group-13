import matplotlib.pyplot as plt
import seaborn as sns

def generate_boxplot_comparison(data, x, y_cols, title=None):
    """
    Creates side-by-side boxplots for multiple y-variables against a single x-variable.
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
