import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib import ticker as plticker
import seaborn as sns

color_lists = ['r','k','b','g','y','m','c','chartreuse', 'silver', 'lightstealblue', 'deepskyblue', 'cornflowerblue', 'limegreen', 'mediumblue', 'goldenrod', 'burlywood', 'navy', 'brown', 'teal', 'darkgray', 'slategrey', 'turquoise', 'navajowhite', 'lightgray', 'darkgreen', 'mocassin', 'steelblue']

def plot_df_line(df, x_col, y_cols, title, x_label, y_label, line_plot_settings):
    """
    INPUT:
        - df:       the DataFrame which should be plotted as a line plot,
        - x_col:    x-axis of the plot
        - y_cols:   the y axis of the plot
        - title:    provide a title as string for the plot
        - x_label:  name of the x axis
        - y_label:  name of the y axis
        - line_plot_settings: Dictionray with plot_settings

    OUTPUT:
        - A line plot with a specially designed layout

    AIM:
        1.) Set the plot
        2.) Prepare the legend
        3.) Set the plot axes and title
    """

    figure_size=line_plot_settings['figure_size']
    subplots=line_plot_settings['subplots']
    fontsize_title=line_plot_settings['fontsize_title']
    fontsize_axes_values=line_plot_settings['fontsize_axes_values']
    fontsize_axes_label=line_plot_settings['fontsize_axes_label']
    fontsize_text=line_plot_settings['fontsize_text']
    fontsize_legend=line_plot_settings['fontsize_legend']
    line_width=line_plot_settings['line_width']
    marker=line_plot_settings['marker']
    marker_size=line_plot_settings['marker_size']
    set_xticks_range=line_plot_settings['set_xticks_range']
    xticks_start=line_plot_settings['xticks_start']
    xticks_end=line_plot_settings['xticks_end']
    xticks_step=line_plot_settings['xticks_step']
    set_yticks_range=line_plot_settings['set_yticks_range']
    yticks_start=line_plot_settings['yticks_start']
    yticks_end=line_plot_settings['yticks_end']
    yticks_step=line_plot_settings['yticks_step']
    xlim_value_lower=line_plot_settings['xlim_value_lower']
    xlim_value_upper=line_plot_settings['xlim_value_upper']
    ylim_value_lower=line_plot_settings['ylim_value_lower']
    ylim_value_upper=line_plot_settings['ylim_value_upper']
    color_lists=line_plot_settings['color_lists']
    legend_state=line_plot_settings['legend_state']
    legend_list_to_plot =line_plot_settings['legend_list_to_plot']
    legend_move =line_plot_settings['legend_move']
    legend_x=line_plot_settings['legend_x']
    legend_y=line_plot_settings['legend_y']

    """
    Set plot
    """
    axes = df.plot(
            x=x_col,
            y=y_cols,
            subplots=subplots,
            layout=(1, 1),
            figsize=figure_size,
            legend=legend_state,
            color = color_lists,
            linewidth=line_width,
            marker=marker,
            ms=marker_size,
            fillstyle='full'
           )
    """
    Prepare legend
    """
    axes.legend(fontsize=fontsize_legend)
    if legend_list_to_plot != '':
        axes.legend(legend_list_to_plot)

    if legend_move == True:
        axes.get_legend().set_bbox_to_anchor((legend_x,legend_y))

    """
    Set plot axes and title
    """
    axes.set_title(title, size=fontsize_title, verticalalignment='bottom',horizontalalignment='center')
    if set_xticks_range == True:
        axes.set_xticks(np.arange(xticks_start, xticks_end, xticks_step))
    if set_yticks_range == True:
        axes.set_yticks(np.arange(yticks_start, yticks_end, yticks_step))
    axes.tick_params(axis="both", labelsize=fontsize_axes_values)
    if x_label != '':
        axes.set_xlabel(x_label, fontsize=fontsize_axes_label)
    if y_label != '':
        axes.set_ylabel(y_label, fontsize=fontsize_axes_label)
    if xlim_value_lower != None or xlim_value_upper != None:
        axes.set_xlim(xlim_value_lower, xlim_value_upper)
    if ylim_value_lower != None or ylim_value_upper != None:
        axes.set_ylim(ylim_value_lower, ylim_value_upper)
    #axes.grid(True)


