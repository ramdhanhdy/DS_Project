import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def plot_boxplots_for_numeric_features(df, figsize=(15, 10), columns=None, title="Boxplots of Numeric Features"):
    """
    Plots boxplots for all numeric features in a DataFrame to identify outliers.

    Parameters:
    - df: pandas DataFrame
    - figsize: tuple, size of the figure (default: (15, 10))
    - columns: list, subset of numeric columns to plot (default: None, plots all numeric columns)
    - title: str, title of the plot (default: "Boxplots of Numeric Features")
    """
    # Identify numeric columns
    if columns is None:
        numeric_columns = df.select_dtypes(include=['number']).columns
    else:
        numeric_columns = [col for col in columns if col in df.columns and pd.api.types.is_numeric_dtype(df[col])]
    
    # Check if numeric_columns is empty
    if len(numeric_columns) == 0:
        print("No numeric columns found in the dataset.")
        return
    
    # Set up the figure
    num_plots = len(numeric_columns)
    rows = (num_plots // 3) + (1 if num_plots % 3 != 0 else 0)
    cols = min(3, num_plots)
    
    plt.figure(figsize=figsize)
    plt.suptitle(title, fontsize=16, y=1.02)
    
    # Plot boxplots for each numeric column
    for i, column in enumerate(numeric_columns, 1):
        plt.subplot(rows, cols, i)
        sns.boxplot(x=df[column], color='skyblue')
        plt.title(f"{column}")
        plt.xlabel(column)
    
    plt.tight_layout()
    plt.show()