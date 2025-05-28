from linearmodels.panel import PanelOLS
import statsmodels.api as sm

def run_panel_model(df):
    """
    Runs a Fixed Effects panel regression model.

    Parameters:
        df (pd.DataFrame): Preprocessed panel data with region and year.

    Returns:
        PanelOLSResults: Fitted model results.
    """
    # Set multi-index for panel data (region, year)
    df = df.set_index(['region', 'year'])

    # Dependent variable
    y = df['mortality']

    # Independent variables (you can expand this list)
    X = df[['unemployment_rate', 'urbanization', 'gdp_per_capita', 
            'avg_salary', 'doctors_per_10k', 'pollution', 
            'age_65_plus', 'covid_period']]
    X = sm.add_constant(X)

    # Estimate the model with entity fixed effects
    model = PanelOLS(y, X, entity_effects=True)
    results = model.fit()

    return results
