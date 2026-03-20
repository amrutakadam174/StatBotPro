import streamlit as st
import pandas as pd
from agent.pandas_agent import analyze_data

# Page settings
st.set_page_config(page_title="StatBot Pro", layout="wide")

# Title
st.title("📊 StatBot Pro - AI Data Analyst")

st.write("Upload your CSV file and ask questions about your data.")

# File upload
uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])

if uploaded_file is not None:
    
    # Read file
    df = pd.read_csv(uploaded_file)

    st.subheader("📁 Data Preview")
    st.dataframe(df.head())

    # User input
    query = st.text_input("💬 Ask your question (e.g., mean, max, min)")

    # Button
    if st.button("Analyze"):
        if query:
            result = analyze_data(df, query)
            
            st.subheader("📊 Result")
            st.write(result)
        else:
            st.warning("Please enter a question!")