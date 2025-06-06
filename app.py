import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL", "http://localhost:8000")

st.set_page_config(page_title="AI Product Manager Assistant", layout="wide")
st.title("🤖 AI Product Manager Assistant")

st.write("Enter your product features or backlog items, each on a new line:")

features = st.text_area("Product Features / Backlog Items", height=200)

if st.button("Get AI Insights"):
    if not features.strip():
        st.warning("Please enter some product features or backlog items.")
    else:
        with st.spinner("Analyzing features..."):
            try:
                response = requests.post(f"{API_URL}/analyze-features", json={"features": features})
                response.raise_for_status()
                insights = response.json()["insights"]
                st.markdown("### 💡 AI Insights")
                st.write(insights)
            except Exception as e:
                st.error(f"Error calling API: {e}")

