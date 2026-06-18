from datetime import datetime


class FussballLeistung:
    def __init__(self, spieler_id, heatmap_pfad=None, spielertyp=None, leistungswert=None, datum=None, datei_pfad=None):
        self.spieler_id = spieler_id
        self.datum = datum if datum else datetime.now().strftime("%Y-%m-%d")
        self.sportart = "Fußball"
        self.heatmap_pfad = heatmap_pfad    # Pfad zum Heatmap-Bild
        self.spielertyp = spielertyp        # "Stürmer", "Achter", "Verteidiger"
        self.leistungswert = leistungswert  # Wert von 0 bis 10
        self.datei_pfad = datei_pfad        # Pfad zu einer zusätzlichen Datei

    def validiere(self):
        if not self.spieler_id or not self.datum:
            return False
        if self.leistungswert is not None:
            if not isinstance(self.leistungswert, (int, float)) or not (0 <= self.leistungswert <= 10):
                return False
        return True

    def __repr__(self):
        typ = self.spielertyp if self.spielertyp else "unbekannt"
        return f"FussballLeistung(spieler_id={self.spieler_id}, typ={typ}, datum={self.datum})"


class VolleyballLeistung:
    def __init__(self, spieler_id, schlagkraft=None, sprungkraft=None, belastung=None, leistungspunkte=None, datum=None, datei_pfad=None):
        self.spieler_id = spieler_id
        self.datum = datum if datum else datetime.now().strftime("%Y-%m-%d")
        self.sportart = "Volleyball"
        self.schlagkraft = schlagkraft          # in km/h
        self.sprungkraft = sprungkraft          # in cm
        self.belastung = belastung              # in Minuten
        self.leistungspunkte = leistungspunkte  # allgemeiner Leistungswert
        self.datei_pfad = datei_pfad            # Pfad zur hochgeladenen CSV/EKG Datei

    def validiere(self):
        if not self.spieler_id or not self.datum:
            return False
        if self.schlagkraft is not None and self.schlagkraft < 0:
            return False
        if self.sprungkraft is not None and self.sprungkraft < 0:
            return False
        if self.belastung is not None and self.belastung < 0:
            return False
        return True

    def __repr__(self):
        return (f"VolleyballLeistung(spieler_id={self.spieler_id}, "
                f"schlagkraft={self.schlagkraft}km/h, "
                f"sprungkraft={self.sprungkraft}cm, "
                f"datum={self.datum})")