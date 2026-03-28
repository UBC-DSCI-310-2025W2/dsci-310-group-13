import pytest
import pandas as pd
import matplotlib.pyplot as plt
from source.generate_histograms import generate_histograms

@pytest.fixture
def sample_wine_data():
    return pd.DataFrame({
        'alcohol': [10.5, 11.0, 12.0, 13.0],
        'quality': [5, 6, 7, 6],
        'wine_type': ['red', 'white', 'red', 'white']
    })

def test_generate_histograms_numeric(sample_wine_data):
    fig = generate_histograms(sample_wine_data, ['alcohol', 'quality'], title="Test Hist")
    # Coverage: Check object type
    assert isinstance(fig, plt.Figure)
    # Coverage: Check title property
    assert fig.texts[0].get_text() == "Test Hist"
    plt.close(fig)

def test_generate_histograms_categorical_content(sample_wine_data):
    # Coverage: Check if categorical logic actually maps labels to the axis
    fig = generate_histograms(sample_wine_data, 'wine_type', is_categorical=True)
    ax = fig.gca()
    tick_labels = [tick.get_text() for tick in ax.get_xticklabels()]
    assert 'red' in tick_labels
    assert 'white' in tick_labels
    plt.close(fig)

def test_generate_histograms_empty_error():
    # Error Case: Empty DF
    with pytest.raises(ValueError, match="The provided DataFrame is empty"):
        generate_histograms(pd.DataFrame(), 'alcohol')
