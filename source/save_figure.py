import os
import matplotlib.pyplot as plt

def save_figure(fig, output_path):
    """
    Saves a Matplotlib figure to a specified path, creating directories if needed.
    """
    if fig is None:
        raise ValueError("Figure object is None.")
    
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    fig.savefig(output_path)
    plt.close(fig)
