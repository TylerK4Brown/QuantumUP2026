import streamlit as st
import pandas as pd

st.write("# 1")

df_t1 = pd.read_csv("data/t1_quantum_scrubbed.csv")
df_t2 = pd.read_csv("data/t2_quantum_scrubbed.csv")
df_bb = pd.read_csv("data/BB_quantum_scrubbed.csv")

bg_combined = pd.DataFrame({
    't1': df_t1['severity'].value_counts(),
    't2': df_t2['severity'].value_counts(),
    'bb': df_bb['Severity'].value_counts()
})

st.write(bg_combined.head())

st.bar_chart(bg_combined.head(20000))