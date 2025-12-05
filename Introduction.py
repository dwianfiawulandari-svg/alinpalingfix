import streamlit as st
from sidebar import language_selector
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Transform Matrix App", layout="wide")

# Sidebar bahasa
language_selector()
lang = st.session_state["lang"]

# ========== THEME PIXEL ==========
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

</style>
"""
st.markdown(pixel_theme, unsafe_allow_html=True)

# TITLE
st.title("📘 Aplikasi Transformasi Matriks" if lang == "ID" else "📘 Matrix Transformation App")

# ============================================================
#   INTRODUCTION (WITH FULL EXPLANATION)
# ============================================================

st.markdown('<div class="pixel-card">', unsafe_allow_html=True)

if lang == "ID":
    st.header("Apa itu Transformasi Matriks?")
    st.write("""
Transformasi matriks adalah operasi matematika yang digunakan untuk **mengubah posisi, orientasi, atau ukuran objek 2D**.

Transformasi yang umum meliputi:
- **Translasi** → memindahkan posisi
- **Rotasi** → memutar objek
- **Scaling** → memperbesar / memperkecil
- **Shearing** → menggeser bentuk
- **Reflection** → membalik objek terhadap sumbu tertentu

Semua ini dilakukan menggunakan **matriks 2×2 atau 3×3**.
    """)
else:
    st.header("What is Matrix Transformation?")
    st.write("""
Matrix transformation is a mathematical operation used to **modify the position, orientation, or size of a 2D object**.

Common transformations include:
- **Translation**
- **Rotation**
- **Scaling**
- **Shearing**
- **Reflection**

All of these are performed using **2×2 or 3×3 matrices**.
    """)

st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
#   VISUAL EXAMPLE – ROTATION
# ============================================================

st.markdown('<div class="pixel-card">', unsafe_allow_html=True)

st.subheader("🟩 Visual Example: Rotasi Matriks")

points = np.array([[0,0], [1,0], [0.5,1], [0,0]])
theta = np.radians(45)
rotation_matrix = np.array([[np.cos(theta), -np.sin(theta)],
                            [np.sin(theta), np.cos(theta)]])
rotated = points @ rotation_matrix.T

fig, ax = plt.subplots()
ax.plot(points[:,0], points[:,1], label="Original", linewidth=3)
ax.plot(rotated[:,0], rotated[:,1], label="Rotated 45°", linewidth=3)
ax.legend()
ax.set_aspect('equal')
ax.grid(True)
st.pyplot(fig)

st.markdown('</div>', unsafe_allow_html=True)


# ============================================================
#   CONVOLUTION + VISUAL EXAMPLE
# ============================================================

st.markdown('<div class="pixel-card">', unsafe_allow_html=True)

if lang == "ID":
    st.subheader("🔶 Apa itu Convolution?")
    st.write("""
Convolution adalah proses menggeser **kernel (matriks kecil)** di atas gambar 
untuk menghasilkan gambar baru.

Digunakan untuk:
- Deteksi tepi
- Blur
- Sharpen
- Ekstraksi fitur CNN
    """)
else:
    st.subheader("🔶 What is Convolution?")
    st.write("""
Convolution is the process of sliding a **kernel (small matrix)** across an image 
to generate a transformed image.

Used for:
- Edge detection  
- Blur  
- Sharpen  
- CNN feature extraction  
    """)

# VISUAL EXAMPLE
image = np.array([
    [10,10,10,10,10],
    [10,50,50,50,10],
    [10,50,100,50,10],
    [10,50,50,50,10],
    [10,10,10,10,10],
])

kernel = np.array([
    [-1,-1,-1],
    [-1, 8,-1],
    [-1,-1,-1]
])

output = np.zeros((3,3))
for i in range(3):
    for j in range(3):
        output[i,j] = np.sum(image[i:i+3, j:j+3] * kernel)

fig2, ax2 = plt.subplots(1,3, figsize=(10,3))
ax2[0].imshow(image, cmap="gray"); ax2[0].set_title("Original")
ax2[1].imshow(kernel, cmap="gray"); ax2[1].set_title("Kernel")
ax2[2].imshow(output, cmap="gray"); ax2[2].set_title("Output")

for a in ax2: a.axis("off")

st.pyplot(fig2)

st.markdown('</div>', unsafe_allow_html=True)
