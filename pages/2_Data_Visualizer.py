import streamlit as st
import altair as alt


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



# SEVERITY CHART
st.divider()
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



# STATE CHART
st.divider()
state_counts = t1_df.groupby(['status', 'severity']).size().reset_index(name='count')
st.subheader("Vulnerabilities by State")
zoom_pan_state = alt.selection_interval(bind='scales')
state_chart = alt.Chart(state_counts).mark_bar().encode(
    x=alt.X('status:N', title='State'),
    y=alt.Y('count:Q', title='Number of Vulnerabilities'),
    color=alt.Color('severity:N', title='Severity'),
    tooltip=['status', 'severity', 'count']
).add_selection(
    zoom_pan_state
)
st.altair_chart(state_chart, use_container_width=True)

show_table_3 = st.checkbox("Show vulnerabilities by state table")
if show_table_3:
    st.dataframe(state_counts)



# TODO: DISPLAY DATA BB RESOURCE FOR BB TABLE