import streamlit as st

st.title("Keyword Search")

option = st.selectbox(
    'Select a field:',
    (
        'Resource Name',
        'Cloud Provider ID',
        'Native Type', 'Tags',
        'Policy Name', 'Severity',
        'Result',
        'Compliance Check Name',
        'Category',
        'Remediation Steps',
        'Assessed At',
        'Subscription Name',
        'Subscription Provider ID'
    ))

input = st.text_input("Search", placeholder='Enter a keyword')

if input:
    valid_rows = st.session_state.df_bb[st.session_state.df_bb[option].str.contains(input, na=False, case=False)]
else:
    valid_rows = st.session_state.df_bb

st.write(valid_rows.reset_index(drop=True))