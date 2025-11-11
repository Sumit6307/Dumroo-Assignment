import pandas as pd
import os

class DataLoader:
    def __init__(self, csv_path: str = "data/students_data.csv"):
        self.df = pd.read_csv(csv_path)
        self.df['quiz_date'] = pd.to_datetime(self.df['quiz_date'])

    def get_dataframe(self):
        return self.df.copy()