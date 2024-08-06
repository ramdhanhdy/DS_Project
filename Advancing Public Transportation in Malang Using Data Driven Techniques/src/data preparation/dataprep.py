import pandas as pd
import numpy as np 
import calendar

def load_and_preprocess_data(file_path, file_type='csv', correction_factor=None):
    # Load data
    if file_type == 'csv':
        df = pd.read_csv(file_path)
    elif file_type == 'excel':
        df = pd.read_excel(file_path)

    # Drop unnecessary columns
    df.drop(['flag', 'speed', 'imei', 'bus_id'], axis=1, inplace=True)

    # Convert latitude and longitude to numeric, handling different possible formats
    def convert_to_numeric(x):
        if isinstance(x, (int, float)):
            return x
        elif isinstance(x, str):
            return pd.to_numeric(x.replace(',', '.'), errors='coerce')
        else:
            return np.nan

    df['latitude'] = df['latitude'].apply(convert_to_numeric)
    df['longitude'] = df['longitude'].apply(convert_to_numeric)

    # Correct latitude and longitude if needed
    if correction_factor:
        df['latitude'] = df['latitude'] / correction_factor
        df['longitude'] = df['longitude'] / correction_factor

    # Convert 'time' to datetime and sort data
    df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
    df.sort_values(by=['route_id', 'time'], inplace=True)

    # Extract time-related features
    df['hour'] = df['time'].dt.hour
    df['weekday'] = df['time'].dt.weekday
    df['day_name'] = df['time'].dt.day_name()
    df['month'] = df['time'].dt.month
    
    # Apply a lambda function to convert month numbers to names
    df['month_name'] = df['month'].apply(lambda x: calendar.month_name[x])

    return df

def remove_weekend_data(df):
    df = df[df['weekday'].isin([0, 1, 2, 3, 4])]


