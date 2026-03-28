import os
import matplotlib.pyplot as plt

def save_figure(fig, output_path):
    """
    Saves a Matplotlib figure object to a file, handling directory creation.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        The figure object to save.
    output_path : str
        The full file path (including filename and extension) where the image 
        should be saved (e.g., 'results/figures/plot.png').

    Returns
    -------
    None

    Raises
    ------
    ValueError
        If the figure object provided is None.
    """
    if fig is None:
        raise ValueError("Figure object is None.")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path)
    plt.close(fig)
