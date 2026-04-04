import streamlit as st
import pandas as pd

# MIGHT NEED TWO SEPARATE GRAPHS FOR T1T2 AND BB
# BB IS SORTED VIA RESOURCE
# may be able to store information as a value

# OLD CODE
# bg_combined = pd.DataFrame({
#     't1': st.session_state.df_t1['severity'].value_counts(),
#     't2': st.session_state.df_t2['severity'].value_counts(),
#     'bb': st.session_state.df_bb['Severity'].value_counts()
# })
#st.write(bg_combined.head())
#st.bar_chart(bg_combined.head(20000))

# Load all the data
# t12_dataframe = pd.DataFrame({
#     't1': st.session_state.df_t1['severity'].value_counts(),
#     't2': st.session_state.df_t2['severity'].value_counts(),
#     'bb': st.session_state.df_bb['Severity'].value_counts()
#
# })

# Load all data
t1_df = st.session_state['df_t1']
bb_df = st.session_state['df_bb']

# Convert nominal values to numeric values
severity_mapping = {"Info": 1, "Low": 2, "Medium": 3, "High": 4, "Critical": 5}
t1_df["severity_numerical"] = t1_df["severity"].map(severity_mapping)
state_mapping = {"NEW": 1, "ACTIVE": 2, "RESURFACED": 3}
t1_df["state_numerical"] = t1_df["state"].map(state_mapping)


# Present filtering options for t1 dataframe
options = st.multiselect(
    "What would you like to visualize?:",
    ["Port", "Severity", "State"]
)
items = st.slider("How many entries?", 1, len(t1_df.index))

# Change data based on selection
df_filtered = pd.DataFrame()
if options:

    if "Port" in options:
        df_filtered = pd.concat([df_filtered, t1_df["port"]], axis=1)
        # df_filtered = pd.merge(df_filtered, t1_df["port"], on="port")

    if "Severity" in options:
        df_filtered = pd.concat([df_filtered, t1_df["severity_numerical"]], axis=1)
        # df_filtered = pd.merge(df_filtered, t1_df["severity_numerical"], on="severity_numerical")

    if "State" in options:
        df_filtered = pd.concat([df_filtered, t1_df["state_numerical"]], axis=1)
        # df_filtered = pd.merge(df_filtered, t1_df["state_numerical"], on="state_numerical")


st.write(df_filtered.head(items))

# Render graphs
st.bar_chart(df_filtered.head(items))