import streamlit as st
import pandas as pd

st.write("# 1")

bg_combined = pd.DataFrame({
    't1': st.session_state.df_t1['severity'].value_counts(),
    't2': st.session_state.df_t2['severity'].value_counts(),
    'bb': st.session_state.df_bb['Severity'].value_counts()
})

st.write(bg_combined.head())

st.bar_chart(bg_combined.head(20000))