import streamlit as st
import pandas as pd

st.set_page_config(
    page_title="Home",
)

st.write("# Welcome!")

# Initialization for session state
if 'df_t1' not in st.session_state:
    st.session_state['df_t1'] = pd.read_csv("data/t1_quantum_scrubbed.csv")

if 'df_t2' not in st.session_state:
    st.session_state['df_t2'] = pd.read_csv("data/t2_quantum_scrubbed.csv")

if 'df_bb' not in st.session_state:
    st.session_state['df_bb'] = pd.read_csv("data/BB_quantum_scrubbed.csv")

# Navigation Logic and Order
pages = {
    "Data": [
        st.Page("pages/2_Data_Visualizer.py", title="Visualizer")
    ],
    "Keyword Search": [
        st.Page("pages/3_Policy_Name.py", title="Policy Name"),
        st.Page("pages/4_Resource_Name.py", title="Resource Name"),
        st.Page("pages/5_Name.py", title="Name")
    ],
    "Risk Assessment": [
        st.Page("pages/6_Vulnerability_Assessment.py", title="Rationale"),
        st.Page("pages/7_Analysis.py", title="Analysis"),
    ],
    "Results": [
        st.Page("pages/8_Solution.py", title="Solution")
    ],
}

pg = st.navigation(pages)
pg.run()