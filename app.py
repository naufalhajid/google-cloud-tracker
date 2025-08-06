import streamlit as st

# Baca konten HTML dari file
with open('google-cloud-spreadsheet.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Tampilkan konten HTML di Streamlit tanpa tinggi tetap
st.components.v1.html(html_content, scrolling=True)
