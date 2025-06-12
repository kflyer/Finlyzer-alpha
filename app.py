
import streamlit as st
import pdfplumber
import pandas as pd

st.set_page_config(page_title="Finlyzer Alpha", layout="wide")
st.title("📊 Finlyzer Alpha - Financial Report Summarizer")

uploaded_file = st.file_uploader("Upload a financial report (PDF only)", type=["pdf"])

if uploaded_file:
    with pdfplumber.open(uploaded_file) as pdf:
        text = ""
        for page in pdf.pages:
            text += page.extract_text() or ""

    st.subheader("Extracted Text")
    st.write(text[:2000] + "...")  # Show first part only

    # Dummy example extraction
    revenue = "Not found"
    if "Revenue" in text:
        revenue = "$4.1B (example)"

    st.subheader("📈 Financial Summary")
    st.markdown(f"""
    - **Revenue**: {revenue}  
    - **Net Income**: Placeholder  
    - **EBITDA**: Placeholder  
    - **Debt to Equity Ratio**: Placeholder  
    """)

    st.download_button("Download Summary as CSV", data="Revenue,Net Income\n4.1B,1.2B", file_name="summary.csv")
