import streamlit as st
import pandas as pd
#st.title("Dead Page")

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

st.title("Create Your View")

dataset_option = st.selectbox(
    'Select a dataset:',
    (
        't1',
        't2',
        'bb'
    ))

# Sets up columns for the checkboxes
num_cols = 3
checked = []
cols = st.columns(num_cols)
column_names = st.session_state['df_' + dataset_option].columns.tolist()
for i, option in enumerate(column_names):
    checked.append(cols[i % num_cols].checkbox(option, key=option))

# Creates Output DataFrame
df_filtered = pd.DataFrame()
for i, name in enumerate(column_names):
    if checked[i]:
        df_filtered = pd.concat([df_filtered, st.session_state['df_' + dataset_option][name]], axis=1)

# Outputs DataFrames
st.write(df_filtered)
