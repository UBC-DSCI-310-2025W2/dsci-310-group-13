import pytest
import matplotlib.pyplot as plt
import os
from source.save_figure import save_figure

def test_save_figure_directory_creation(tmp_path):
    # Coverage: Check if os.makedirs actually works
    fig, _ = plt.subplots()
    # tmp_path is a pytest tool to keep your real project clean
    nested_path = tmp_path / "new_folder" / "deep_folder" / "test.png"
    
    save_figure(fig, str(nested_path))
    
    assert os.path.exists(str(nested_path))
    assert os.path.exists(os.path.dirname(str(nested_path)))

def test_save_figure_none_input():
    # Error Case: Passing None instead of a Figure
    with pytest.raises(ValueError, match="Figure object is None"):
        save_figure(None, "test.png")
