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



# SHOW VULNERABILITIES BY PORT
st.subheader("Vulnerabilities by Port")
min_port = int(port_status_counts['port'].min())
max_port = int(port_status_counts['port'].max())
port_range = st.slider("Select port range", min_value=min_port, max_value=max_port, value=(min_port, max_port))
filtered_data = port_status_counts[(port_status_counts['port'] >= port_range[0]) &
                                   (port_status_counts['port'] <= port_range[1])]
st.write(f"Showing ports from {port_range[0]} to {port_range[1]}")

sort_by_total = st.checkbox("Sort ports by total vulnerabilities (highest first)", value=False)
port_totals = filtered_data.groupby('port')['count'].sum().reset_index(name='total_count')

if sort_by_total:
    sorted_ports = port_totals.sort_values('total_count', ascending=False)['port'].tolist()
else:
    sorted_ports = sorted(port_totals['port'].tolist())

zoom_pan = alt.selection_interval(bind='scales')
color=alt.Color('status:N', title='Status', scale=alt.Scale(domain=['ACTIVE','NEW'], range=['red','blue']))
chart = alt.Chart(filtered_data).mark_bar().encode(
    x=alt.X('port:O', title='Port', sort=sorted_ports),
    y=alt.Y('count:Q', title='Number of Vulnerabilities'),
    color=alt.Color(
        'status:N',
        title='Status',
        scale=alt.Scale(
            domain=['ACTIVE','NEW','RESURFACED'],  # include all statuses
            range=['red','blue','orange']          # assign colors
        )
    ),
    tooltip=['port','status','count']
).add_selection(
    zoom_pan
)
st.altair_chart(chart, use_container_width=True)

show_table_1 = st.checkbox("Show vulnerabilities by port table")
if show_table_1:
    st.dataframe(port_status_counts)
