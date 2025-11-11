import pandas as pd

class RoleManager:
    def __init__(self, admin_grade: str):
        self.admin_grade = admin_grade.replace("Grade ", "")

    def apply_scope(self, query: str) -> str:
        return f"{query} Only include data for Grade {self.admin_grade}."

    def filter_df(self, df: pd.DataFrame) -> pd.DataFrame:
        return df[df['grade'] == int(self.admin_grade)].copy()