import pandas as pd

def preprocess_data(df):
    """
    Performs preprocessing on the input DataFrame:
    - Adds a COVID period binary variable
    - Standardizes region names
    - Converts numeric columns to float
    - Drops rows with missing values

    Parameters:
        df (pd.DataFrame): Raw data.

    Returns:
        pd.DataFrame: Cleaned and transformed data.
    """
    # Create a binary variable for the COVID-19 period (2020–2023)
    df['covid_period'] = ((df['year'] >= 2020) & (df['year'] <= 2023)).astype(int)

    # Standardize region names (strip whitespace and capitalize)
    df['region'] = df['region'].str.strip().str.title()

    # Convert all non-categorical columns to numeric (coerce errors to NaN)
    numeric_cols = df.columns.difference(['region', 'year'])
    df[numeric_cols] = df[numeric_cols].apply(pd.to_numeric, errors='coerce')

    # Drop rows with any missing values
    df = df.dropna()

    return df
