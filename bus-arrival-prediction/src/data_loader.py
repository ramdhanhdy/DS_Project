from abc import ABC, abstractmethod
import pandas as pd

class DataLoader(ABC):
    @abstractmethod
    def load_data(self, file_path):
        pass

class CSVDataLoader(DataLoader):
    def load_data(self, file_path):
        return pd.read_csv(file_path)

class ExcelDataLoader(DataLoader):
    def load_data(self, file_path):
        return pd.read_excel(file_path)

def create_loader(file_type):
    if file_type == 'csv':
        return CSVDataLoader()
    elif file_type == 'excel':
        return ExcelDataLoader()
    else:
        raise ValueError(f"Unsupported file type: {file_type}")