def plot_df_bar(df, title, bar_setting_dict):
    """
    INPUT:
        - df:       the DataFrame which should be plotted as a bar plot,
                    index of df --> categorical x axis of the bar plot,
                    columns of df --> the bars of the plot
        - title:    provide a title as string for the plot
        - bar_setting_dict: Dictionray with plot_settings

    OUTPUT:
        - A bar plot with a specially designed layout

    AIM:
        1.) Set the plot
        2.) Prepare the legend
        3.) Set the plot axes and title
    """


    """
    Set plot
    """
    axes = df.plot(
            kind='bar',
            subplots=bar_setting_dict['subplots'],
            layout=bar_setting_dict['layout'],
            figsize=bar_setting_dict['figsize'],
            width=bar_setting_dict['width'],
            align=bar_setting_dict['align'],
            legend=bar_setting_dict['legend_state']
           )

    """
    Prepare legend
    """
    if bar_setting_dict['legend_state']==True:
        axes.legend(fontsize=bar_setting_dict['fontsize_legend'])
        if bar_setting_dict['legend_list_to_plot'] != '':
            axes.legend(bar_setting_dict['legend_list_to_plot'])

        if bar_setting_dict['legend_move'] == True:
            axes.get_legend().set_bbox_to_anchor((bar_setting_dict['legend_x'], bar_setting_dict['legend_y']))

    """
    Set plot axes and title
    """

    axes.set_title(title, size=bar_setting_dict['fontsize_title'], verticalalignment='bottom', horizontalalignment='center')
    if bar_setting_dict['set_yticks_range'] == True:
        axes.set_yticks(np.arange(bar_setting_dict['yticks_start'], bar_setting_dict['yticks_end'], bar_setting_dict['yticks_step']))
    axes.tick_params(axis="both", labelsize=bar_setting_dict['fontsize_axes_values'])
    if bar_setting_dict['x_label'] != '':
        axes.set_xlabel(bar_setting_dict['x_label'], fontsize=bar_setting_dict['fontsize_axes_label'])
    else:
        axes.set_xlabel('')

    if bar_setting_dict['y_label'] != '':
        axes.set_ylabel(bar_setting_dict['y_label'], fontsize=bar_setting_dict['fontsize_axes_label'])
    else:
        axes.set_ylabel('')



def plot_df_pie(df, title, explode, pie_setting_dict):
    """
    INPUT:
        - df: the DataFrame which should be plotted as a pie plot,
                columns of df --> the pie pieces of the plot
        - title: provide a title as string for the plot
        - explode: a list which sets the explosion of each pie piece, length must be the same as the number of pie pieces
        - pie_setting_dict:  Dictionray with plot_settings

    OUTPUT:
        - A pie chart with a specially designed layout

    AIM:
        1.) Set the plot
        2.) Prepare the legend
        3.) Set the plot axes and title
    """

    figsize=pie_setting_dict['figsize']
    shadow=pie_setting_dict['shadow']
    autopct=pie_setting_dict['autopct']
    startangle=pie_setting_dict['startangle']
    fontsize_title=pie_setting_dict['fontsize_title']
    fontsize_text=pie_setting_dict['fontsize_text']
    fontsize_legend=pie_setting_dict['fontsize_legend']
    legend_state=pie_setting_dict['legend_state']
    legend_title=pie_setting_dict['legend_title']
    legend_list_to_plot =pie_setting_dict['legend_list_to_plot']
    legend_move = pie_setting_dict['legend_move']
    legend_x=pie_setting_dict['legend_x']
    legend_y=pie_setting_dict['legend_y']

    """
    Set plot
    """
    axes = df.plot(
            kind='pie',
            explode=explode,
            autopct=autopct,
            textprops={'fontsize': fontsize_text},
            shadow=shadow,
            startangle=startangle,
            figsize=figsize,
            legend=legend_state
           )

    """
    Prepare legend
    """

    if legend_state==True:

        if legend_list_to_plot != '':
            axes.legend(legend_list_to_plot)
        if legend_title != '':
            axes.legend(title=legend_title)
        axes.legend(fontsize=fontsize_legend)
        if legend_move == True:
            axes.get_legend().set_bbox_to_anchor((legend_x,legend_y))

    """
    Set plot axes and title
    """
    axes.set_xlabel('')
    axes.set_ylabel('')

    axes.set_title(title, size=fontsize_title, verticalalignment='bottom',horizontalalignment='center')
    axes.axis('equal')


