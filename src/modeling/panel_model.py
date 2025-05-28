from linearmodels.panel import PanelOLS
import statsmodels.api as sm

def run_panel_model(df):
    df = df.set_index(['region', 'year'])
    y = df['mortality']
    X = df[['unemployment_rate', 'covid_period']]
    X = sm.add_constant(X)
    model = PanelOLS(y, X, entity_effects=True)
    results = model.fit()
    return results