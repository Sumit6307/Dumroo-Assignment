import pandas as pd
import os

class DataLoader:
    def __init__(self, csv_path: str = "data/students_data.csv"):
        # FIX: Go UP one level from src/ to project root
        base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
        full_path = os.path.join(base_dir, csv_path)
        
        if not os.path.exists(full_path):
            raise FileNotFoundError(f"Data file not found: {full_path}")
        
        self.df = pd.read_csv(full_path)
        self.df['quiz_date'] = pd.to_datetime(self.df['quiz_date'])

    def get_dataframe(self):
        return self.df.copy()