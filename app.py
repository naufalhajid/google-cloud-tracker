import streamlit as st

st.set_page_config(layout="wide")

with open('google-cloud-spreadsheet.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

iframe_html = f"""
<iframe 
    srcdoc='{html_content.replace("'", "&apos;")}' 
    width="100%" 
    height="800px" 
    style="border:none; transform: scale(1.8); transform-origin: top left; width: 56%; height: 56%;"
    scrolling="yes">
</iframe>
"""

st.components.v1.html(iframe_html, height=1200)
