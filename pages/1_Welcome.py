import streamlit as st
import pandas as pd
from streamlit.runtime.state import session_state





st.header("Vulnerability Dashboard")
st.write("By: Gjin Rexhaj, John Legge, Tyler Brown, Luis Sanchez, Jonathan Orlando")

st.subheader("Description:")
st.write("""
    This dashboard's purpose is to provide the necessary tools to holistically analyze data
    in such a way that allows the user to easily recognize and act on patterns. 
""")

st.subheader("Data:")
st.write("""
    The data dropdown and whats under it is meant to display the raw data to provide the user
    with a more digestible way to take in the full dataset with some simple insights.
""")

st.subheader("Tools:")
st.write("""
    The tools dropdown is meant to provide the user with more specific ways to manipulate the data.
    The tools include a way to search by each individual field, a way to customize a view of each dataset,
    and an asset name search. All these tools are built with the purpose of allowsing the user to look for
    specific details in the dataset in order to create more complex insights and conclusions.
""")

st.subheader("Risk Assessment:")
st.write("""
    Risk Assessment is meant to provide immediate insight into the top vulnerabilities based on their score of severity.
    Through the pages the user may identify key trends or patterns in the data depending on what is most present. This is
    meant to be used in tandem with the tools dropdown to do more fine tuning from this overview of the main vulnerabilities.
""")




t1_file = st.file_uploader("Upload t1_quantum_scrubbed.csv here", type="csv")
t2_file = st.file_uploader("Upload t2_quantum_scrubbed.csv here", type="csv")
bb_file = st.file_uploader("Upload BB_quantum_scrubbed.csv here", type="csv")



if t1_file is not None:
    print("t1 file uploaded!")
    st.session_state['df_t1'] = pd.read_csv(t1_file)
if t2_file is not None:
    print("t2 file uploaded!")
    st.session_state['df_t2'] = pd.read_csv(t2_file)
if bb_file is not None:
    print("bb file uploaded!")
    st.session_state['df_bb'] = pd.read_csv(bb_file)





# if t1_file or t2_file or bb_file is None:
#     st.info("Please upload all files to proceed.")
#     # st.stop() # Stops execution here so errors below don't trigger
#
#
#
# # Initialization for session state
# if 'df_t1' not in st.session_state and t1_file is not None:
#     #st.session_state['df_t1'] = pd.read_csv("data/t1_quantum_scrubbed.csv")
#     st.session_state['df_t1'] = pd.read_csv(t1_file)
#     print(f"st.session_state['df_t1']: {st.session_state['df_t1']}")
# elif 'df_t2' not in st.session_state and t2_file is not None:
#     #st.session_state['df_t2'] = pd.read_csv("data/t2_quantum_scrubbed.csv")
#     st.session_state['df_t2'] = pd.read_csv(t2_file)
#     print(f"st.session_state['df_t1']: {st.session_state['df_t2']}")
#
# elif 'df_bb' not in st.session_state and bb_file:
#     #st.session_state['df_bb'] = pd.read_csv("data/BB_quantum_scrubbed.csv")
#     st.session_state['df_bb'] = pd.read_csv(bb_file)
#     print(f"st.session_state['df_t1']: {st.session_state['df_t3']}")