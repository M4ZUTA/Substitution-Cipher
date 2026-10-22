from collections import Counter
from html import escape
from string import ascii_uppercase

import pandas as pd
import plotly.express as px
import streamlit as st

from Cryptanalysis import calculate_letter_frequencies


st.set_page_config(
    page_title="Frequency Analyzer",
    page_icon="🔐",
    layout="wide",
)

st.markdown(
    """
    <style>
    :root {
        color-scheme: dark;
    }
    .stApp {
        background: #10151d;
        color: #eef2f5;
    }
    [data-testid="stHeader"] {
        background: rgba(16, 21, 29, 0.9);
    }
    [data-testid="stSidebar"] {
        background: #151c25;
    }
    .block-container {
        max-width: 1440px;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }
    .eyebrow {
        color: #59cf72;
        font-size: 0.78rem;
        font-weight: 700;
        letter-spacing: 0.13em;
        text-transform: uppercase;
    }
    .hero-title {
        margin: 0.35rem 0 0.25rem;
        font-size: clamp(2rem, 4vw, 3rem);
        font-weight: 750;
        letter-spacing: -0.04em;
    }
    .hero-copy, .section-copy {
        color: #9ba8b7;
    }
    .section-title {
        margin: 1.4rem 0 0.2rem;
        font-size: 1.25rem;
        font-weight: 700;
    }
    .preview {
        min-height: 220px;
        max-height: 420px;
        overflow: auto;
        padding: 1.1rem;
        border: 1px solid #303b48;
        border-radius: 10px;
        background: #151b24;
        color: #c9d2dc;Crypta
        font-family: ui-monospace, SFMono-Regular, Menlo, monospace;
        font-size: 0.95rem;
        line-height: 1.8;
        overflow-wrap: anywhere;
        white-space: pre-wrap;
    }
    .preview .mapped {
        color: #66df80;
        font-weight: 700;
    }
    .preview .unmapped {
        color: #d7a65e;
    }
    div[data-testid="stMetric"] {
        padding: 0.9rem 1rem;
        border: 1px solid #303b48;
        border-radius: 10px;
        background: #151b24;
    }
    div[data-testid="stMetricLabel"] {
        color: #9ba8b7;
    }
    div.stButton > button[kind="secondary"] {
        border-color: #3d4b58;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

if "ciphertext" not in st.session_state:
    st.session_state.ciphertext = ""
for letter in ascii_uppercase:
    st.session_state.setdefault(f"mapping_{letter}", "")

st.markdown('<div class="eyebrow">Cryptanalysis workspace</div>', unsafe_allow_html=True)
st.markdown(
    '<h1 class="hero-title">Substitution Cipher Frequency Analyzer</h1>',
    unsafe_allow_html=True,
)
st.markdown(
    '<p class="hero-copy">Explore letter patterns, test substitutions, and watch your message take shape.</p>',
    unsafe_allow_html=True,
)

st.markdown('<div class="section-title">01 &nbsp; Ciphertext</div>', unsafe_allow_html=True)
st.markdown(
    '<p class="section-copy">Paste or edit your encrypted message. Only A–Z letters are included in frequency analysis.</p>',
    unsafe_allow_html=True,
)
ciphertext = st.text_area(
    "Ciphertext",
    key="ciphertext",
    height=180,
    placeholder="Paste your ciphertext here…",
    label_visibility="collapsed",
)

letter_count = sum(char.isascii() and char.isalpha() for char in ciphertext)
frequencies = calculate_letter_frequencies(ciphertext)
mapping_values = {
    letter: st.session_state[f"mapping_{letter}"].strip()
    for letter in ascii_uppercase
}
mapping = {
    letter: value.upper()
    for letter, value in mapping_values.items()
    if value.isascii() and value.isalpha()
}
invalid_mappings = [
    letter for letter, value in mapping_values.items() if value and letter not in mapping
]
mapped_count = len(mapping)

metric_columns = st.columns(3)
metric_columns[0].metric("Letters analyzed", f"{letter_count:,}")
metric_columns[1].metric("Different letters", len(frequencies))
metric_columns[2].metric("Mappings applied", f"{mapped_count} / 26")

st.markdown('<div class="section-title">02 &nbsp; Frequency analysis</div>', unsafe_allow_html=True)
st.markdown(
    '<p class="section-copy">Compare the message against typical English letter frequencies.</p>',
    unsafe_allow_html=True,
)

english_frequencies = {
    "A": 8.17, "B": 1.49, "C": 2.78, "D": 4.25, "E": 12.70,
    "F": 2.23, "G": 2.02, "H": 6.09, "I": 6.97, "J": 0.15,
    "K": 0.77, "L": 4.03, "M": 2.41, "N": 6.75, "O": 7.51,
    "P": 1.93, "Q": 0.10, "R": 5.99, "S": 6.33, "T": 9.06,
    "U": 2.76, "V": 0.98, "W": 2.36, "X": 0.15, "Y": 1.97,
    "Z": 0.07,
}
chart_data = pd.DataFrame(
    [
        {"Letter": letter, "Series": "Ciphertext", "Frequency (%)": frequencies.get(letter, 0) * 100}
        for letter in ascii_uppercase
    ]
    + [
        {"Letter": letter, "Series": "Typical English", "Frequency (%)": english_frequencies[letter]}
        for letter in ascii_uppercase
    ]
)
chart = px.bar(
    chart_data,
    x="Letter",
    y="Frequency (%)",
    color="Series",
    barmode="group",
    color_discrete_map={"Ciphertext": "#35b64a", "Typical English": "#596779"},
    template="plotly_dark",
)
chart.update_layout(
    paper_bgcolor="rgba(0,0,0,0)",
    plot_bgcolor="rgba(0,0,0,0)",
    font_color="#cbd4de",
    legend_title_text="",
    margin=dict(l=8, r=8, t=20, b=8),
    height=330,
)
chart.update_xaxes(showgrid=False, title_text="")
chart.update_yaxes(gridcolor="#293441", title_text="Percent of letters")
st.plotly_chart(chart, use_container_width=True, config={"displayModeBar": False})

st.markdown('<div class="section-title">03 &nbsp; Decryption workbench</div>', unsafe_allow_html=True)
st.markdown(
    '<p class="section-copy">Map each cipher letter to a plaintext letter. Mapped letters appear green; unresolved letters appear amber.</p>',
    unsafe_allow_html=True,
)

mapping_column, preview_column = st.columns([1.1, 0.9], gap="large")
with mapping_column:
    st.markdown("**Substitution map**")
    reset_column, hint_column = st.columns([1, 2])
    with reset_column:
        if st.button("Reset mappings", use_container_width=True):
            for letter in ascii_uppercase:
                st.session_state[f"mapping_{letter}"] = ""
            st.rerun()
    with hint_column:
        st.caption("Enter one letter per field. Spaces and punctuation are preserved.")

    left_grid, right_grid = st.columns(2, gap="medium")
    for index, letter in enumerate(ascii_uppercase):
        grid = left_grid if index < 13 else right_grid
        with grid:
            st.text_input(
                f"{letter} →",
                key=f"mapping_{letter}",
                max_chars=1,
                placeholder="—",
            )

if invalid_mappings:
    st.warning(
        "Use one A–Z letter in each mapping field. Invalid entries were ignored: "
        + ", ".join(invalid_mappings)
        + "."
    )
duplicate_targets = sorted(
    target for target, count in Counter(mapping.values()).items() if count > 1
)
if duplicate_targets:
    st.warning(
        "More than one cipher letter maps to "
        + ", ".join(duplicate_targets)
        + ". A substitution alphabet usually uses each plaintext letter once."
    )

with preview_column:
    st.markdown("**Live decryption preview**")
    if not ciphertext:
        st.info("Add ciphertext above to see your decryption preview.")
    else:
        preview = "".join(
            f'<span class="mapped">{escape(mapping[char.upper()])}</span>'
            if char.isascii() and char.isalpha() and char.upper() in mapping
            else f'<span class="unmapped">{escape(char.lower())}</span>'
            if char.isascii() and char.isalpha()
            else escape(char)
            for char in ciphertext
        )
        st.markdown(f'<div class="preview">{preview}</div>', unsafe_allow_html=True)
