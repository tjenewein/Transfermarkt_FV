import streamlit as st
from datetime import date

def spieler_inserat_volleyball():
    st.title("Spieler Inserat")
    st.write("Hier kannst du dein Volleyball-Inserat erstellen und verwalten.")
    
    vornname = st.text_input("Vorname des Spielers")
    nachname = st.text_input("Nachname des Spielers")
    
    sportart = "Volleyball"

    position = st.selectbox("Position", ["Außenangreifer","Diagonalangreifer", "Mittelblocker", "Zuspieler", "Libero"])

    geburtsdatum = st.date_input("Geburtsdatum", min_value=date(1900, 1, 1), max_value=date.today())
    
    # heutiges Datum
    today = date.today()

    # Alter berechnen
    alter = today.year - geburtsdatum.year - ((today.month, today.day) < (geburtsdatum.month, geburtsdatum.day))

    st.write(f"Alter: {alter} Jahre")

    größe = st.number_input("Größe in cm", min_value=100, max_value=250)

    sprungkraft = st.number_input("Sprungkraft in cm", min_value=0, max_value=200)

    schlagkraft = st.number_input("Schlagkraft in km/h", min_value=0, max_value=200)

    hand=st.selectbox("Hand", ["Rechts", "Links"])

    spiel_status = st.selectbox("Spielstatus", ["Aktiv", "Inaktiv", "Verletzt"])

    if spiel_status == "Aktiv":
        liga = st.selectbox("Aktuelle Liga", ["1. Bundesliga", "2. Bundesliga", "A-Landesliga", "B-Landesliga", "C-Landesliga", "D-Landesliga","Mixed-Landesliga",])
        verein = st.text_input("Verein")
    else:
        liga = st.selectbox("Letzte Liga", ["1. Bundesliga", "2. Bundesliga", "A-Landesliga", "B-Landesliga", "C-Landesliga", "D-Landesliga", "Mixed-Landesliga",])
        verein = st.text_input("Letzter Verein")


    if st.button("Inserat erstellen"):
        if vornname and nachname and verein:
            st.success(f"Das Inserat für {vornname} {nachname} wurde erfolgreich erstellt!")
        else:
            st.warning("Bitte füllen Sie alle Felder aus.")

spieler_inserat_volleyball()