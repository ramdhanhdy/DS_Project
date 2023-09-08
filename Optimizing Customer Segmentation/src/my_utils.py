import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import zscore

def find_outlier_columns(df, method='z-score', threshold=3, factor=1.5):
    outlier_cols = []
    num_cols = df.select_dtypes(include=[np.number]).columns

    # Exclude binary columns
    num_cols = [col for col in num_cols if df[col].nunique() > 2]

    if method == 'z-score':
        for col in num_cols:
            z_scores = zscore(df[col].dropna())
            if (np.abs(z_scores) > threshold).any():
                outlier_cols.append(col)
    elif method == 'iqr':
        for col in num_cols:
            Q1 = df[col].quantile(0.25)
            Q3 = df[col].quantile(0.75)
            IQR = Q3 - Q1
            if ((df[col] < (Q1 - factor * IQR)) | (df[col] > (Q3 + factor * IQR))).any():
                outlier_cols.append(col)
    else:
        print(f"Unsupported method: {method}")
        return None

    return outlier_cols


def detect_outliers(df, column, plot=False):
    """
    This function returns a DataFrame that consists of outliers in the specified column of the input DataFrame.
    An optional boxplot for visualizing the outliers can be displayed if plot=True.

    Args:
    df (pandas.DataFrame): The input DataFrame.
    column (str): The name of the column in which to search for outliers.
    plot (bool): If True, display a boxplot for the specified column. Default is False.

    Returns:
    outliers (pandas.DataFrame): A DataFrame that consists of outliers.
    """
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1

    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR

    outliers = df[(df[column] < lower_bound) | (df[column] > upper_bound)]

    if plot:
        plt.figure(figsize=(10,4))
        sns.boxplot(x=df[column])
        plt.title('Boxplot for ' + column)
        plt.show()

    return outliers


    
def plot_dist_kurtosis(df, numerical_cols):
    for col in numerical_cols:
        plt.figure(figsize=(10,5))
        sns.distplot(df[col].dropna(), kde=True)

        kurtosis = df[col].kurtosis()

        # Define kurtosis category
        if kurtosis > 0:
            kurtosis_category = 'Leptokurtic'
        elif kurtosis < 0:
            kurtosis_category = 'Platykurtic'
        else:
            kurtosis_category = 'Mesokurtic'

        # Annotate the kurtosis category
        plt.text(0.97, 0.97, f'Kurtosis: {kurtosis:.2f}\n{kurtosis_category}',
                 verticalalignment='top', horizontalalignment='right',
                 transform=plt.gca().transAxes)

        plt.title(f'Distribution of {col} (kurtosis: {kurtosis:.2f})')
        plt.show()