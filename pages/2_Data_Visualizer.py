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


numerical = st.checkbox("Convert nominal data to numerical data?")

if numerical:
    # Convert nominal values to numeric values
    severity_mapping = {"Info": 1, "Low": 2, "Medium": 3, "High": 4, "Critical": 5}
    t1_df["severity_copy"] = t1_df["severity"].map(severity_mapping)
    state_mapping = {"NEW": 1, "ACTIVE": 2, "RESURFACED": 3}
    t1_df["state_copy"] = t1_df["state"].map(state_mapping)
else:
    t1_df["severity_copy"] = t1_df["severity"]
    t1_df["state_copy"] = t1_df["state"]

# Present filtering options for t1 dataframe
options = st.multiselect(
    "What would you like to visualize?",
    ["Port", "Severity", "State"]
)


min_num = 0
max_num = 100

st.write(f"Dataset size: [0 : {t1_df.index.stop}]")
col1, col2 = st.columns(2)
with col1:
    min_num = st.number_input("Min", min_value=0, max_value=len(t1_df.index-1), value=0)
with col2:
    max_num = st.number_input("Max", min_value=1, max_value=len(t1_df.index), value=100)


# Change data based on selection
df_port = pd.DataFrame()
df_severity = pd.DataFrame()
df_state = pd.DataFrame()

if options:
    if "Port" in options:
        df_port = pd.concat([df_port, t1_df["port"]], axis=1)
        st.bar_chart(df_port.iloc[min_num: max_num])

    if "Severity" in options:
        df_severity = pd.concat([df_severity, t1_df["severity_copy"]], axis=1)
        st.bar_chart(df_severity.iloc[min_num: max_num])

    if "State" in options:
        df_state = pd.concat([df_state, t1_df["state_copy"]], axis=1)
        st.bar_chart(df_state.iloc[min_num: max_num])