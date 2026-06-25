import streamlit as st

min_val, max_val = st.slider(
    "Bereich auswählen",
    min_value=0,
    max_value=100,
    value=(20, 80)   # <-- Tuple = Bereichs-Slider
)

#st.write(f"Von {min_val} bis {max_val}")