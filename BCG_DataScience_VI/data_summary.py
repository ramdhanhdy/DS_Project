import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
from IPython.display import HTML, display

def generate_minimal_plot(data, dtype):
    """Generate a base64-encoded minimal bar plot for the data with extra side spaces."""
    plt.figure(figsize=(4, 2)) 
    ax = plt.gca()
    
    if dtype == 'Numeric':
        plt.hist(data.dropna(), bins=10, color='skyblue', edgecolor='black')
    elif dtype == 'Object':
        data.value_counts(normalize=True).head(5).plot(kind='bar', color='skyblue', edgecolor='black', ax=ax)
    elif dtype == 'Datetime':
        data.value_counts().sort_index().plot(kind='bar', color='skyblue', ax=ax)
    
    # Remove axes, labels, and titles for minimal visuals
    ax.set_xticks([])
    ax.set_yticks([])
    ax.set_xlabel("")  # Remove x-axis label
    ax.set_ylabel("")  # Remove y-axis label
    ax.set_frame_on(False)
    
    # Add extra spaces on the left and right
    plt.subplots_adjust(left=0.2, right=0.8)  # Adjust left and right margins for extra space
    # plt.tight_layout()
    
    # Encode plot into base64
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight', pad_inches=0)
    plt.close()
    buffer.seek(0)
    encoded_plot = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return f'<img src="data:image/png;base64,{encoded_plot}" width="120" height="140">'

def create_summary_table(df):
    """Generate a summary DataFrame for the given DataFrame."""
    summary = []
    for col in df.columns:
        col_data = df[col]
        graph = None
        missing = col_data.isnull().sum()
        missing_pct = col_data.isnull().mean() * 100
        
        if col_data.dtype == 'object':
            dtype = 'Object'
            top_categories = col_data.value_counts(normalize=True).head(5)
            top_categories_text = "<br>".join(
                f"{idx}: {val} ({round(pct * 100, 1)}%)"
                for idx, (val, pct) in enumerate(top_categories.items())
            )
            summary_text = f"{top_categories_text}"
            graph = generate_minimal_plot(col_data, dtype)
            summary.append({
                'Variable': col,
                'Type': dtype,
                'Details': summary_text,
                'Missing (%)': f"{missing} ({round(missing_pct, 1)}%)",
                'Graph': graph
            })
        elif np.issubdtype(col_data.dtype, np.number):
            dtype = 'Numeric'
            mean = col_data.mean()
            std = col_data.std()
            min_val = col_data.min()
            median = col_data.median()
            max_val = col_data.max()
            iqr = col_data.quantile(0.75) - col_data.quantile(0.25)
            cv = std / mean if mean != 0 else np.nan
            summary_text = (
                f"Mean (sd): {round(mean, 2)} ({round(std, 2)})<br>"
                f"min < med < max: {round(min_val, 2)} < {round(median, 2)} < {round(max_val, 2)}<br>"
                f"IQR (CV): {round(iqr, 2)} ({round(cv, 2) if cv is not np.nan else 'NA'})"
            )
            graph = generate_minimal_plot(col_data, dtype)
            summary.append({
                'Variable': col,
                'Type': dtype,
                'Details': summary_text,
                'Missing (%)': f"{missing} ({round(missing_pct, 1)}%)",
                'Graph': graph
            })
        elif np.issubdtype(col_data.dtype, np.datetime64):
            dtype = 'Datetime'
            min_date = col_data.min()
            max_date = col_data.max()
            summary_text = (
                f"Range: {min_date} to {max_date}"
            )
            graph = generate_minimal_plot(col_data, dtype)
            summary.append({
                'Variable': col,
                'Type': dtype,
                'Details': summary_text,
                'Missing (%)': f"{missing} ({round(missing_pct, 1)}%)",
                'Graph': graph
            })
    return pd.DataFrame(summary)

def view_summary_table(summary_df):
    """Display the summary DataFrame with embedded graphs."""
    summary_html = summary_df.to_html(escape=False, index=False)
    display(HTML(summary_html))

# Example usage:
# df_summary_table = create_summary_table(df)
# view_summary_table(df_summary_table)
