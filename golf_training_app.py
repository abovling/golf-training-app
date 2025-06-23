import streamlit as st
import streamlit.components.v1 as components

st.title("GOLFTRÆNING 🏌️‍♂️")
st.caption("Golftræning af Anders Bøvling (2025)")

# Træningstyper
træningstyper = {
    "A": {
        "plan": """
- **0–10 min:** Opvarmning med halve SW og 56° wedge (30–50 m). Fokus på kontakt og balance.
- **10–25 min:** Pitch med PW, SW og 56° fra 30–70 m. Skift afstand og kølle. Mål: Ram 5/10 inden for greenområde.
- **25–35 min:** Chips fra 10–20 m. Øv forskellige lies (kort græs, semirough). Skift mellem PW og 56°.
- **35–45 min:** ‘Up & down’-øvelse: Chip + putt. 5 bolde – mål: Lav 2 pars.
- **45–60 min:** Lang putting (10–15 m). Fokus på afstandskontrol. Øvelse: 2-putt challenge eller GolfBoy lag putting.
""",
        "øvelser": [
            ("0–10 min: Kommentar eller antal gentagelser", "text_input"),
            ("10–25 min: Antal ramte inden for greenområde (0–10)", "slider", 0, 10, 0),
            ("25–35 min: Kommentar eller antal gentagelser", "text_input"),
            ("35–45 min: Antal pars lavet (mål: 2)", "number_input", 0, 5, 0),
            ("45–60 min: Kommentar eller score på øvelse", "text_input"),
        ],
    },
    "B": {
        "plan": "Her kan du tilføje træningsplan for B...",
        "øvelser": [
            ("Øvelse 1 for B", "text_input"),
            ("Øvelse 2 for B", "number_input", 0, 10, 0),
        ],
    },
    "C": {
        "plan": "Her kan du tilføje træningsplan for C...",
        "øvelser": [
            ("Øvelse 1 for C", "text_input"),
            ("Øvelse 2 for C", "number_input", 0, 10, 0),
        ],
    },
    "D": {
        "plan": "Her kan du tilføje træningsplan for D...",
        "øvelser": [
            ("Øvelse 1 for D", "text_input"),
            ("Øvelse 2 for D", "number_input", 0, 10, 0),
        ],
    },
    "E": {
        "plan": "Her kan du tilføje træningsplan for E...",
        "øvelser": [
            ("Øvelse 1 for E", "text_input"),
            ("Øvelse 2 for E", "number_input", 0, 10, 0),
        ],
    },
}

valgt_træning = st.selectbox("Vælg træningstype:", list(træningstyper.keys()))

st.markdown("### Træningsplan")
st.markdown(træningstyper[valgt_træning]["plan"])

# Gem input værdier
resultater = []

for øvelse in træningstyper[valgt_træning]["øvelser"]:
    label = øvelse[0]
    input_type = øvelse[1]
    if input_type == "text_input":
        val = st.text_input(label)
    elif input_type == "slider":
        val = st.slider(label, øvelse[2], øvelse[3], øvelse[4])
    elif input_type == "number_input":
        val = st.number_input(label, min_value=øvelse[2], max_value=øvelse[3], value=øvelse[4])
    else:
        val = None
    resultater.append((label, val))

# Generer rapport
if st.button("Generer rapport"):
    rapport = f"Golftræning – Træning {valgt_træning} rapport\n\n"
    for label, val in resultater:
        rapport += f"{label}: {val}\n"
    st.text_area("Rapport klar til kopiering:", rapport, height=250)

    # Kopier-knap med JavaScript
    import streamlit.components.v1 as components
    components.html(f"""
    <script>
    function copyToClipboard() {{
        const text = `{rapport}`;
        navigator.clipboard.writeText(text).then(function() {{
            alert('Rapport kopieret til udklipsholder!');
        }}, function(err) {{
            alert('Fejl ved kopiering: ' + err);
        }});
    }}
    </script>
    <button onclick="copyToClipboard()">Kopier rapport</button>
    """, height=50)