def plot_sparsity(df, col, target_col):
    stats = df[[col, target_col]].groupby(col).agg(['count', 'mean', 'sum'])
    stats = stats.reset_index()
    stats.columns = [col, 'count', 'mean', 'sum']
    stats_sort = stats['count'].value_counts().reset_index()
    stats_sort = stats_sort.sort_values('index')
    plt.figure(figsize=(15,4))
    plt.bar(stats_sort['index'].astype(str).values[0:20], stats_sort['count'].values[0:20])
    plt.title('Frequency of ' + str(col))
    plt.xlabel('Number frequency')
    plt.ylabel('Frequency')

def plot_top20(df, col, target_col):
    stats = df[[col, target_col]].groupby(col).agg(['count', 'mean', 'sum'])
    stats = stats.reset_index()
    stats.columns = [col, 'count', 'mean', 'sum']
    stats = stats.sort_values('count', ascending=False)
    fig, ax1 = plt.subplots(figsize=(15,4))
    ax2 = ax1.twinx()
    ax1.bar(stats[col].astype(str).values[0:20], stats['count'].values[0:20])
    ax1.set_xticklabels(stats[col].astype(str).values[0:20], rotation='vertical')
    ax2.plot(stats['mean'].values[0:20], color='red')
    ax2.set_ylim(0,1)
    ax2.set_ylabel('Mean Target')
    ax1.set_ylabel('Frequency')
    ax1.set_xlabel(col)
    ax1.set_title('Top20 ' + col + 's based on frequency')

def visualize_category_counts(df, column, ax):
    # Count the occurrences of each unique value
    value_counts = df[column].value_counts()

    # Calculate the percentage of each value
    percentages = value_counts / len(df) * 100

    # Sort the values in descending order
    sorted_values = value_counts.sort_values(ascending=False)

    if len(sorted_values) > 2:
        # If non-binary, use seaborn barplot
        sns.barplot(x=sorted_values.values, y=sorted_values.index, ax=ax, palette='copper_r')
        ax.set_title(f'{column} Counts')
        ax.set_xlabel('Count')
        ax.set_ylabel(column)

        # Add count and percentage text to each bar
        for i, count in enumerate(sorted_values):
            percentage = percentages[sorted_values.index[i]]
            ax.text(count, i, f"{count} ({percentage:.1f}%)", va='center')
    else:
        # If binary, use a pie chart
        ax.pie(sorted_values, labels=sorted_values.index, autopct='%1.1f%%', startangle=90)
        ax.set_title(f'{column} Distribution')

    ax.grid(False)


