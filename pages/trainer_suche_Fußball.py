import streamlit as st
from datetime import date

st.header("Trainer Suche")
def spieler_inserat_fußball():
    st.title("Hier kannst du nach deinem Wunschspieler suchen.")
    
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

    #Spieler Alter auswählen
    min_val, max_val = st.slider(
    "Alter in Jahren auswählen",
    min_value=0,
    max_value=100,
    value=(0, 100)   #Startpunkte
    )
    

    #Spieler Größe auswählen
    min_val, max_val = st.slider(
    "Größe in cm auswählen",
    min_value=100,
    max_value=250,
    value=(100, 250)   #Startpunkte
    )
    

    #Sprintgeschwindigkeit auswählen
    min_val, max_val = st.slider(
    "Sprintgeschwindigkeit in km/h auswählen",
    min_value=0,
    max_value=50,
    value=(0, 50)   #Startpunkte
    )

    #Schusskraft auswählen
    min_val, max_val = st.slider(
    "Schusskraft in km/h auswählen",
    min_value=0,
    max_value=200,
    value=(0, 200)   #Startpunkte
    )

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