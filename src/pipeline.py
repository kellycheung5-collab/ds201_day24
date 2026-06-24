"""
pipeline.py — Data processing pipeline stub
"""

import pandas as pd


def load_data(filepath: str) -> pd.DataFrame:
    """Load CSV data from the given filepath."""
    df = pd.read_csv(filepath)
    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """Remove nulls and duplicates."""
    df = df.dropna()
    df = df.drop_duplicates()
    return df


def compute_summary(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    """Group by group_col and sum value_col."""
    summary = df.groupby(group_col)[value_col].sum().reset_index()
    summary.columns = [group_col, f'total_{value_col}']
    return summary


if __name__ == '__main__':
    print('Pipeline module loaded successfully.')
