import streamlit as st
from PIL import Image
import os
from sidebar import language_selector

language_selector()
# Title for Group Members Page
st.markdown("""
<h1 style="
    font-family: 'Press Start 2P', cursive;
    color: #00ff9c;
    text-shadow: 3px 3px #003f2b;
    margin-bottom: 20px;
">
👥 Group Members
</h1>
""", unsafe_allow_html=True)

pixel_sidebar = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

/* === SIDEBAR FULL RETRO PIXEL === */
section[data-testid="stSidebar"] {
    background-color: #000000 !important;
    border-right: 4px solid #00ff9c !important;
    padding: 20px;
}

/* TEXT STYLE */
section[data-testid="stSidebar"] * {
    font-family: 'Press Start 2P', cursive !important;
    color: #00ffcc !important;
    text-shadow: 2px 2px #003f2b;
}

/* MENU ITEM STYLE */
section[data-testid="stSidebar"] .css-1siy2j7,      /* Streamlit menu item wrapper */
section[data-testid="stSidebar"] .css-1my2v7x,
section[data-testid="stSidebar"] ul li {
    font-size: 13px !important;
    padding: 10px !important;
    margin-bottom: 8px;
    border-radius: 6px;
}

/* ACTIVE ITEM (yang lagi dipilih) */
section[data-testid="stSidebar"] .css-1siy2j7:hover,
section[data-testid="stSidebar"] .css-1my2v7x:hover,
section[data-testid="stSidebar"] ul li:hover {
    background-color: #1f1f1f !important;
    border: 2px solid #00ff9c !important;
    color: #00ffaa !important;
    transform: scale(1.05);
}

/* RADIO BUTTON RETRO */
div[data-baseweb="radio"] > div {
    margin-bottom: 15px !important;
}

input[type="radio"] {
    accent-color: #ff4d4d !important;
}

/* Radio label */
label {
    font-size: 12px !important;
}

/* GLOBE ICON & LANGUAGE TITLE */
.sidebar-title {
    font-size: 20px !important;
    color: #00ffcc !important;
    text-shadow: 3px 3px #004430;
    margin-top: 20px;
    margin-bottom: 10px;
}

</style>
"""
st.markdown(pixel_sidebar, unsafe_allow_html=True)


lang = st.session_state["lang"]
pixel_theme = """
<style>

@import url('https://fonts.googleapis.com/css2?family=Press+Start+2P&display=swap');

/* FONT RETRO PIXEL */
html, body, [class*="css"]  {
    font-family: 'Press Start 2P', cursive !important;
    background: #1a1a1a !important;
    color: #e0e0e0 !important;
}

/* TITLES */
h1, h2, h3, h4 {
    font-family: 'Press Start 2P', cursive !important;
    color: #00ff9c !important;
    text-shadow: 3px 3px #003f2b;
}

/* CARD UI */
.pixel-card {
    background: #262626;
    padding: 25px;
    border-radius: 0px;
    border: 4px solid #00ff9c;
    box-shadow: 8px 8px 0px #003f2b;
    margin-bottom: 20px;
}

/* BUTTONS */
.stButton > button {
    background-color: #00ff9c !important;
    color: #000 !important;
    border-radius: 0px !important;
    border: 4px solid #003f2b !important;
    padding: 10px 20px;
    font-size: 12px;
    font-weight: bold;
    box-shadow: 4px 4px 0px #003f2b;
    transition: 0.1s;
}

.stButton > button:hover {
    background-color: #00ffaa !important;
    transform: translate(-3px, -3px);
    box-shadow: 7px 7px 0px #003f2b;
}

/* SIDEBAR */
section[data-testid="stSidebar"] {
    background-color: #111 !important;
    border-right: 4px solid #00ff9c;
}

section[data-testid="stSidebar"] * {
    color: #00ffcc !important;
}

/* INPUTS */
.stTextInput input,
.stNumberInput input,
.stSelectbox select {
    background-color: #000 !important;
    border: 4px solid #00ff9c !important;
    border-radius: 0px !important;
    color: #00ffaa !important;
}

