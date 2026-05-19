import streamlit as st


files_uploaded = True

if st.session_state["df_t1"] is None:
    st.info("Please upload a t1 dataset file!")
    files_uploaded = False
if st.session_state["df_t2"] is None:
    st.info("Please upload a t2 dataset file!")
    files_uploaded = False
if st.session_state["df_bb"] is None:
    st.info("Please upload a bb dataset file!")
    files_uploaded = False

if not files_uploaded:
    st.write("All files must be uploaded for the dashboard to function. Please do so via the \"welcome\" page.")
    st.stop()

st.title("Search by Asset Name")

input = st.text_input("Search", placeholder='Enter a keyword')

if input:
    valid_rows = st.session_state.df_t1[st.session_state.df_t1["asset.name"].str.contains(input, na=False, case=False)]
else:
    valid_rows = st.session_state.df_t1

st.write(valid_rows.reset_index(drop=True))