import streamlit as st
from datetime import date

def spieler_inserat_fußball():
    st.title("Spieler Inserat für Fußball")
    st.write("Hier kannst du dein Inserat erstellen und verwalten.")
    
    vornname = st.text_input("Vorname des Spielers")
    nachname = st.text_input("Nachname des Spielers")
    
    sportart = "Fußball"

    position = st.selectbox("Position", 
                            ["Torwart", 
                             
                             "Innenverteidiger", 
                             "Rechtsverteidiger",
                             "Linksverteidiger",

                             "Defensives Mittelfeld",
                             "Zentrales Mittelfeld",
                             "Offensives Mittelfeld",
                             "Rechtes Mittelfeld",
                             "Linkes Mittelfeld",
                             
                             "Mittelstürmer",
                             "Linksaußen",
                             "Rechtsaußen"])

    geburtsdatum = st.date_input("Geburtsdatum",value=None,min_value=date(1900, 1, 1),max_value=date.today())
    today = date.today()
    
    if geburtsdatum is not None:
        alter = today.year - geburtsdatum.year - (
            (today.month, today.day) < (geburtsdatum.month, geburtsdatum.day)
        )
        st.success(f"Alter: {alter} Jahre")
    else:
        st.info("Bitte Geburtsdatum auswählen")

    größe = st.number_input("Größe in cm", min_value=100, max_value=250)

    sprintgeschwindigkeit = st.number_input("Sprintgeschwindigkeit in km/h", min_value=0, max_value=50)

    schusskraft = st.number_input("Schusskraft in km/h", min_value=0, max_value=200)

    fuß=st.selectbox("Fuß", ["Rechts", "Links"])

    spiel_status = st.selectbox("Spielstatus", ["Aktiv", "Inaktiv", "Verletzt"])

    if spiel_status == "Aktiv":
        liga = st.selectbox("Aktuelle Liga", 
                            ["1. Bundesliga", 
                             "2. Bundesliga", 
                             "Regionalliga", 
                             "HYPO Tirol Liga", 
                             "Landesliga", 
                             "Gebietsliga",
                             "Bezirksliga",
                             "1. Klasse",
                             "2. Klasse",
                             "Reserve"])
        verein = st.text_input("Verein")
    else:
        liga = st.selectbox("Letzte Liga", 
                            ["1. Bundesliga", 
                             "2. Bundesliga", 
                             "Regionalliga", 
                             "HYPO Tirol Liga", 
                             "Landesliga", 
                             "Gebietsliga",
                             "Bezirksliga",
                             "1. Klasse",
                             "2. Klasse",
                             "Reserve"])
        verein = st.text_input("Letzter Verein")


    if st.button("Inserat erstellen"):
        if vornname and nachname and verein:
            st.success(f"Das Inserat für {vornname} {nachname} wurde erfolgreich erstellt!")
        else:
            st.warning("Bitte füllen Sie alle Felder aus.")

spieler_inserat_fußball()