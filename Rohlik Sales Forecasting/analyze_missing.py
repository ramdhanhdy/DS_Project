import polars as pl
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter

def plot_missing_values(data, target_column, figsize=(6, 15), title_suffix="samples with non-null target"):
    """
    Plot missing values as a horizontal bar chart for a dataset filtered by a non-null target column.
    
    Parameters:
    - data (pl.DataFrame): The input dataset in Polars DataFrame format.
    - target_column (str): The name of the column used to filter non-null rows.
    - figsize (tuple): The size of the figure (default: (6, 15)).
    - title_suffix (str): Suffix for the plot title (default: "samples with non-null target").
    """
    # Filter rows where the target column is not null
    filtered_data = data.filter(pl.col(target_column).is_not_null())
    
    # Calculate the number of missing values per feature
    missing_values = (
        filtered_data
        .null_count()
        .transpose(include_header=True,
                   header_name='feature',
                   column_names=['null_count'])
        .sort('null_count', descending=True)
        .with_columns((pl.col('null_count') / len(filtered_data)).alias('null_ratio'))
    )
    
    # Plotting the missing values
    plt.figure(figsize=figsize)
    plt.title(f'Missing values over the {len(filtered_data)} {title_suffix}')
    plt.barh(np.arange(len(missing_values)), 
             missing_values.get_column('null_ratio'), 
             color='coral', 
             label='missing')
    plt.barh(np.arange(len(missing_values)), 
             1 - missing_values.get_column('null_ratio'),
             left=missing_values.get_column('null_ratio'),
             color='darkseagreen', 
             label='available')
    plt.yticks(np.arange(len(missing_values)), missing_values.get_column('feature'))
    plt.gca().xaxis.set_major_formatter(PercentFormatter(xmax=1, decimals=0))
    plt.xlim(0, 1)
    plt.legend()
    plt.show()
