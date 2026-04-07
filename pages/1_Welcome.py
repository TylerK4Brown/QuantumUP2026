import streamlit as st

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