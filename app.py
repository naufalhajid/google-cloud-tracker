import streamlit as st

# WAJIB: Set layout wide di bagian paling atas
st.set_page_config(
    page_title="Google Cloud Learning Tracker",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Baca konten HTML
with open('google-cloud-spreadsheet.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# CSS untuk memperbaiki tampilan
css_fixes = """
<style>
    /* Reset dan base styling */
    * {
        box-sizing: border-box;
    }
    
    body {
        margin: 0 !important;
        padding: 20px !important;
        background-color: #0e1117 !important;
        font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Roboto', sans-serif !important;
        zoom: 1.3 !important;
        min-height: 100vh !important;
    }
    
    /* Container utama */
    .main-container, .container, .wrapper {
        width: 100% !important;
        max-width: none !important;
        min-width: 800px !important;
        margin: 0 auto !important;
        padding: 20px !important;
    }
    
    /* Card/Panel styling */
    .card, .panel, .dashboard-card {
        width: 100% !important;
        max-width: 600px !important;
        min-width: 400px !important;
        margin: 0 auto !important;
        padding: 30px !important;
        border-radius: 12px !important;
        box-shadow: 0 4px 20px rgba(0,0,0,0.3) !important;
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%) !important;
    }
    
    /* Text dan heading */
    h1, h2, h3, h4, h5, h6 {
        color: white !important;
        margin-bottom: 15px !important;
        font-weight: 600 !important;
    }
    
    p, span, div {
        color: white !important;
        font-size: 16px !important;
        line-height: 1.5 !important;
    }
    
    /* Stats/Numbers styling */
    .stat-number, .number, .count {
        font-size: 48px !important;
        font-weight: bold !important;
        color: white !important;
        text-align: center !important;
        margin: 10px 0 !important;
    }
    
    .stat-label, .label {
        font-size: 14px !important;
        opacity: 0.9 !important;
        text-transform: uppercase !important;
        letter-spacing: 1px !important;
    }
    
    /* Progress bars */
    .progress-bar, .progress {
        width: 100% !important;
        height: 8px !important;
        border-radius: 4px !important;
        background-color: rgba(255,255,255,0.2) !important;
        margin: 15px 0 !important;
    }
    
    .progress-fill {
        height: 100% !important;
        border-radius: 4px !important;
        background-color: #4CAF50 !important;
    }
    
    /* Responsive adjustments */
    @media (max-width: 768px) {
        body {
            zoom: 1.1 !important;
            padding: 10px !important;
        }
        
        .card, .panel, .dashboard-card {
            min-width: 300px !important;
            padding: 20px !important;
        }
    }
    
    /* Pastikan semua elemen visible */
    * {
        visibility: visible !important;
        opacity: 1 !important;
    }
</style>
"""

# Gabungkan CSS dengan HTML
enhanced_html = css_fixes + html_content

# Tampilkan dengan pengaturan optimal
st.components.v1.html(
    enhanced_html, 
    width=None,  # Gunakan full width
    height=1000,  # Tinggi yang cukup
    scrolling=True
)

# Alternative: Jika masih terlalu kecil, gunakan ini
st.markdown("---")
st.subheader("Alternative Display (Jika tampilan di atas masih bermasalah)")

# Buat wrapper dengan iframe yang lebih besar
iframe_wrapper = f"""
<div style="width: 100%; height: 1000px; overflow: auto; border: 1px solid #ddd; border-radius: 8px;">
    <iframe 
        srcdoc='{enhanced_html.replace("'", "&apos;").replace('"', "&quot;")}' 
        width="100%" 
        height="1000px" 
        style="border: none; transform: scale(1.5); transform-origin: top left; width: 67%; height: 67%;"
        scrolling="yes">
    </iframe>
</div>
"""

st.components.v1.html(iframe_wrapper, height=1000)

# Tambahan: Custom CSS untuk Streamlit app
st.markdown("""
<style>
    /* Hide Streamlit footer */
    footer {visibility: hidden;}
    
    /* Hide hamburger menu */
    #MainMenu {visibility: hidden;}
    
    /* Reduce top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 2rem;
        max-width: none;
    }
    
    /* Make sure iframe uses full width */
    iframe {
        width: 100% !important;
    }
</style>
""", unsafe_allow_html=True)
