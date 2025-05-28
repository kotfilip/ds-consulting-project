import pandas as pd

def load_csv(path):
    """
    Loads a CSV file and returns a pandas DataFrame.

    Parameters:
        path (str): The file path to the CSV file.

    Returns:
        pd.DataFrame: Loaded data as a DataFrame.
    """
    df = pd.read_csv(path)
    return df
