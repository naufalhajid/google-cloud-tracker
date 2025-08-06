import streamlit as st

# Baca konten HTML dari file
with open('google-cloud-spreadsheet.html', 'r', encoding='utf-8') as f:
    html_content = f.read()

# Tampilkan konten HTML di Streamlit
st.components.v1.html(html_content, height=800, scrolling=True)

# Tambahkan elemen Streamlit lain jika diperlukan,
# misalnya:
st.write("Aplikasi pelacak progres belajar Anda!")