def analyze_missing(df, min_percent_missing=0, max_percent_missing=100, plot_distribution=False):
    # calculate the number of missing values for each column
    missing_counts = df.isnull().sum()
    # create a new DataFrame with the variable name and number of missing values for each column
    output_df = pd.DataFrame(data=missing_counts.values, index=missing_counts.index, columns=['Missing Values'])
    # calculate the percentage of missing values for each column
    output_df['Percent Missing'] = output_df['Missing Values'] / df.shape[0] * 100
    # sort the output DataFrame by the number of missing values in descending order
    output_df = output_df.sort_values(by='Missing Values', ascending=False)

    if plot_distribution:
        # plot a histogram of the percentage of missing values for all columns
        plt.hist(output_df['Percent Missing'], bins=20, edgecolor='black')
        plt.title('Distribution of Missing Values')
        plt.xlabel('Percent Missing')
        plt.ylabel('Count')
        plt.show()

    # only return columns where the percentage of missing values is within the range [min_percent_missing, max_percent_missing]
    output_df = output_df[(output_df['Percent Missing'] >= min_percent_missing) & (output_df['Percent Missing'] <= max_percent_missing)]

    return output_df

def discretize(v, v_intervals, use_quartiles=False, use_continuous_bins=False):
    if isinstance(v, (pd.core.series.Series, np.ndarray)) and isinstance(v_intervals, (list, np.ndarray)) and len(np.unique(v)) != len(v_intervals):
        raise Exception("length of interval must match unique items in array")

    if isinstance(v, (str)) and isinstance(v_intervals, (list, np.ndarray)):
        #name of variable instead of array and list of intervals used
        if isinstance(v_intervals, list): v_intervals = np.array(v_intervals)
        return v, v_intervals

    if (np.isin(v.dtype, [int, float, 'int8', 'int16', 'int32', 'float16', 'float32'])) and (isinstance(v_intervals, (int))) and (len(np.unique(v)) >= v_intervals) and (max(v) > min(v)):
        #v is discretizable, otherwise assumed to be already discretized
        if use_continuous_bins:
            if use_quartiles:
                v, bins = pd.qcut(v, v_intervals, duplicates='drop', retbins=True, labels=True, precision=2)
            else:
                v, bins = pd.cut(v, v_intervals, duplicates='drop', retbins=True, labels=True, precision=2)
        else:
            if use_quartiles:
                v = pd.qcut(v, v_intervals, duplicates='drop', precision=2)
            else:
                v = pd.cut(v, v_intervals, duplicates='drop', precision=2)

    if np.isin(v.dtype, [object, 'category']):
        if not isinstance(v, (pd.core.series.Series)):
            v = pd.Series(v)
        bins = np.sort(np.unique(v)).astype(str)
        v = v.astype(str)
        bin_dict = {bins[i]:i for i in range(len(bins))}
        v = v.replace(bin_dict)
    else:
        bins = np.unique(v)

    if isinstance(v_intervals, (list, np.ndarray)) and len(bins) == len(v_intervals):
        bins = v_intervals

    return v, bins

