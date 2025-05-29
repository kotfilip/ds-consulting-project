import matplotlib.pyplot as plt
import os

def plot_model_coefficients_excl_gdp(results, output_path="figures/model_coefficients_excl_gdp.png"):
    """
    Creates a vertical bar plot of model coefficients excluding GDP per capita,
    with annotations and significance indication.

    Parameters:
        results: Fitted PanelOLS model results (from linearmodels)
        output_path (str): Path to save the plot image
    """
    # Prepare data
    coefs = results.params.copy()
    pvals = results.pvalues.copy()

    if 'const' in coefs:
        coefs = coefs.drop('const')
        pvals = pvals.drop('const')

    if 'gdp_per_capita' in coefs:
        coefs = coefs.drop('gdp_per_capita')
        pvals = pvals.drop('gdp_per_capita')

    # Determine significance
    significance = pvals < 0.05
    colors = ['steelblue' if sig else 'lightgray' for sig in significance]
    labels = [f"{var}\n(n.s.)" if not sig else var for var, sig in zip(coefs.index, significance)]

    # Create plot
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.figure(figsize=(10, 6))
    bars = plt.bar(labels, coefs.values, color=colors, edgecolor='black')

    # Add value labels above each bar
    for bar, value in zip(bars, coefs.values):
        y_pos = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, y_pos,
                 f"{value:.2f}", ha='center',
                 va='bottom' if value >= 0 else 'top',
                 fontsize=8, color='black')

    # Styling
    plt.axhline(y=0, color='black', linestyle='--', linewidth=0.8)
    plt.title("Effect of Variables on Mortality (excluding GDP per capita)")
    plt.ylabel("Coefficient Value")
    plt.xticks(rotation=45, ha='right')
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    # Save
    plt.savefig(output_path)
    plt.close()