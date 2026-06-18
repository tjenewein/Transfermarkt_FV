import sqlite3
from datetime import datetime
import sys
import os

sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from spieler_daten.spieler import FussballSpieler, VolleyballSpieler
from spieler_daten.leistung import FussballLeistung, VolleyballLeistung


class DBManager:
    def __init__(self, db_pfad="datenbank.db"):
        self.db_pfad = db_pfad
        self.verbindung = sqlite3.connect(self.db_pfad)
        self.verbindung.row_factory = sqlite3.Row
        self.init_tables()

    # ------------------------------------------------------------------ #
    #  TABELLEN ERSTELLEN
    # ------------------------------------------------------------------ #

    def init_tables(self):
        cursor = self.verbindung.cursor()

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fussball_spieler (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                name            TEXT NOT NULL,
                geburtsjahr     INTEGER NOT NULL,
                liga            TEXT NOT NULL,
                team            TEXT NOT NULL,
                groesse         REAL NOT NULL,
                linksfuss       INTEGER NOT NULL DEFAULT 0,
                spielertyp      TEXT,
                foto_pfad       TEXT,
                heatmap_pfad    TEXT,
                erstellt_am     TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS volleyball_spieler (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                name            TEXT NOT NULL,
                geburtsjahr     INTEGER NOT NULL,
                liga            TEXT NOT NULL,
                team            TEXT NOT NULL,
                groesse         REAL NOT NULL,
                foto_pfad       TEXT,
                leistung_pfad   TEXT,
                erstellt_am     TEXT NOT NULL
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS fussball_leistung (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                spieler_id      INTEGER NOT NULL,
                datum           TEXT NOT NULL,
                heatmap_pfad    TEXT,
                spielertyp      TEXT,
                leistungswert   REAL,
                datei_pfad      TEXT,
                FOREIGN KEY (spieler_id) REFERENCES fussball_spieler(id)
            )
        """)

        cursor.execute("""
            CREATE TABLE IF NOT EXISTS volleyball_leistung (
                id              INTEGER PRIMARY KEY AUTOINCREMENT,
                spieler_id      INTEGER NOT NULL,
                datum           TEXT NOT NULL,
                schlagkraft     REAL,
                sprungkraft     REAL,
                belastung       REAL,
                leistungspunkte REAL,
                datei_pfad      TEXT,
                FOREIGN KEY (spieler_id) REFERENCES volleyball_spieler(id)
            )
        """)

        self.verbindung.commit()

    # ------------------------------------------------------------------ #
    #  SPIELER HINZUFÜGEN
    # ------------------------------------------------------------------ #

    def add_spieler(self, spieler):
        """Spieler speichern — erkennt automatisch ob Fußball oder Volleyball."""
        if not spieler.validiere():
            raise ValueError(f"Spieler ungültig: {spieler}")

        cursor = self.verbindung.cursor()

        if spieler.sportart == "Fußball":
            cursor.execute("""
                INSERT INTO fussball_spieler
                    (name, geburtsjahr, liga, team, groesse, linksfuss,
                     spielertyp, foto_pfad, heatmap_pfad, erstellt_am)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                spieler.name, spieler.geburtsjahr, spieler.liga, spieler.team,
                spieler.groesse, int(spieler.linksfuss), spieler.spielertyp,
                spieler.foto_pfad, spieler.heatmap_pfad, spieler.erstellt_am
            ))

        elif spieler.sportart == "Volleyball":
            cursor.execute("""
                INSERT INTO volleyball_spieler
                    (name, geburtsjahr, liga, team, groesse,
                     foto_pfad, leistung_pfad, erstellt_am)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                spieler.name, spieler.geburtsjahr, spieler.liga, spieler.team,
                spieler.groesse, spieler.foto_pfad, spieler.leistung_pfad,
                spieler.erstellt_am
            ))

        self.verbindung.commit()
        return cursor.lastrowid

    # ------------------------------------------------------------------ #
    #  SPIELER ABRUFEN
    # ------------------------------------------------------------------ #

    def get_alle_spieler(self, sportart):
        """Alle Spieler einer Sportart abrufen."""
        cursor = self.verbindung.cursor()

        if sportart == "Fußball":
            cursor.execute("SELECT * FROM fussball_spieler")
            return [self._zeile_zu_fussball_spieler(z) for z in cursor.fetchall()]

        elif sportart == "Volleyball":
            cursor.execute("SELECT * FROM volleyball_spieler")
            return [self._zeile_zu_volleyball_spieler(z) for z in cursor.fetchall()]

    def get_spieler(self, spieler_id, sportart):
        """Einen einzelnen Spieler anhand ID und Sportart abrufen."""
        cursor = self.verbindung.cursor()

        if sportart == "Fußball":
            cursor.execute("SELECT * FROM fussball_spieler WHERE id = ?", (spieler_id,))
            zeile = cursor.fetchone()
            return self._zeile_zu_fussball_spieler(zeile) if zeile else None

        elif sportart == "Volleyball":
            cursor.execute("SELECT * FROM volleyball_spieler WHERE id = ?", (spieler_id,))
            zeile = cursor.fetchone()
            return self._zeile_zu_volleyball_spieler(zeile) if zeile else None

    # ------------------------------------------------------------------ #
    #  SPIELER UPDATEN
    # ------------------------------------------------------------------ #

    def update_spieler(self, spieler_id, spieler):
        """Bestehenden Spieler aktualisieren."""
        if not spieler.validiere():
            raise ValueError(f"Spieler ungültig: {spieler}")

        cursor = self.verbindung.cursor()

        if spieler.sportart == "Fußball":
            cursor.execute("""
                UPDATE fussball_spieler SET
                    name = ?, geburtsjahr = ?, liga = ?, team = ?, groesse = ?,
                    linksfuss = ?, spielertyp = ?, foto_pfad = ?, heatmap_pfad = ?
                WHERE id = ?
            """, (
                spieler.name, spieler.geburtsjahr, spieler.liga, spieler.team,
                spieler.groesse, int(spieler.linksfuss), spieler.spielertyp,
                spieler.foto_pfad, spieler.heatmap_pfad, spieler_id
            ))

        elif spieler.sportart == "Volleyball":
            cursor.execute("""
                UPDATE volleyball_spieler SET
                    name = ?, geburtsjahr = ?, liga = ?, team = ?, groesse = ?,
                    foto_pfad = ?, leistung_pfad = ?
                WHERE id = ?
            """, (
                spieler.name, spieler.geburtsjahr, spieler.liga, spieler.team,
                spieler.groesse, spieler.foto_pfad, spieler.leistung_pfad, spieler_id
            ))

        self.verbindung.commit()

    # ------------------------------------------------------------------ #
    #  SPIELER FILTERN
    # ------------------------------------------------------------------ #

    def filter_spieler(self, sportart, liga=None, alter_min=None, alter_max=None,
                        groesse_min=None, groesse_max=None, linksfuss=None):
        """Spieler nach Kriterien filtern."""
        tabelle = "fussball_spieler" if sportart == "Fußball" else "volleyball_spieler"
        query = f"SELECT * FROM {tabelle} WHERE 1=1"
        params = []

        if liga:
            query += " AND liga = ?"
            params.append(liga)
        if alter_min:
            query += " AND (? - geburtsjahr) >= ?"
            params.extend([datetime.now().year, alter_min])
        if alter_max:
            query += " AND (? - geburtsjahr) <= ?"
            params.extend([datetime.now().year, alter_max])
        if groesse_min:
            query += " AND groesse >= ?"
            params.append(groesse_min)
        if groesse_max:
            query += " AND groesse <= ?"
            params.append(groesse_max)
        if linksfuss is not None and sportart == "Fußball":
            query += " AND linksfuss = ?"
            params.append(int(linksfuss))

        cursor = self.verbindung.cursor()
        cursor.execute(query, params)
        zeilen = cursor.fetchall()

        if sportart == "Fußball":
            return [self._zeile_zu_fussball_spieler(z) for z in zeilen]
        else:
            return [self._zeile_zu_volleyball_spieler(z) for z in zeilen]

    # ------------------------------------------------------------------ #
    #  LEISTUNG HINZUFÜGEN
    # ------------------------------------------------------------------ #

    def add_leistung(self, leistung):
        """Leistungseintrag speichern — erkennt automatisch ob Fußball oder Volleyball."""
        if not leistung.validiere():
            raise ValueError(f"Leistung ungültig: {leistung}")

        cursor = self.verbindung.cursor()

        if leistung.sportart == "Fußball":
            cursor.execute("""
                INSERT INTO fussball_leistung
                    (spieler_id, datum, heatmap_pfad, spielertyp, leistungswert, datei_pfad)
                VALUES (?, ?, ?, ?, ?, ?)
            """, (
                leistung.spieler_id, leistung.datum, leistung.heatmap_pfad,
                leistung.spielertyp, leistung.leistungswert, leistung.datei_pfad
            ))

        elif leistung.sportart == "Volleyball":
            cursor.execute("""
                INSERT INTO volleyball_leistung
                    (spieler_id, datum, schlagkraft, sprungkraft,
                     belastung, leistungspunkte, datei_pfad)
                VALUES (?, ?, ?, ?, ?, ?, ?)
            """, (
                leistung.spieler_id, leistung.datum, leistung.schlagkraft,
                leistung.sprungkraft, leistung.belastung,
                leistung.leistungspunkte, leistung.datei_pfad
            ))

        self.verbindung.commit()
        return cursor.lastrowid

    # ------------------------------------------------------------------ #
    #  LEISTUNG ABRUFEN
    # ------------------------------------------------------------------ #

    def get_leistungen(self, spieler_id, sportart):
        """Alle Leistungseinträge eines Spielers abrufen."""
        cursor = self.verbindung.cursor()

        if sportart == "Fußball":
            cursor.execute("""
                SELECT * FROM fussball_leistung
                WHERE spieler_id = ? ORDER BY datum DESC
            """, (spieler_id,))
            return [self._zeile_zu_fussball_leistung(z) for z in cursor.fetchall()]

        elif sportart == "Volleyball":
            cursor.execute("""
                SELECT * FROM volleyball_leistung
                WHERE spieler_id = ? ORDER BY datum DESC
            """, (spieler_id,))
            return [self._zeile_zu_volleyball_leistung(z) for z in cursor.fetchall()]

    # ------------------------------------------------------------------ #
    #  HILFSMETHODEN
    # ------------------------------------------------------------------ #

    def _zeile_zu_fussball_spieler(self, zeile):
        spieler = FussballSpieler(
            name=zeile["name"], geburtsjahr=zeile["geburtsjahr"],
            liga=zeile["liga"], team=zeile["team"], groesse=zeile["groesse"],
            linksfuss=bool(zeile["linksfuss"]), spielertyp=zeile["spielertyp"],
            foto_pfad=zeile["foto_pfad"], heatmap_pfad=zeile["heatmap_pfad"]
        )
        spieler.id = zeile["id"]
        spieler.erstellt_am = zeile["erstellt_am"]
        return spieler

    def _zeile_zu_volleyball_spieler(self, zeile):
        spieler = VolleyballSpieler(
            name=zeile["name"], geburtsjahr=zeile["geburtsjahr"],
            liga=zeile["liga"], team=zeile["team"], groesse=zeile["groesse"],
            foto_pfad=zeile["foto_pfad"], leistung_pfad=zeile["leistung_pfad"]
        )
        spieler.id = zeile["id"]
        spieler.erstellt_am = zeile["erstellt_am"]
        return spieler

    def _zeile_zu_fussball_leistung(self, zeile):
        leistung = FussballLeistung(
            spieler_id=zeile["spieler_id"], heatmap_pfad=zeile["heatmap_pfad"],
            spielertyp=zeile["spielertyp"], leistungswert=zeile["leistungswert"],
            datum=zeile["datum"], datei_pfad=zeile["datei_pfad"]
        )
        leistung.id = zeile["id"]
        return leistung

    def _zeile_zu_volleyball_leistung(self, zeile):
        leistung = VolleyballLeistung(
            spieler_id=zeile["spieler_id"], schlagkraft=zeile["schlagkraft"],
            sprungkraft=zeile["sprungkraft"], belastung=zeile["belastung"],
            leistungspunkte=zeile["leistungspunkte"], datum=zeile["datum"],
            datei_pfad=zeile["datei_pfad"]
        )
        leistung.id = zeile["id"]
        return leistung

    def schliessen(self):
        self.verbindung.close()