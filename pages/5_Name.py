import streamlit as st

st.title("Search by Asset Name")

input = st.text_input("Search", placeholder='Enter a keyword')

if input:
    valid_rows = st.session_state.df_t1[st.session_state.df_t1["asset.name"].str.contains(input, na=False, case=False)]
else:
    valid_rows = st.session_state.df_t1

st.write(valid_rows.reset_index(drop=True))