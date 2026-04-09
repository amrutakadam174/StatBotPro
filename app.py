import streamlit as st
import pandas as pd
from agent.pandas_agent import analyze_data

# ================== PAGE CONFIG ==================
st.set_page_config(page_title="StatBot Pro", layout="wide", page_icon="📊")

# ================== CUSTOM UI ==================
st.markdown("""
<style>
.main {background-color: #f8fafc;}
h1 {text-align:center; color:#1e293b;}
.stButton>button {
    width: 100%;
    border-radius: 8px;
    height: 2.6em;
    background-color: #4CAF50;
    color: white;
    font-weight: bold;
}
.stButton>button:hover {
    background-color: #45a049;
}
</style>
""", unsafe_allow_html=True)

# ================== HEADER ==================
st.markdown("""
<h1>📊 StatBot Pro</h1>
<p style='text-align:center; color:gray;'>
AI Data Analyst • Ask Questions • Get Insights
</p>
""", unsafe_allow_html=True)

st.divider()

# ================== SESSION ==================
if "history" not in st.session_state:
    st.session_state.history = []

if "selected_query" not in st.session_state:
    st.session_state.selected_query = ""

# ================== SIDEBAR ==================
st.sidebar.title("⚡ Quick Actions")

def set_query(q):
    st.session_state.selected_query = q

# 📊 Sales
st.sidebar.markdown("### 📊 Sales")
st.sidebar.button("Mean Sales", on_click=set_query, args=("mean sales",))
st.sidebar.button("Max Sales", on_click=set_query, args=("max sales",))
st.sidebar.button("Sum Sales", on_click=set_query, args=("sum sales",))

# 📦 Quantity
st.sidebar.markdown("### 📦 Quantity")
st.sidebar.button("Mean Quantity", on_click=set_query, args=("mean quantityordered",))
st.sidebar.button("Max Quantity", on_click=set_query, args=("max quantityordered",))

# 📈 Graphs
st.sidebar.markdown("### 📈 Graphs")
st.sidebar.button("Plot Sales", on_click=set_query, args=("plot sales",))
st.sidebar.button("Plot Country", on_click=set_query, args=("plot country",))

# ⭐ Smart
st.sidebar.markdown("### ⭐ Smart")
st.sidebar.button("Average Sales", on_click=set_query, args=("average sales",))
st.sidebar.button("Total Sales", on_click=set_query, args=("total sales",))

# ================== FILE UPLOAD ==================
st.markdown("### 📁 Upload Dataset")
uploaded_file = st.file_uploader("", type=["csv"])

if uploaded_file is None:
    st.info("⬆️ Upload a CSV file to start")

# ================== INSIGHTS FUNCTION ==================
def generate_insights(df):
    insights = []
    try:
        numeric_cols = df.select_dtypes(include='number').columns
        for col in numeric_cols[:3]:
            insights.append(f"📊 Avg {col}: {round(df[col].mean(), 2)}")
            insights.append(f"🔺 Max {col}: {df[col].max()}")
            insights.append(f"🔻 Min {col}: {df[col].min()}")
    except:
        insights.append("No insights available")
    return insights

# ================== MAIN ==================
if uploaded_file is not None:
    try:
        df = pd.read_csv(uploaded_file, encoding='latin1', on_bad_lines='skip')

        # 🔥 CLEAN DATA
        for col in df.columns:
            if df[col].dtype == 'object':
                try:
                    df[col] = df[col].astype(str)
                    df[col] = df[col].str.replace("₹", "")
                    df[col] = df[col].str.replace(",", "")
                    df[col] = pd.to_numeric(df[col], errors='ignore')
                except:
                    pass

        st.success("✅ Dataset Loaded")

        # 📊 METRICS
        col1, col2, col3 = st.columns(3)
        col1.metric("Rows", df.shape[0])
        col2.metric("Columns", df.shape[1])
        col3.metric("Features", len(df.columns))

        # 🧠 INSIGHTS
        st.markdown("### 🧠 Key Insights")
        insights = generate_insights(df)

        for ins in insights:
            st.info(ins)

        # 📥 DOWNLOAD REPORT
        st.markdown("### 📥 Download Report")

        report_text = "StatBot Pro Report\n\n"
        for ins in insights:
            report_text += ins + "\n"

        report_text += f"\nRows: {df.shape[0]}"
        report_text += f"\nColumns: {df.shape[1]}"

        st.download_button(
            label="📄 Download Insights Report",
            data=report_text,
            file_name="statbot_report.txt",
            mime="text/plain"
        )

        # 📄 Preview
        with st.expander("📊 Preview Data"):
            st.dataframe(df.head(), use_container_width=True)

        st.divider()

        # ================== QUERY ==================
        st.markdown("### 💬 Ask Question")

        query = st.chat_input("Type your query...")

        # 🔥 AUTO RUN (sidebar click)
        if st.session_state.selected_query:
            query = st.session_state.selected_query
            st.session_state.selected_query = ""

        if query:
            st.session_state.history.append(("user", query))

            with st.spinner("🤖 Thinking..."):
                result = analyze_data(df, query)

            st.session_state.history.append(("bot", result))

        # ================== CHAT ==================
        for role, message in st.session_state.history:

            if role == "user":
                st.chat_message("user").write(message)

            else:
                with st.chat_message("assistant"):
                    if isinstance(message, dict) and message.get("type") == "graph":
                        st.image(message["path"], caption="📊 Generated Graph")
                    else:
                        st.write(str(message))

    except Exception as e:
        st.error(f"❌ Error: {e}")