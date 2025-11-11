import streamlit as st
from src.data_loader import DataLoader
from src.query_engine import QueryEngine
from src.role_manager import RoleManager
import pandas as pd

st.set_page_config(page_title="Dumroo Admin Panel", layout="wide")
st.title("Dumroo Admin Panel - Ask in English")

# === Session State ===
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False

# === Sidebar Login ===
with st.sidebar:
    st.header("Admin Login")
    admin_name = st.text_input("Name", "Ms. Sharma")
    admin_grade = st.selectbox("Your Grade", ["Grade 7", "Grade 8", "Grade 9"])
    
    if st.button("Login"):
        st.session_state.logged_in = True
        st.session_state.admin_grade = admin_grade
        st.session_state.admin_name = admin_name
        st.success(f"Logged in as {admin_name}")

if not st.session_state.get("logged_in"):
    st.info("Please log in from the sidebar.")
    st.stop()

# === Load Data ===
@st.cache_data
def load_data():
    return DataLoader().get_dataframe()

df = load_data()
role = RoleManager(st.session_state.admin_grade)
df_scoped = role.filter_df(df)

st.write(f"**Scope:** {st.session_state.admin_grade} | **Students:** {len(df_scoped)}")

# === Query Engine ===
engine = QueryEngine(df_scoped)

question = st.text_input(
    "Ask about your students:",
    placeholder="e.g., Who hasn’t submitted homework?"
)

if question:
    with st.spinner("Thinking..."):
        scoped_question = role.apply_scope(question)
        result = engine.ask(scoped_question)

    if 'error' in result.columns:
        st.error("Query Failed")
        st.code(result['error'].iloc[0])
    elif 'info' in result.columns:
        st.warning(result['info'].iloc[0])
    else:
        st.success(f"Found {len(result)} record(s)")
        st.dataframe(result, use_container_width=True)
        
        csv = result.to_csv(index=False).encode()
        st.download_button(
            "Export to CSV",
            data=csv,
            file_name="result.csv",
            mime="text/csv"
        )