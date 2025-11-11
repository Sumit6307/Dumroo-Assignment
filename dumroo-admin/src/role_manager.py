from typing import Dict, Any

class RoleManager:
    def __init__(self, admin_grade: str):
        self.admin_grade = admin_grade

    def apply_scope(self, query: str) -> str:
        return f"{query} Only include data for Grade {self.admin_grade}."

    def filter_df(self, df):
        return df[df['grade'] == int(self.admin_grade.replace("Grade ", "")) if "Grade" in self.admin_grade else self.admin_grade]