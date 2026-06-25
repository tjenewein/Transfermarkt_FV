import streamlit as st

st.title("Transfermarkt")
st.subheader("Finde den passenden Trainer oder Spieler für dein Team!")


st.markdown("""
    <style>
    div[role=radiogroup] label {
        margin-right: 50px;
    }
    </style>
""", unsafe_allow_html=True)

size = 200

option = st.radio("", ["Fußballspieler", "Fußballtrainer", "Volleyballspieler", "Volleyballtrainer"], horizontal=True)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.image("Bilder/Fußballspieler.jpg", width=size)
with col2:
    st.image("Bilder/Fußballtrainer.png", width=size)
with col3:
    st.image("Bilder/Volleyballspieler.jpeg", width=size)
with col4:
    st.image("Bilder/Volleyballtrainer.jpeg", width=size)

if st.button("Weiter"):
    if option == "Fußballspieler":
        st.switch_page("pages/spieler_inserat_fußball.py")
    elif option == "Fußballtrainer":
        st.switch_page("pages/fussballtrainer.py")
    elif option == "Volleyballspieler":
        st.switch_page("pages/spieler_inserat_volleyball.py")
    elif option == "Volleyballtrainer":
        st.switch_page("pages/volleyballtrainer.py")
