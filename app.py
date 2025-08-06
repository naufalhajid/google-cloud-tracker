import streamlit as st

# WAJIB: Set di paling atas
st.set_page_config(layout="wide")

with open('google-cloud-spreadsheet.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Tampilkan dengan ukuran yang benar
st.components.v1.html(html_content, width=1400, height=1000, scrolling=True)
