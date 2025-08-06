import streamlit as st

# Set layout wide (letakkan di bagian atas)
st.set_page_config(layout="wide")

# Baca file HTML
with open('google-cloud-spreadsheet.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Tambahkan CSS untuk styling yang lebih baik
css_style = """
<style>
img {
    max-width: 100% !important;
    height: auto !important;
    min-width: 800px !important;
}
body {
    zoom: 1.1;
    margin: 0;
    padding: 20px;
}
</style>
"""

# Gabungkan dan tampilkan
html_with_css = css_style + html_content
st.components.v1.html(html_with_css, height=900, scrolling=True)
