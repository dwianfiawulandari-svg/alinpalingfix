import streamlit as st
import numpy as np
import cv2
from PIL import Image
from sidebar import language_selector

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(__file__)))


language_selector()

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

st.markdown(pixel_theme, unsafe_allow_html=True)
# ==========================



st.title("🖼️ Image Processing" if lang == "EN" else "🖼️ Pemprosesan Gambar")


uploaded_img = st.file_uploader(
    "Upload image" if lang == "EN" else "Upload gambar",
    type=["jpg", "png", "jpeg"]
)

if uploaded_img:
    img = Image.open(uploaded_img)
    img_np = np.array(img)

    st.subheader("Original Image" if lang == "EN" else "Gambar Asli")
    st.image(img_np, width=300)

    col1, col2 = st.columns(2)

    with col1:
        st.header("Transformations" if lang == "EN" else "Transformasi")

        angle = st.slider("Rotation (°)" if lang == "EN" else "Rotasi (°)", -180, 180, 0)
        dx = st.slider("Translate X" if lang == "EN" else "Translasi X", -200, 200, 0)
        dy = st.slider("Translate Y" if lang == "EN" else "Translasi Y", -200, 200, 0)
        scale = st.slider("Scaling", 0.1, 3.0, 1.0)

        shear_x = st.slider("Shearing X", -1.0, 1.0, 0.0)
        shear_y = st.slider("Shearing Y", -1.0, 1.0, 0.0)

        reflection = st.selectbox(
            "Reflection" if lang == "EN" else "Refleksi",
            ["None", "Horizontal", "Vertical"]
        )

    # ================= APPLY TRANSFORMATIONS ===================
    rows, cols = img_np.shape[:2]

    # Translation
    M_translate = np.float32([[1, 0, dx], [0, 1, dy]])
    result = cv2.warpAffine(img_np, M_translate, (cols, rows))

    # Rotation
    M_rotate = cv2.getRotationMatrix2D((cols/2, rows/2), angle, 1)
    result = cv2.warpAffine(result, M_rotate, (cols, rows))

    # Scaling
    result = cv2.resize(result, None, fx=scale, fy=scale)

    # Shearing
    M_shear = np.float32([[1, shear_x, 0],
                          [shear_y, 1, 0]])
    result = cv2.warpAffine(result, M_shear, (cols * 2, rows * 2))

    # Reflection
    if reflection == "Horizontal":
        result = cv2.flip(result, 1)
    elif reflection == "Vertical":
        result = cv2.flip(result, 0)

    with col2:
        st.header("Edited Image" if lang == "EN" else "Gambar Hasil Edit")
        st.image(result, width=300)

    st.success("Transformation applied!" if lang == "EN" else "Transformasi berhasil diterapkan!")
