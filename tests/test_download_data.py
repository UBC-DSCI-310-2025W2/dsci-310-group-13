import pytest
import pandas as pd
import os
from source.download_data import load_csv_from_url, save_dataframe

#load data from the url
# simple case 1
def test_load_csv_valid():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = load_csv_from_url(url, sep=",")
    assert isinstance(df, pd.DataFrame)


# simple case 2
def test_load_csv_shape():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = load_csv_from_url(url, sep=",")
    assert df.shape[0] > 0


# edge case (weird separator but still valid input)
def test_load_csv_different_sep():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/iris.csv"
    df = load_csv_from_url(url, sep=",")
    assert "sepal_length" in df.columns


# wrong input
def test_load_csv_invalid_url():
    with pytest.raises(ValueError):
        load_csv_from_url("invalid_url")



# save_dataframe

# simple case 1
def test_save_dataframe(tmp_path):
    df = pd.DataFrame({"a": [1, 2]})
    file_path = str(tmp_path / "test.csv")

    save_dataframe(df, file_path)
    assert os.path.exists(file_path)


# simple case 2
def test_save_dataframe_content(tmp_path):
    df = pd.DataFrame({"a": [1, 2]})
    file_path = tmp_path / "test.csv"

    save_dataframe(df, file_path)
    loaded = pd.read_csv(file_path)

    assert loaded.equals(df)


# edge case (empty dataframe)
def test_save_empty_dataframe(tmp_path):
    df = pd.DataFrame()
    file_path = tmp_path / "empty.csv"

    save_dataframe(df, file_path)
    assert os.path.exists(file_path)


# wrong input
def test_save_invalid_input(tmp_path):
    with pytest.raises(ValueError):
        save_dataframe("not_a_dataframe", tmp_path / "fail.csv")