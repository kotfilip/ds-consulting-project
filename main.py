# Główna logika projektu

from src.etl.load_data import load_csv
from src.etl.transform import preprocess_data
from src.modeling.panel_model import run_panel_model

if __name__ == '__main__':
    df = load_csv('data/data.csv')
    df_clean = preprocess_data(df)
    results = run_panel_model(df_clean)
    print(results.summary())