from datetime import datetime


class FussballSpieler:
    def __init__(self, name, geburtsjahr, liga, team, groesse, linksfuss=False, spielertyp=None, foto_pfad=None, heatmap_pfad=None):
        self.name = name
        self.geburtsjahr = geburtsjahr
        self.liga = liga
        self.team = team
        self.groesse = groesse          # in cm
        self.linksfuss = linksfuss      # True = Linksfuß, False = Rechtsfuß
        self.spielertyp = spielertyp    # "Stürmer", "Achter", "Verteidiger" — von heatmap.py gesetzt
        self.foto_pfad = foto_pfad
        self.heatmap_pfad = heatmap_pfad
        self.sportart = "Fußball"
        self.erstellt_am = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def berechne_alter(self):
        return datetime.now().year - self.geburtsjahr

    def validiere(self):
        if not self.name or not self.geburtsjahr or not self.liga or not self.team or not self.groesse:
            return False
        if not isinstance(self.geburtsjahr, int) or self.geburtsjahr < 1950 or self.geburtsjahr > datetime.now().year:
            return False
        if not isinstance(self.groesse, (int, float)) or self.groesse < 100 or self.groesse > 250:
            return False
        if not isinstance(self.linksfuss, bool):
            return False
        return True

    def __repr__(self):
        seite = "Linksfuß" if self.linksfuss else "Rechtsfuß"
        typ = self.spielertyp if self.spielertyp else "unbekannt"
        return f"FussballSpieler({self.name}, {self.liga}, {self.team}, {typ}, {seite})"


class VolleyballSpieler:
    def __init__(self, name, geburtsjahr, liga, team, groesse, foto_pfad=None, leistung_pfad=None):
        self.name = name
        self.geburtsjahr = geburtsjahr
        self.liga = liga
        self.team = team
        self.groesse = groesse          # in cm
        self.foto_pfad = foto_pfad
        self.leistung_pfad = leistung_pfad  # Pfad zur hochgeladenen Leistungsdatei
        self.sportart = "Volleyball"
        self.erstellt_am = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def berechne_alter(self):
        return datetime.now().year - self.geburtsjahr

    def validiere(self):
        if not self.name or not self.geburtsjahr or not self.liga or not self.team or not self.groesse:
            return False
        if not isinstance(self.geburtsjahr, int) or self.geburtsjahr < 1950 or self.geburtsjahr > datetime.now().year:
            return False
        if not isinstance(self.groesse, (int, float)) or self.groesse < 100 or self.groesse > 250:
            return False
        return True

    def __repr__(self):
        return f"VolleyballSpieler({self.name}, {self.liga}, {self.team})"