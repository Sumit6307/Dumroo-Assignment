# src/query_engine.py
from langchain_groq import ChatGroq
from langchain.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from .prompts import SQL_SYSTEM_PROMPT
import pandas as pd
from dotenv import load_dotenv
import os

load_dotenv()

class QueryEngine:
    def __init__(self, df: pd.DataFrame):
        self.df = df
        self.llm = ChatGroq(
            model="llama3-8b-8192",
            temperature=0,
            groq_api_key=os.getenv("GROQ_API_KEY")
        )
        self.parser = StrOutputParser()

        self.prompt = ChatPromptTemplate.from_messages([
            ("system", SQL_SYSTEM_PROMPT),
            ("human", "{question}")
        ])
        self.chain = self.prompt | self.llm | self.parser

    def ask(self, question: str):
        try:
            code = self.chain.invoke({"question": question})
            if hasattr(code, 'content'):
                code = code.content
            code = code.strip().strip("```python").strip("```")
            print(f"Generated Code:\n{code}")

            local_vars = {"df": self.df, "pd": pd}
            exec(code, {}, local_vars)
            result = local_vars.get('result')

            if result is None:
                # Fallback: extract result from last line
                lines = code.strip().split('\n')
                last_expr = lines[-1].strip()
                if not last_expr.startswith('df'):
                    exec("result = " + last_expr, {}, local_vars)
                    result = local_vars.get('result')

            return result if isinstance(result, pd.DataFrame) else pd.DataFrame([{"error": "No result"}])
        except Exception as e:
            return pd.DataFrame({"error": [f"Query failed: {str(e)}"]})