/* FILE UPLOADER */
.stFileUploader {
    border: 4px dashed #00ff9c !important;
    padding: 12px;
    background: #111;
}

</style>
"""

st.markdown("""
<style>
.pixel-card {
    background-color: #000000;              /* kotak hitam */
    border: 4px solid #00ff9c;              /* border hijau neon */
    padding: 20px;
    border-radius: 0px;                     /* supaya pixel-style */
    box-shadow: 0 0 15px #00ff9c;           /* glow hijau seperti contoh */
    font-family: 'Courier New', monospace;  /* font retro */
}
</style>
""", unsafe_allow_html=True)
if lang == "ID":
    st.markdown("""
    <div class="pixel-card" style="color: #00ff9c; font-size: 16px; line-height: 1.6;">
        <h3 style="color: #00ff9c;">🔍 Penjelasan Singkat Aplikasi</h3>
        Aplikasi ini dibuat untuk membantu pengguna memahami bagaimana 
        <b>transformasi matriks 2D</b> bekerja. <br><br>

        Pengguna dapat mencoba berbagai jenis transformasi seperti:<br>
        • Translasi <br>
        • Rotasi <br>
        • Skala <br>
        • Shearing <br>
        • Refleksi <br><br>

        Setiap transformasi akan langsung divisualisasikan sehingga 
        memudahkan proses pembelajaran.
    </div>
    """, unsafe_allow_html=True)

else:
    st.markdown("""
    <div class="pixel-card" style="color: #00ff9c; font-size: 16px; line-height: 1.6;">
        <h3 style="color: #00ff9c;">🔍 Short Explanation of the App</h3>
        This application is designed to help users understand how 
        <b>2D matrix transformations</b> work. <br><br>

        Users can try several transformation types such as:<br>
        • Translation <br>
        • Rotation <br>
        • Scaling <br>
        • Shearing <br>
        • Reflection <br><br>

        Each transformation is visualized instantly, making the 
        learning process easier and more interactive.
    </div>
    """, unsafe_allow_html=True)


st.markdown("""
<div style="
    font-family: 'Press Start 2P', cursive;
    color: #00ff9c;
    text-shadow: 3px 3px #003f2b;
    font-size: 32px;
    margin-top: 20px;
    margin-bottom: 25px;
">
👥 Group Members
</div>
""", unsafe_allow_html=True)

# Daftar anggota (lengkapi path foto sesuai folder 'members/')
members = [
    {
        "name": "Ananda Fasya Wiratama Putri",
        "photo": "members/fasya.jpg",
        "role_id": "Pengembang fitur shearing & refleksi; dokumentasi",
        "role_en": "Developed shearing & reflection features; documentation"
    },
    {
        "name": "Dwi Anfia Putri Wulandari",
        "photo": "members/anfia.jpeg",
        "role_id": "Pengembang antarmuka & integrasi bahasa",
        "role_en": "UI developer & language integration"
    },
    {
        "name": "Gina Sonia",
        "photo": "members/gina.jpg",
        "role_id": "Mengimplementasikan scaling & optimisasi gambar",
        "role_en": "Implemented scaling & image optimizations"
    },
    {
        "name": "Moh. Trisbintang A. Menu",
        "photo": "members/tris.jpg",
        "role_id": "Analisis transformasi matriks; rotasi & translasi",
        "role_en": "Matrix transformation analysis; rotation & translation"
    },
]

# Tampilkan anggota dalam grid 2 kolom
cols = st.columns(2)
for i, m in enumerate(members):
    col = cols[i % 2]
    with col:
        st.subheader(m["name"])
        # Cek apakah file foto ada, jika tidak tampilkan placeholder
        if os.path.exists(m["photo"]):
            try:
                img = Image.open(m["photo"])
                st.image(img, width=220)
            except Exception as e:
                st.warning("Gagal membuka gambar: " + str(e))
        else:
            st.warning("Foto tidak ditemukan: " + m["photo"])

        # Tampilkan peran sesuai bahasa
        role_text = m["role_en"] if lang == "EN" else m["role_id"]
        st.write("**Role:** " + role_text)
        st.write("---")