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
        self.df = df.copy()
        self.df['quiz_date'] = pd.to_datetime(self.df['quiz_date'], errors='coerce')

        self.llm = ChatGroq(
           model="llama-3.1-8b-instant",
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
            response = self.chain.invoke({"question": question})
            code = response.content if hasattr(response, 'content') else str(response)
            code = code.strip().strip("```python").strip("```").strip()

            print(f"\nGenerated Code:\n{code}\n")

            local_vars = {"df": self.df, "pd": pd, "result": None}
            exec(code, {}, local_vars)
            result = local_vars.get("result")

            if result is None:
                return pd.DataFrame({"error": ["LLM did not assign `result`."]})
            if not isinstance(result, pd.DataFrame):
                return pd.DataFrame({"error": ["Result is not a DataFrame."]})
            if result.empty:
                return pd.DataFrame({"info": ["No matching data found."]})

            return result.reset_index(drop=True)

        except Exception as e:
            return pd.DataFrame({"error": [f"Execution error: {str(e)}"]})