def plot_prob_progression(x, y, x_intervals=7, use_quartiles=False,\
                          xlabel=None, ylabel=None, title=None, text=None, model=None, X_df=None, x_col=None,\
                         mean_line=False, figsize=(12,6), x_margin=0.01, color='Reds'):
    x = x.astype(int)
    y = y.astype(int)
    if isinstance(x, list): x = np.array(x)
    if isinstance(y, list): y = np.array(y)
    if (not isinstance(x, (str, pd.core.series.Series, np.ndarray))) or (not isinstance(y, (str, pd.core.series.Series, np.ndarray))):
        raise Exception("x and y must be either lists, pandas series or numpy arrays. x can be string when dataset is provided seperately")
    if (isinstance(x, (pd.core.series.Series, np.ndarray)) and (len(x.shape) != 1)) or ((isinstance(y, (pd.core.series.Series, np.ndarray))) and (len(y.shape) != 1)):
        raise Exception("x and y must have a single dimension")
    if (isinstance(x_intervals, (int)) and (x_intervals < 2)) or (isinstance(x_intervals, (list, np.ndarray)) and (len(x_intervals) < 2)):
        raise Exception("there must be at least two intervals to plot")
    if not np.isin(y.dtype, [int, float, 'int8', 'int16', 'int32', 'float16', 'float32']):
        raise Exception("y dimension must be a list, pandas series or numpy array of integers or floats")
    if max(y) == min(y):
        raise Exception("y dimension must have at least two values")
    elif len(np.unique(y)) == 2 and ((max(y) != 1) or (min(y) != 0)):
        raise Exception("y dimension if has two values must have a max of exactly 1 and min of exactly zero")
    elif len(np.unique(y)) > 2 and ((max(y) <= 1) or (min(y) >= 0)):
        raise Exception("y dimension if has more than two values must have range between between 0-1")
    x_use_continuous_bins = (model is not None) and (isinstance(x_intervals, (list, np.ndarray)))
    x, x_bins = discretize(x, x_intervals, use_quartiles, x_use_continuous_bins)
    x_range = [*range(len(x_bins))]
    plot_df = pd.DataFrame({'x':x_range})
    if (model is not None) and (X_df is not None) and (x_col is not None):
        preds = model.predict(X_df).squeeze()
        if len(np.unique(preds)) <= 2:
            preds = model.predict_proba(X_df)[:,1]
        x_, _ = discretize(X_df[x_col], x_intervals, use_quartiles, x_use_continuous_bins)
        xy_df = pd.DataFrame({'x':x_, 'y':preds})
    else:
        xy_df = pd.DataFrame({'x':x,'y':y})
    probs_df = xy_df.groupby(['x']).mean().reset_index()
    probs_df = pd.merge(plot_df, probs_df, how='left', on='x').fillna(0)

    x_bin_cnt = len(x_bins)
    l_width = 0.933
    r_width = 0.05
    w, h = figsize
    wp = (w-l_width-r_width)/9.27356902357
    xh_margin = ((wp-(x_margin*2))/(x_bin_cnt*2))+x_margin
    fig, (ax0, ax1) = plt.subplots(2, 1, figsize=figsize,\
                                   gridspec_kw={'height_ratios': [3, 1]})
    if title is not None:
        fig.suptitle(title, fontsize=21)
        ax0.text(0.61, 0.85, text,
                 horizontalalignment='left', verticalalignment='top', transform=ax0.transAxes, fontsize=9, fontstyle='italic')
        plt.subplots_adjust(top = 0.92, bottom=0.01, hspace=0.001, wspace=0.001)
    else:
        plt.subplots_adjust(top = 0.99, bottom=0.01, hspace=0.001, wspace=0.001)

    ax0.minorticks_on()
    # Disable grid for ax0
    ax0.grid(False)
    cmap = mpl.colormaps[color]
    num_segments = len(probs_df['y']) - 1

    for i in range(num_segments):
        segment = probs_df.iloc[i:i+2]
        color = cmap(i / num_segments)
        sns.lineplot(data=segment, x='x', y='y', marker='o', color=color, ax=ax0)

    # sns.lineplot(data=probs_df, x='x', y='y', marker='o', ax=ax0)
    ax0.set_ylabel('Probability', fontsize=15)
    ax0.set_xlabel('')

    if mean_line:
        ax0.axhline(y=xy_df.y.mean(), c='#E9EAE5', alpha=0.6, linestyle='dotted', label="mean")
        ax0.legend()

    
    colors = [cmap(i) for i in np.linspace(0, 1, len(x_bins))]

    # Disable grid for ax1
    ax1.grid(False)

    hist = sns.histplot(xy_df, x="x", stat='probability', bins=np.arange(x_bin_cnt+1)-0.5, ax=ax1)
    # color the bars using the color map
    for patch, color in zip(hist.patches, colors):
        patch.set_facecolor(color) # color depends on the index of the bar
    ax1.set_ylabel('Observations', fontsize=15)
    ax1.set_xlabel(xlabel, fontsize=15)
    ax1.xaxis.set_major_locator(plticker.MultipleLocator(base=1.0))
    ax1.set_xticklabels(['']+['(' + str(round(float(i.split(',')[0][1:]))) + ', ' + str(round(float(i.split(',')[1][:-1]))) + ']' for i in x_bins])
    ax1.margins(x=x_margin)
    plt.show()