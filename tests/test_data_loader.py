import os
import pandas as pd
from src.data_loader import load_data

def test_load_data():
    df = load_data("../data/raw_analyst_ratings.csv")
    assert isinstance(df, pd.DataFrame)
    assert 'headline' in df.columns
