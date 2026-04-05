import streamlit as st
import pandas as pd
#st.title("Dead Page")

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
