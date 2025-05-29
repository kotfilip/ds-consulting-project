# Main project logic

from src.etl.load_data import load_csv
from src.etl.transform import preprocess_data
from src.modeling.panel_model import run_panel_model
from src.visualization.plotting import (
    plot_model_coefficients_excl_gdp,
    plot_mortality_trends_by_region,
    plot_gdp_by_region_bar
)


if __name__ == '__main__':
    df = load_csv('data/data.csv')
    df_clean = preprocess_data(df)
    results = run_panel_model(df_clean)
    print(results.summary)
    plot_model_coefficients_excl_gdp(results)
    plot_mortality_trends_by_region(df_clean)
    plot_gdp_by_region_bar(df_clean)
    
