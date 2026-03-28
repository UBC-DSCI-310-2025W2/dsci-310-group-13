import pytest
import pandas as pd
import matplotlib.pyplot as plt
from src.generate_histograms import generate_histograms

@pytest.fixture
def df():
    return pd.DataFrame({'quality': [5, 6], 'alcohol': [10, 11]})

def test_simple(df):
    fig = generate_histograms(df, 'quality', is_categorical=True)
    assert isinstance(fig, plt.Figure)

def test_edge_empty():
    with pytest.raises(ValueError, match="empty"):
        generate_histograms(pd.DataFrame(), 'quality')

def test_error_missing_col(df):
    with pytest.raises(KeyError):
        generate_histograms(df, 'fake_column')
