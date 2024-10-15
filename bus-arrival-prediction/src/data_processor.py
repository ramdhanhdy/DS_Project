from abc import ABC, abstractmethod
import pandas as pd
import calendar

class DataProcessor(ABC):
    @abstractmethod
    def process_data(self, df):
        pass

class StandardDataProcessor(DataProcessor):
    def process_data(self, df):
        df = self._drop_columns(df)
        df = self._convert_coordinates(df)
        df = self._convert_time(df)
        df = self._extract_time_features(df)
        return df

    def _drop_columns(self, df):
        return df.drop(['flag', 'speed', 'imei', 'bus_id'], axis=1)

    def _convert_coordinates(self, df):
        df['latitude'] = pd.to_numeric(df['latitude'].astype(str).str.replace(',', '.'), errors='coerce')
        df['longitude'] = pd.to_numeric(df['longitude'].astype(str).str.replace(',', '.'), errors='coerce')
        return df

    def _convert_time(self, df):
        df['time'] = pd.to_datetime(df['time'], format='%Y-%m-%d %H:%M:%S')
        return df.sort_values(by=['route_id', 'time'])

    def _extract_time_features(self, df):
        df['hour'] = df['time'].dt.hour
        df['weekday'] = df['time'].dt.weekday
        df['day_name'] = df['time'].dt.day_name()
        df['month'] = df['time'].dt.month
        df['month_name'] = df['month'].apply(lambda x: calendar.month_name[x])
        return df

class CorrectionFactorDataProcessor(StandardDataProcessor):
    def __init__(self, correction_factor):
        self.correction_factor = correction_factor

    def process_data(self, df):
        df = super().process_data(df)
        df['latitude'] = df['latitude'] / self.correction_factor
        df['longitude'] = df['longitude'] / self.correction_factor
        return df

def create_processor(correction_factor=None):
    if correction_factor:
        return CorrectionFactorDataProcessor(correction_factor)
    else:
        return StandardDataProcessor()