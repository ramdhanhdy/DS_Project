import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
from IPython.display import HTML
import base64
from io import BytesIO

def plot_to_base64(series, var_type):
    plt.figure(figsize=(2, 1.5))
    if var_type in ['int64', 'float64']:
        sns.histplot(series.dropna(), kde=False, color="skyblue", bins=30)
    elif var_type in ['object', 'category']:
        value_counts = series.value_counts()
        sns.barplot(x=value_counts.index[:5], y=value_counts.values[:5], color="skyblue")
        plt.xticks(rotation=45, ha='right')
    else:
        plt.text(0.5, 0.5, f"Unsupported type: {var_type}", ha='center', va='center')
    
    plt.axis('off')
    plt.tight_layout()
    buffer = BytesIO()
    plt.savefig(buffer, format="png", dpi=100, bbox_inches='tight', pad_inches=0.1)
    plt.close()
    return base64.b64encode(buffer.getvalue()).decode("utf-8")

def create_summary_table(df):
    def get_variable_summary(series):
        var_type = str(series.dtype)
        missing = series.isnull().sum()
        distinct = series.nunique()
        
        if var_type in ['int64', 'float64']:
            stats = series.describe()
            iqr = stats['75%'] - stats['25%']
            cv = (stats['std'] / stats['mean']).round(1) if stats['mean'] != 0 else np.nan
            stats = [
                ('Mean (sd)', f"{stats['mean']:.1f} ({stats['std']:.1f})"),
                ('min < med < max', f"{stats['min']:.1f} < {stats['50%']:.1f} < {stats['max']:.1f}"),
                ('IQR (CV)', f"{iqr:.1f} ({cv})")
            ]
        else:
            freq_counts = series.value_counts()
            stats = [
                (str(val), f"{count} ({count/series.count()*100:.1f}%)")
                for val, count in freq_counts.head().items()
            ]
        
        graph = plot_to_base64(series, var_type)
        return var_type, stats, missing, distinct, graph

    summaries = []
    for col in df.columns:
        var_type, stats, missing, distinct, graph = get_variable_summary(df[col])
        summaries.append({
            'Variable': col,
            'Type': var_type,
            'Stats': stats,
            'Missing': missing,
            'Distinct': distinct,
            'Graph': graph
        })

    html_parts = ['<table style="border-collapse: collapse; width: 100%;">']
    html_parts.append('<tr><th>No</th><th>Variable</th><th>Stats / Values</th><th>Freqs (% of Valid)</th><th>Graph</th><th>Missing</th></tr>')

    for idx, summary in enumerate(summaries, 1):
        html_parts.append(f'<tr><td>{idx}</td><td>{summary["Variable"]}<br>[{summary["Type"]}]</td>')
        
        stats_html = '<br>'.join([f"{stat}: {value}" for stat, value in summary['Stats']])
        freqs_html = f"{summary['Distinct']} distinct values"
        
        html_parts.append(f'<td>{stats_html}</td>')
        html_parts.append(f'<td>{freqs_html}</td>')
        html_parts.append(f'<td><img src="data:image/png;base64,{summary["Graph"]}" style="width:200px;height:150px;"></td>')
        html_parts.append(f'<td>{summary["Missing"]} ({summary["Missing"]/len(df)*100:.1f}%)</td></tr>')
    html_parts.append('</table>')
    return HTML(''.join(html_parts))