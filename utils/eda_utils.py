import matplotlib.pyplot as plt
import seaborn as sns

# Function to perform and plot univariate analysis
def univariate_analysis(df, columns_to_analyze=None, figsize=(20, 10)):
    """
    This function performs univariate analysis for specified or all columns in a DataFrame. 
    It generates appropriate plots (countplot for categorical, histplot for numerical) and displays them in a grid layout.

    Parameters:
        df (pandas.DataFrame): The DataFrame to analyze.
        columns_to_analyze (list, optional): A list of column names to analyze. If None, analyzes all columns.
        figsize (tuple, optional): The size of the figure to display the plots (width, height).

    Returns:
        None: Displays the plots.
    """
    
    # Set the aesthetic style of the plots (optional)
    sns.set_style("whitegrid")

    # If no specific columns are provided, analyze all
    if columns_to_analyze is None:
        columns_to_analyze = df.columns

    # Calculate number of rows and columns for the subplot grid
    num_plots = len(columns_to_analyze)
    num_rows = (num_plots + 1) // 2
    num_cols = 2

    # Create the subplots
    fig, axes = plt.subplots(num_rows, num_cols, figsize=figsize)
    axes = axes.flatten()  # Flatten the array for easy iteration

    # Function for individual plot generation
    def plot_single_variable(data, column, ax):
        if data[column].dtype == 'object':
            sns.countplot(data=data, x=column, palette='viridis', ax=ax)
            ax.set_title(f'Count Plot of {column}')
        else:
            sns.histplot(data[column], kde=True, ax=ax)
            ax.set_title(f'Distribution of {column}')
        ax.set_xlabel(column)
        ax.set_ylabel('Frequency/Density')
        ax.tick_params(axis='x', rotation=45)

    # Generate plots for each column
    for i, column in enumerate(columns_to_analyze):
        plot_single_variable(df, column, axes[i])

    # Remove any extra empty subplots
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])

    # Adjust layout for better readability
    plt.tight_layout()

    # Show the plots
    plt.show()