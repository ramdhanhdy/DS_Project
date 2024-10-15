import pandas as pd
import os
from src.data_loader import create_loader
from src.data_processor import create_processor

class DataPreparationPipeline:
    def __init__(self, loader, processor):
        self.loader = loader
        self.processor = processor

    def prepare_data(self, file_path):
        df = self.loader.load_data(file_path)
        return self.processor.process_data(df)

def create_pipeline(file_type, correction_factor=None):
    loader = create_loader(file_type)
    processor = create_processor(correction_factor)
    return DataPreparationPipeline(loader, processor)

def prepare_all_data(data_dir):
    feb_pipeline = create_pipeline('csv')
    march_pipeline = create_pipeline('excel', correction_factor=100000)
    april_pipeline = create_pipeline('csv')
    may_pipeline = create_pipeline('csv')

    feb_df = feb_pipeline.prepare_data(os.path.join(data_dir, 'location_data_Feb2024.csv'))
    march_df = march_pipeline.prepare_data(os.path.join(data_dir, 'data_march_2024.xlsx'))
    april_df = april_pipeline.prepare_data(os.path.join(data_dir, 'data_april.csv'))
    may_df = may_pipeline.prepare_data(os.path.join(data_dir, 'location_data_May2024.csv'))

    merged_df = pd.concat([feb_df, march_df, april_df, may_df])
    merged_df.reset_index(drop=True, inplace=True)

    filtered_df = merged_df[merged_df['weekday'].isin([0, 1, 2, 3, 4])]
    return filtered_df

def main():
    data_dir = 'D:\\CDS590\\data\\raw'
    prepared_data = prepare_all_data(data_dir)
    print(f"Prepared data shape: {prepared_data.shape}")
    return prepared_data

if __name__ == "__main__":
    main()