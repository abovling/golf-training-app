import streamlit as st

st.title("Golftræning – Træning A")

st.markdown("""
### Træning A plan:
- **0–10 min:** Opvarmning med halve SW og 56° wedge (30–50 m). Fokus på kontakt og balance.
- **10–25 min:** Pitch med PW, SW og 56° fra 30–70 m. Skift afstand og kølle. Mål: Ram 5/10 inden for greenområde.
- **25–35 min:** Chips fra 10–20 m. Øv forskellige lies (kort græs, semirough). Skift mellem PW og 56°.
- **35–45 min:** ‘Up & down’-øvelse: Chip + putt. 5 bolde – mål: Lav 2 pars.
- **45–60 min:** Lang putting (10–15 m). Fokus på afstandskontrol. Øvelse: 2-putt challenge eller GolfBoy lag putting.
""")

# Inputs til hver øvelse
opvarmning = st.text_input("0–10 min: Kommentar eller antal gentagelser", "")
pitch = st.slider("10–25 min: Antal ramte inden for greenområde (0–10)", 0, 10, 0)
chips = st.text_input("25–35 min: Kommentar eller antal gentagelser", "")
up_down = st.number_input("35–45 min: Antal pars lavet (mål: 2)", min_value=0, max_value=5, value=0)
lang_putting = st.text_input("45–60 min: Kommentar eller score på øvelse", "")

# Generer rapport
if st.button("Generer rapport"):
    rapport = f"""
    Golftræning – Træning A rapport

    0–10 min – Opvarmning: {opvarmning}
    10–25 min – Pitch (ramte inden for greenområde): {pitch}/10
    25–35 min – Chips: {chips}
    35–45 min – Up & down (pars lavet): {up_down} / 5 (mål 2)
    45–60 min – Lang putting: {lang_putting}
    """
    st.text_area("Rapport klar til kopiering:", rapport, height=250)
