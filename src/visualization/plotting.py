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


def plot_mortality_trends_by_region(df, regions=None, output_path="figures/mortality_trends_selected_regions.png"):
    """
    Creates a line plot of mortality trends over time for selected regions.

    Parameters:
        df (pd.DataFrame): Preprocessed dataset with 'region', 'year', 'mortality'
        regions (list): List of regions to include in the plot (optional)
        output_path (str): Path to save the plot image
    """
    import pandas as pd

    # Ensure 'mortality' is numeric
    df['mortality'] = df['mortality'].astype(str).str.replace(',', '.')
    df['mortality'] = pd.to_numeric(df['mortality'], errors='coerce')

    # Filter regions if provided
    if regions is None:
        regions = ["Mazowieckie", "Śląskie", "Podkarpackie", "Lubelskie"]
    df_filtered = df[df["region"].isin(regions)]

    # Pivot for plotting
    pivot_df = df_filtered.pivot_table(index="year", columns="region", values="mortality")

    # Plot
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    plt.figure(figsize=(10, 6))
    pivot_df.plot(marker='o', linewidth=2)
    plt.title("Mortality Trends in Selected Regions (2017–2023)")
    plt.ylabel("Mortality Rate")
    plt.xlabel("Year")
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.legend(title="Region", bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    plt.savefig(output_path)
    plt.close()
