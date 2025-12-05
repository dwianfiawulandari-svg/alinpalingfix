import streamlit as st

def language_selector():
    st.sidebar.title("🌐 Language / Bahasa")

    if "lang" not in st.session_state:
        st.session_state["lang"] = "ID"

    selected_lang = st.sidebar.radio(
        "Choose Language / Pilih Bahasa:",
        ("ID", "EN"),
        index=0 if st.session_state["lang"] == "ID" else 1
    )

    st.session_state["lang"] = selected_lang
