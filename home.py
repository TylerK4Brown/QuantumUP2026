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