import pandas as pd
import os

class DataLoader:
    def __init__(self, csv_path: str = "data/students_data.csv"):
        if not os.path.exists(csv_path):
            raise FileNotFoundError(f"Data file not found: {csv_path}")
        self.df = pd.read_csv(csv_path)
        self.df['quiz_date'] = pd.to_datetime(self.df['quiz_date'])

    def get_dataframe(self):
        return self.df.copy()