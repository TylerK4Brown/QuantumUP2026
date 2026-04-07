import streamlit as st
import pandas as pd
from ollama import Client

st.title('Vulnerability Analysis')
st.subheader("This page provides a small analysis of why these vulnerabilities are critical in a PQC environment.")
st.subheader("Select a resource name from the drop-down menu to receive a vulnerability briefing for that resource: ")
df_bbtable_severities = st.session_state['df_bbtable_severities']
df_bbtable = st.session_state['df_bb']

# Creates an option selection for the top 10 resources with the most failed assessments of severity 'Medium'.
resource_names = df_bbtable_severities.sort_values(by=['MEDIUM', 'LOW', 'INFORMATIONAL'], ascending=False).head(10)['Resource Name'].tolist()
option = st.selectbox(
    label="Resource name",
    options=resource_names
)

# Load the policy names and the single native type into a list
df_bbtable_resource = df_bbtable[df_bbtable['Resource Name'] == option]
df_bbtable_policynames = df_bbtable_resource['Policy Name'].unique().tolist()
df_bbtable_nativetype = df_bbtable_resource['Native Type'].unique().tolist()

# Display native types and policy names for the resource selected by the user
for nativetype in df_bbtable_nativetype:
    st.markdown(f"Native Type of this resource: **{nativetype}**")

st.write("**Policy Names associated with this resource:**")
for policy in df_bbtable_policynames:
    st.write(f"{policy}.")

# AI Vulnerability Briefing
# Once this page loads, an AI-generated vulnerability briefing will be displayed on the app
# ALl of the code is referenced directly from Ollama's documentation: https://ollama.com/docs/api-reference/client-chat
# This link will teach you how to create an Ollama API key so you can fill it in here
client = Client(
    host="https://ollama.com",
    headers={'Authorization': 'Bearer ' + '546abedea6394b8da5aba49756f94c0e.HjoRHEIsE-zWCyGj3LC757L3'}
)

# System prompt provides instructions to the model on how to generate the vulnerability briefing
# User prompt provides the model with the resource name, policy names and native types
# The model will use this information to generate a quick vulnerability briefing
messages = [
    {
        "role": "system", 
        "content": '''You are a cybersecurity analyst helper, and you are analyzing a business in a post-quantum cryptography (PQC) environment.
        Given a resource that has failed certain assessments, you will provide a vulnerability briefing that explains the potential risks associated with these failed assessments and the native type of the resource in a PQC environment.
        The briefing should extend no further than 6 sentences. Please provide references to NIST where applicable. Reference the section as well.
        If you are referencing a specific NIST section, please provide a link to the section as well.
        Put newlines between each sentence in the briefing.'''
        },
    {
        "role": "user", 
        "content": f"The resource '{option}' has failed the following assessments: {', '.join(df_bbtable_policynames)}. The native type of this resource is {', '.join(df_bbtable_nativetype)}. Please provide a vulnerability briefing that explains the potential risks associated with these failed assessments."}
]

st.markdown("#### **Loading an AI-generated vulnerability briefing...**")
response = client.chat('glm-5:cloud', messages=messages, stream=False)
st.markdown(response.message.content)