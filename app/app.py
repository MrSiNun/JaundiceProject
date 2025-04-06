
import streamlit as st
import json

st.set_page_config(page_title="🔐 GCP Key Analyzer")
st.title("🔐 GCP Service Account Key Analyzer")

uploaded_file = st.file_uploader("📁 Upload your GCP JSON key file", type="json")

if uploaded_file:
    try:
        key_data = json.load(uploaded_file)
        st.success("✅ File loaded!")

        st.subheader("📄 Key Info")
        for k, v in key_data.items():
            if "private_key" in k:
                st.write(f"🔒 **{k}**: *(hidden)*")
            else:
                st.write(f"**{k}**: {v}")

        if "client_email" in key_data:
            st.info(f"🔎 Service Account Email: `{key_data['client_email']}`")
        if "project_id" in key_data:
            st.info(f"🗂️ Project ID: `{key_data['project_id']}`")
    except:
        st.error("❌ Not a valid JSON file.")
