import streamlit as st
import altair as alt

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

st.set_page_config(layout="wide")



# LOAD AND PROCESS ALL DATA
t1_df = st.session_state['df_t1']
bb_df = st.session_state['df_bb']
t1_df.columns = [
    'uuid', 'asset_id', 'asset_name', 'description', 'category',
    'plugin_id', 'plugin_name', 'field1', 'field2', 'service_uuid',
    'port', 'protocol', 'severity', 'status'
]
port_status_counts = t1_df.groupby(['port', 'status']).size().reset_index(name='count')


# SEVERITY CHART
severity_counts = t1_df.groupby(['severity', 'status']).size().reset_index(name='count')
st.subheader("Vulnerabilities by Severity")
zoom_pan_sev = alt.selection_interval(bind='scales')
color=alt.Color('status:N', title='Status',
                scale=alt.Scale(domain=['ACTIVE','NEW'], range=['red','blue']))
severity_chart = alt.Chart(severity_counts).mark_bar().encode(
    x=alt.X('severity:N', title='Severity'),
    y=alt.Y('count:Q', title='Number of Vulnerabilities'),
    color=alt.Color(
        'status:N',
        title='Status',
        scale=alt.Scale(
            domain=['ACTIVE', 'NEW', 'RESURFACED'],  # include all statuses
            range=['red', 'blue', 'orange']
        )
    ),
    tooltip=['severity', 'status', 'count']
).add_selection(
    zoom_pan_sev
)
st.altair_chart(severity_chart, use_container_width=True)

show_table_2 = st.checkbox("Show severity count table")
if show_table_2:
    st.dataframe(severity_counts)