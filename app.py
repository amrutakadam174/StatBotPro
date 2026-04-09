import streamlit as st
import pandas as pd
from agent.pandas_agent import analyze_data

# Page settings
st.set_page_config(
    page_title="StatBot Pro",
    layout="wide",
    page_icon="📊"
)

# Title
st.title("📊 StatBot Pro - AI Data Analyst")
st.caption("Upload your CSV file and ask intelligent questions about your data")

# Sidebar
st.sidebar.title("📌 Instructions")
st.sidebar.write("""
1. Upload a CSV file  
2. View data preview  
3. Ask questions like:
   - How many rows?
   - Mean of Sales
   - Max Profit
   - Minimum Revenue
   - Minimum Quantity
   - Plot Sales graph
   - Graph Category
   - And more!
""")

# File upload
uploaded_file = st.file_uploader("📁 Upload CSV File", type=["csv"])

if uploaded_file is not None:
    try:
        # 🔹 Read CSV
        df = pd.read_csv(uploaded_file, encoding='latin1', on_bad_lines='skip')

        # 🔥 IMPORTANT: CLEAN NUMERIC COLUMNS
        for col in df.columns:
            if df[col].dtype == 'object':
                try:
                    df[col] = df[col].astype(str)
                    df[col] = df[col].str.replace("₹", "")
                    df[col] = df[col].str.replace(",", "")
                    df[col] = pd.to_numeric(df[col], errors='ignore')
                except:
                    pass

        st.success("✅ File uploaded successfully!")

        # Layout
        col1, col2 = st.columns(2)

        with col1:
            st.subheader("📊 Data Preview")
            st.dataframe(df.head())

        with col2:
            st.subheader("📌 Dataset Info")
            st.write(f"Rows: {df.shape[0]}")
            st.write(f"Columns: {df.shape[1]}")
            st.write("Column Names:")
            st.write(list(df.columns))

            # Helpful for user
            st.info(f"💡 Available columns: {', '.join(df.columns)}")

        # Query section
        st.subheader("💬 Ask Your Question")
        query = st.text_input("Type your query here...")

        if st.button("🚀 Analyze"):
            if query:
                result = analyze_data(df, query)

                st.subheader("📈 Result")

                # ✅ GRAPH OUTPUT (Matplotlib)
                if isinstance(result, dict) and result.get("type") == "graph":
                    st.image(result["path"], caption="Generated Graph")

                # ✅ TEXT OUTPUT
                else:
                    st.success(str(result))

            else:
                st.warning("⚠️ Please enter a question!")

    except Exception as e:
        st.error(f"❌ Error reading file: {e}")

else:
    st.info("⬆️ Please upload a CSV file to begin.")