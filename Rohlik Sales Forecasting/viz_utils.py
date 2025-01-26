import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap
from scipy.stats import gaussian_kde

def plot_kde(df, column, color='#4C72B0', title=None):
    """
    Plots a beautiful and informative KDE plot for any numeric column.

    Parameters:
    - df: pandas DataFrame
    - column: str, name of the numeric column to plot
    - color: str, color for the KDE plot (default: '#4C72B0')
    - title: str, title of the plot (default: "Kernel Density Estimate of {column}")
    """
    # Check if the column exists and is numeric
    if column not in df.columns:
        print(f"Column '{column}' not found in the DataFrame.")
        return
    if not pd.api.types.is_numeric_dtype(df[column]):
        print(f"Column '{column}' is not numeric.")
        return
    
    # Extract column data
    data = df[column].dropna()
    
    # Set default title if not provided
    if title is None:
        title = f"Kernel Density Estimate of {column}"
    
    # Create a KDE plot
    plt.figure(figsize=(10, 6))
    
    # Plot the KDE with a gradient fill
    sns.kdeplot(data, color=color, fill=True, alpha=0.6, label='KDE')
    
    # Add a gradient fill under the curve
    kde = gaussian_kde(data)
    x = np.linspace(data.min(), data.max(), 1000)
    y = kde(x)
    plt.fill_between(x, y, color=color, alpha=0.2, label='Density')
    
    # Add vertical lines for mean, median, and mode
    mean_value = data.mean()
    median_value = data.median()
    mode_value = data.mode().values[0]
    
    plt.axvline(mean_value, color='#D55E00', linestyle='--', linewidth=2, label=f'Mean: {mean_value:.2f}')
    plt.axvline(median_value, color='#009E73', linestyle='-.', linewidth=2, label=f'Median: {median_value:.2f}')
    plt.axvline(mode_value, color='#CC79A7', linestyle=':', linewidth=2, label=f'Mode: {mode_value:.2f}')
    
    # Add annotations for mean, median, and mode
    plt.text(mean_value + 0.05 * data.max(), 0.9 * max(y), f'Mean: {mean_value:.2f}', 
             color='#D55E00', fontsize=9, rotation=0, va='top')
    plt.text(median_value + 0.05 * data.max(), 0.8 * max(y), f'Median: {median_value:.2f}', 
             color='#009E73', fontsize=9, rotation=0, va='top')
    plt.text(mode_value + 0.05 * data.max(), 0.7 * max(y), f'Mode: {mode_value:.2f}', 
             color='#CC79A7', fontsize=9, rotation=0, va='top')
    
    # Customize the plot
    plt.title(title, fontsize=18, pad=20)
    plt.xlabel(column, fontsize=14)
    plt.ylabel('Density', fontsize=14)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend(loc='upper right', fontsize=12)
    
    # Remove top and right spines for a cleaner look
    sns.despine()
    
    # Show the plot
    plt.tight_layout()
    plt.show()

def categorical_plot(df, column, palette="viridis", title=None, 
                             annotate=True, figsize=(18, 10), 
                             font_family="DejaVu Sans"):
    """
    Creates a grid-free horizontal bar plot with descending order and artistic styling.
    """
    
    # Check for column existence
    if column not in df.columns:
        raise ValueError(f"Column '{column}' not found in DataFrame")

    # Set up plot aesthetics
    plt.rcParams['font.family'] = font_family
    plt.rcParams['axes.titleweight'] = 'bold'
    
    # Prepare data with descending order
    counts = df[column].value_counts().sort_values(ascending=True)
    percentages = counts / counts.sum() * 100
    labels = counts.index.tolist()
    values = counts.values
    
    # Create figure and axis
    fig, ax = plt.subplots(figsize=figsize, facecolor='#F5F5F5')
    fig.subplots_adjust(top=0.85, bottom=0.15)
    
    # Create custom gradient palette
    base_color = sns.color_palette(palette, n_colors=1)[0]
    cmap = LinearSegmentedColormap.from_list(
        'custom_gradient', ['white', base_color], N=256
    )
    colors = cmap(np.linspace(0.3, 1, len(labels)))
    
    # Create horizontal bars in descending order
    bars = ax.barh(labels, values, color=colors, edgecolor='#404040', linewidth=0.7)
    
    # Remove all grid lines
    ax.grid(False)
    
    # Add elegant annotations
    if annotate:
        max_value = values.max()
        for i, (value, pct) in enumerate(zip(values, percentages)):
            ax.text(
                value + max_value * 0.008, i,
                f"{value:,}\n({pct:.1f}%)",
                va='center', ha='left', 
                color='#404040', fontsize=11,
                fontstyle='italic'
            )
    
    # Clean spine styling
    for spine in ax.spines.values():
        spine.set_color('#606060')
        spine.set_linewidth(0.8)
    
    # Add titles and labels
    title_text = title if title else f"Distribution of {column}"
    fig.suptitle(title_text, y=0.98, fontsize=16, color='#303030')
    ax.set_xlabel("Count", labelpad=15, fontsize=12, color='#606060')
    
    # Add subtle watermark
    fig.text(
        0.95, 0.05, "Ramdhan H",
        ha='right', va='bottom', 
        color='#A0A0A0', alpha=0.5,
        fontsize=8, rotation=0
    )
    
    plt.tight_layout()
    plt.show()