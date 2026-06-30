import streamlit as st

st.set_page_config(
    page_title="Trainer Suche",
    layout="wide",
)

FILTER_WIDTH = 320  # Breite der linken Filterspalte in px

st.markdown(
    f"""
    <style>
    /* Streamlit-Standardpadding entfernen, damit nichts am Rand "einrückt" */
    .block-container {{
        padding-top: 0rem;
        padding-bottom: 2rem;
        padding-left: 0rem;
        padding-right: 2rem;
        max-width: 100%;
    }}

    /* Die erste Spalte (= unsere Filterspalte) fix an den linken Browserrand pinnen */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type {{
        position: fixed;
        left: 0;
        top: 0;
        height: 100vh;
        width: {FILTER_WIDTH}px;
        overflow-y: auto;
        background-color: #1e1f26;
        padding: 0.8rem 1rem;
        z-index: 100;
    }}

    

    /* ── Abschnitts-Header ─────────────────────────────────────── */
    .filter-panel h4,
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type h4 {{
        color: #6b7280;
        font-size: 0.65rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        margin-bottom: 0.3rem;
        margin-top: 0.1rem;
    }}

    /* ── Pills (POSITION & TEST): gestapelte Karten ────────────── */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        [data-testid="stPills"] {{
        display: flex;
        flex-direction: column;
        gap: 0.25rem;
        margin-bottom: 0;
    }}
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        [data-testid="stPills"] button {{
        width: 100% !important;
        text-align: left !important;
        justify-content: flex-start !important;
        border-radius: 10px !important;
        border: 1px solid #2c2d38 !important;
        background-color: #22232c !important;
        color: #c9cdd6 !important;
        padding: 0.45rem 0.75rem !important;
        font-size: 0.84rem !important;
        transition: border-color 0.15s, background-color 0.15s;
    }}
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        [data-testid="stPills"] button:hover {{
        border-color: #7c6cf6 !important;
        color: #ffffff !important;
        background-color: #2a2b38 !important;
    }}
    /* Aktiver Pill: zartes Lila (wie im Screenshot) */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        [data-testid="stPills"] button[aria-pressed="true"],
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        [data-testid="stPills"] button[data-selected="true"] {{
        background-color: rgba(124, 108, 246, 0.18) !important;
        border-color: #7c6cf6 !important;
        color: #c4baff !important;
    }}

    /* ── Multiselect-Chips (SPIELERTYP) ────────────────────────── */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stMultiSelect span[data-baseweb="tag"] {{
        background-color: rgba(124, 108, 246, 0.22) !important;
        border-radius: 20px !important;
        color: #c4baff !important;
        font-size: 0.78rem !important;
    }}
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stMultiSelect [data-baseweb="select"] > div {{
        background-color: #22232c !important;
        border-color: #2c2d38 !important;
        border-radius: 10px !important;
    }}

    /* ── Slider ─────────────────────────────────────────────────── */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stSlider [data-testid="stThumbValue"],
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stSlider [data-testid="stTickBarMin"],
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stSlider [data-testid="stTickBarMax"] {{
        color: #9da3ae;
        font-size: 0.75rem;
    }}
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stSlider [role="slider"] {{
        background-color: #7c6cf6 !important;
        border-color: #7c6cf6 !important;
    }}
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stSlider [data-testid="stSliderTrackFill"] {{
        background-color: #7c6cf6 !important;
    }}

    /* ── Selectbox & Textinput ──────────────────────────────────── */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stSelectbox [data-baseweb="select"] > div,
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stTextInput input {{
        background-color: #22232c !important;
        border-color: #2c2d38 !important;
        border-radius: 10px !important;
        color: #c9cdd6 !important;
        font-size: 0.84rem !important;
    }}

    /* ── Abstände & Trennlinien ─────────────────────────────────── */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stSlider,
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stRadio,
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stMultiSelect,
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stSelectbox,
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stTextInput,
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        [data-testid="stPills"] {{
        margin-bottom: 0;
        padding-bottom: 0;
    }}
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type hr {{
        margin-top: 0.4rem;
        margin-bottom: 0.4rem;
        border-color: #2c2d38;
    }}
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stMarkdown p {{
        margin: 0;
        line-height: 1.2;
    }}

    /* ── Radio (FUSS) ───────────────────────────────────────────── */
    div[data-testid="stHorizontalBlock"] > div[data-testid="column"]:first-of-type
        .stRadio label {{
        color: #c9cdd6;
        font-size: 0.84rem;
    }}

    div.stButton > button {{
        width: 100%;
        text-align: left;
        border-radius: 10px;
        border: 1px solid #2c2d38;
        background-color: #22232c;
        color: #c9cdd6;
        margin-bottom: 0.25rem;
        padding: 0.45rem 0.75rem;
        font-size: 0.84rem;
    }}
    div.stButton > button:hover {{
        border-color: #7c6cf6;
        color: #ffffff;
    }}
    .pill-active button {{
        background-color: rgba(124, 108, 246, 0.18) !important;
        border-color: #7c6cf6 !important;
        color: #c4baff !important;
    }}
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    f"<div style='padding-left:{320 + 20}px; padding-top:1.5rem;'>",
    unsafe_allow_html=True,
)
st.header("Trainer Suche")
st.markdown("</div>", unsafe_allow_html=True)


def spieler_inserat_fußball():
    st.markdown(
        f"<div style='padding-left:{320 + 20}px;'>",
        unsafe_allow_html=True,
    )
    st.title("Hier kannst du nach deinem Wunschspieler suchen.")
    st.markdown("</div>", unsafe_allow_html=True)

    sportart = "Fußball"

    # -----------------------------------------------------------------
    # Layout: links fixe Filterspalte, rechts Inhalt
    # -----------------------------------------------------------------
    filter_col, content_col = st.columns([1, 3], gap="large")

    # ===================================================================
    # LINKE SPALTE – immer sichtbare Filter
    # ===================================================================
    with filter_col:
        st.markdown('<div class="filter-panel">', unsafe_allow_html=True)

        # --- POSITION -----------------------------------------------------
        st.markdown("#### POSITION")

        positionen = [
            "Torwart",
            "Verteidigung",
            "Mittelfeld",
            "Sturm",
]

        position = st.pills(
             "Position",
            positionen,
            selection_mode="single",
            label_visibility="collapsed",
            default="Torwart",
)

        st.markdown("---")

        # --- SPIELERTYP -----------------------------------------------------
        st.markdown("#### SPIELERTYP")
        spielertyp = st.multiselect(
            "Spielertyp",
            ["Schnell", "Agil", "Ausdauer", "Kraft", "Technik"],
            label_visibility="collapsed",
        )

        st.markdown("---")

        # --- ALTER -----------------------------------------------------
        st.markdown("#### ALTER")
        alter_min, alter_max = st.slider(
            "Alter in Jahren auswählen",
            min_value=0,
            max_value=100,
            value=(18, 28),
            label_visibility="collapsed",
        )

        # --- GRÖSSE -----------------------------------------------------
        st.markdown("#### GRÖSSE")
        groesse_min, groesse_max = st.slider(
            "Größe in cm auswählen",
            min_value=100,
            max_value=250,
            value=(100, 250),
            label_visibility="collapsed",
        )

        # --- SPRINTGESCHWINDIGKEIT -----------------------------------------------------
        st.markdown("#### SPRINTGESCHWINDIGKEIT")
        speed_min, speed_max = st.slider(
            "Sprintgeschwindigkeit in km/h auswählen",
            min_value=0,
            max_value=50,
            value=(0, 50),
            label_visibility="collapsed",
        )

        # --- SCHUSSKRAFT -----------------------------------------------------
        st.markdown("#### SCHUSSKRAFT")
        kraft_min, kraft_max = st.slider(
            "Schusskraft in km/h auswählen",
            min_value=0,
            max_value=200,
            value=(0, 200),
            label_visibility="collapsed",
        )

        st.markdown("---")

        # --- FUSS -----------------------------------------------------
        st.markdown("#### FUSS")
        fuß = st.radio("Fuß", ["Rechts", "Links"], label_visibility="collapsed")

        st.markdown("---")

        # --- TEST -----------------------------------------------------
        st.markdown("#### TEST")
        test_optionen = ["Lauftest 12 min", "Belastungs-EKG", "Ruhe-EKG"]
        test = st.pills(
            "Test",
            test_optionen,
            selection_mode="single",
            label_visibility="collapsed",
            default="Lauftest 12 min",
        )

        st.markdown("</div>", unsafe_allow_html=True)
        spiel_status = st.selectbox("Spielstatus", ["Aktiv", "Inaktiv", "Verletzt"])

        if spiel_status == "Aktiv":
            liga = st.selectbox(
                "Aktuelle Liga",
                [
                    "1. Bundesliga",
                    "2. Bundesliga",
                    "Regionalliga",
                    "HYPO Tirol Liga",
                    "Landesliga",
                    "Gebietsliga",
                    "Bezirksliga",
                    "1. Klasse",
                    "2. Klasse",
                    "Reserve",
                ],
            )
            verein = st.text_input("Verein")
        else:
            liga = st.selectbox(
                "Letzte Liga",
                [
                    "1. Bundesliga",
                    "2. Bundesliga",
                    "Regionalliga",
                    "HYPO Tirol Liga",
                    "Landesliga",
                    "Gebietsliga",
                    "Bezirksliga",
                    "1. Klasse",
                    "2. Klasse",
                    "Reserve",
                ],
            )
            verein = st.text_input("Letzter Verein")





spieler_inserat_fußball()