import streamlit as st
from src.data_loader import DataLoader
from src.query_engine import QueryEngine
from src.role_manager import RoleManager
import pandas as pd

st.set_page_config(page_title="Dumroo Admin Panel", layout="wide")
st.title("🌀 Dumroo Admin Panel - Ask in English")

# Admin Login Simulation
with st.sidebar:
    st.header("Admin Login")
    admin_name = st.text_input("Name", "Ms. Sharma")
    admin_grade = st.selectbox("Your Grade", ["Grade 7", "Grade 8", "Grade 9"])
    if st.button("Login"):
        st.session_state.logged_in = True
        st.session_state.admin_grade = admin_grade
        st.success(f"Logged in as {admin_name} ({admin_grade})")

if not st.session_state.get("logged_in"):
    st.info("Please log in from the sidebar.")
    st.stop()

# Load data
@st.cache_data
def load_data():
    return DataLoader().get_dataframe()

df = load_data()
role = RoleManager(st.session_state.admin_grade)
df_scoped = role.filter_df(df)

st.write(f"**Your Scope:** {st.session_state.admin_grade} | Total Students: {len(df_scoped)}")

# Query Engine
engine = QueryEngine(df_scoped)

question = st.text_input(
    "Ask a question about your students:",
    placeholder="e.g., Which students haven’t submitted homework?"
)

if question:
    with st.spinner("Thinking..."):
        scoped_question = role.apply_scope(question)
        result = engine.ask(scoped_question)

    if not result.empty and 'error' not in result.columns:
        st.success("Results:")
        st.dataframe(result, use_container_width=True)
    else:
        st.error("No results or error in query.")