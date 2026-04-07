import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home",
)

# Initialization for session state
if 'df_t1' not in st.session_state:
    st.session_state['df_t1'] = pd.read_csv("data/t1_quantum_scrubbed.csv")

if 'df_t2' not in st.session_state:
    st.session_state['df_t2'] = pd.read_csv("data/t2_quantum_scrubbed.csv")

if 'df_bb' not in st.session_state:
    st.session_state['df_bb'] = pd.read_csv("data/BB_quantum_scrubbed.csv")

# Navigation Logic and Order
pages = {
    "Introduction": [
        st.Page("pages/1_Welcome.py", title="Welcome")
    ],
    "Data": [
        st.Page("pages/2_Vulnerabilities_By_Port.py", title="Vulnerabilities by Port"),
        st.Page("pages/3_Vulnerabilities_By_Severity.py", title="Vulnerabilities by Severity"),
        st.Page("pages/4_Vulnerabilities_By_State.py", title="Vulnerabilities by State"),
        st.Page("pages/5_Vulnerabilities_By_Resource.py", title="Vulnerabilities by Resource"),
    ],
    "Tools": [
        st.Page("pages/3_Search_By_Field.py", title="Search By Field"),
        st.Page("pages/4_Custom_View.py", title="Custom View"),
        st.Page("pages/5_Name_Search.py", title="Name Search")
    ],
    "Risk Assessment": [
        st.Page("pages/6_Vulnerability_Assessment.py", title="Rationale"),
        st.Page("pages/7_Analysis.py", title="Analysis"),
    ]
}

pg = st.navigation(pages)
pg.run()