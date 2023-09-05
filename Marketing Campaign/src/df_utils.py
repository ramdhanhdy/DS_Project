import pandas as pd
import numpy as np
from IPython.display import display, Markdown


def printmd(string):
    display(Markdown(string))
    
def get_dataframe_summary(df, cat_list, dummy_list):
    """ Autogenerate a dataframe summary in addition to the dataframe-describe() function
    
        INPUTS: 
        ----------
            df -  (pandas dataframe) which should be described in an overview
            cat_list - (list) of all categorical input features
            dummy_list - (list) of all dummy input features 

        OUTPUTS:
        ----------
            No return
            print statements 
            text_for_readme.txt - an auto generated text document with df dataframe summary for the README 
           
    """
    
    number_nan = df.isnull().sum()
    printmd('### DataFrame Overview')
    printmd('- Dataset with {} observations and {} columns'.format(df.shape[0], df.shape[1]))
    
    text_for_readme = '## DataFrame Overview\n'
    text_for_readme += 'Dataset with {} observations and {} columns\n\n'.format(df.shape[0], df.shape[1])
    
    print('___________________________________')
    printmd('- **Numerical** columns:')
    
    text_for_readme += '- **Numerical** columns:\n\n'
    text_for_readme += '\t| column_name | type | min | max | number NaN | number unique | sample unique |\n\t| :-------------  | :-------------  | :-------------  | :-------------  | :-------------  | :-------------  |\n'
    row_num = []
    count_int = 0
    count_float = 0
    for col in df.columns.tolist():
        if (df[col].dtypes == 'float64' or df[col].dtypes == 'int64') and col not in cat_list and col not in dummy_list:
            row_num.append([col, df[col].dtypes, df[col].min(), df[col].max(), number_nan[col], df[col].nunique(), df[col].unique()[:5]])
            text_for_readme +=('\t| ' + str(col) + ' | ' + str(df[col].dtypes) + ' | ' + str(df[col].min()) + ' | ' + str(df[col].max()) + ' | '+ str(number_nan[col]) + ' | ' + str(df[col].nunique()) + ' | ' + str(df[col].unique()[:5]) + ' |\n') 
            if df[col].dtypes == 'int64':
                count_int += 1
            if df[col].dtypes == 'float64':
                count_float += 1
    df_num = pd.DataFrame(row_num,columns=['column_name', 'type', 'min', 'max', 'number NaN', 'number unique', 'sample unique'])
    text_for_readme +='\n\n'
    display(df_num)

    print('___________________________________')
    printmd('- **Categorical** columns:')
    
    text_for_readme += '- **Categorical** columns:\n\n'
    text_for_readme += '\t| column_name | type | min | max | number NaN | number unique | sample unique |\n\t| :-------------  | :-------------  | :-------------  | :-------------  | :-------------  | :-------------  |\n'
    row_cat = []
    count_object = 0
    for col in df.columns.tolist():
        if df[col].dtypes == 'object' or col in cat_list:
            try:
                row_cat.append([col, df[col].dtypes, df[col].min(), df[col].max(), number_nan[col], df[col].nunique(), df[col].unique()[:5]])
                text_for_readme +=('\t| ' + str(col) + ' | ' + str(df[col].dtypes) + ' | ' + str(df[col].min()) + ' | ' + str(df[col].max()) + ' | '+ str(number_nan[col]) + ' | ' + str(df[col].nunique()) + ' | ' + str(df[col].unique()[:5]) + ' |\n') 
            except:
                row_cat.append([col, df[col].dtypes, 'NaN', 'NaN', number_nan[col], df[col].nunique(), df[col].unique()[:5]])
                text_for_readme +=('\t| ' + str(col) + ' | ' + str(df[col].dtypes) + ' | '+ 'NaN' + ' | '+ 'NaN' + ' | '+ str(number_nan[col]) + ' | ' + str(df[col].nunique()) + ' | ' + str(df[col].unique()[:5]) + ' |\n') 
            count_object += 1
    df_cat = pd.DataFrame(row_cat,columns=['column_name', 'type', 'min', 'max', 'number NaN', 'number unique', 'sample unique'])
    text_for_readme +='\n\n'
    display(df_cat)

    print('___________________________________')
    printmd('- **Dummy** columns:')
    
    text_for_readme += '- **Dummy** columns:\n\n'
    text_for_readme += '\t| column_name | type | min | max | number NaN | number unique | sample unique |\n\t| :-------------  | :-------------  | :-------------  | :-------------  | :-------------  | :-------------  |\n'
    row_dummy = []
    for col in dummy_list:
        if (df[col].dtypes == 'float64' or df[col].dtypes == 'int64'):
            row_dummy.append([col, df[col].dtypes, df[col].min(), df[col].max(), number_nan[col], df[col].nunique(), df[col].unique()[:5]])
            text_for_readme +=('\t| ' + str(col) + ' | ' + str(df[col].dtypes) + ' | ' + str(df[col].min()) + ' | ' + str(df[col].max()) + ' | '+ str(number_nan[col]) + ' | ' + str(df[col].nunique()) + ' | ' + str(df[col].unique()[:5]) + ' |\n')
    df_dummy = pd.DataFrame(row_dummy,columns=['column_name', 'type', 'min', 'max', 'number NaN', 'number unique', 'sample unique'])
    text_for_readme +='\n\n'
    display(df_dummy)
    
    print('___________________________________')
    printmd('- There are ***{} numerical*** ({}x int and {}x float) columns'.format(count_int + count_float, count_int, count_float))
    printmd('- There are ***{} categorical*** columns'.format(count_object))
    printmd('- There are ***{} dummy*** columns'.format(len(dummy_list)))
    
    print('___________________________________')
    printmd('- There are ***{} numerical*** ({}x int and {}x float) columns\n'.format(count_int + count_float, count_int, count_float))
    printmd('- There are ***{} categorical*** columns\n'.format(count_object))
    printmd('- There are ***{} dummy*** columns\n'.format(len(dummy_list)))
    printmd('- There are ***{} missing values*** in total in the dataset\n'.format(df.isnull().values.sum()))
    
    with open('text_for_readme.txt', 'w') as f:
        f.write(text_for_readme)

def count_rows_with_blankspace(df):
    """
    This function takes a Pandas DataFrame as input and returns a new DataFrame with the number of rows
    having a blankspace as value for each column.
    """
    missing_counts = df.astype(str).apply(lambda x: x.str.isspace().sum())
    missing_df = pd.DataFrame({'Missing Rows': missing_counts}).sort_values(by='Missing Rows', ascending=False)
    return missing_df

def replace_blankspace_with_nan(df):
    """
    This function takes a Pandas DataFrame as input and replaces any rows with blank spaces with NaN values.
    """
    df = df.replace(r'^\s*$', np.nan, regex=True)
    return df

def dataframe_info(df):
    report = pd.DataFrame(columns=['Column', 'Data Type', 'Unique Count', 'Unique Sample', 'Missing Values', 'Missing Percentage'])
    for column in df.columns:
        data_type = df[column].dtype
        unique_count = df[column].nunique()
        unique_sample = df[column].unique()[:5]
        missing_values = df[column].isnull().sum()
        missing_percentage = (missing_values / len(df)) * 100
        report = pd.concat([report, pd.DataFrame({'Column': [column],
                                                      'Data Type': [data_type],
                                                      'Unique Count': [unique_count],
                                                      'Unique Sample': [unique_sample],
                                                      'Missing Values': [missing_values],
                                                      'Missing Percentage': [missing_percentage.round(4)]})],
                             ignore_index=True)
    return report