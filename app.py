import plotly.express as px
import streamlit as st

from config.css import MAIN_CSS
from config.settings import APP_ICON, APP_TITLE, COLUMNS, MENU_ITEMS
from data_loader import load_data
from utils import (
    count_unique,
    sum_by_col,
    top_beneficiary,
    total_actions,
    total_programs,
    treemap_data,
)

# ── Page config — must be the very first Streamlit call ───────────────────────
st.set_page_config(
    page_title=APP_TITLE,
    page_icon=APP_ICON,
    layout="wide",
    initial_sidebar_state="expanded",
    menu_items=MENU_ITEMS,
)

st.markdown(MAIN_CSS, unsafe_allow_html=True)

# ── Data ──────────────────────────────────────────────────────────────────────
df = load_data()

C = COLUMNS  # local alias for readability

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("Navigation")
    st.markdown(
        "Explorez les réalisations du **PSGOUV 2023** à travers les indicateurs "
        "clés et les visualisations interactives."
    )
    st.divider()
    st.caption(f"Données : {total_programs(df)} enregistrements chargés.")

# ── Header ────────────────────────────────────────────────────────────────────
st.markdown(
    """
    <div class="main-header">
        <h1>🇨🇮 Programme Social du Gouvernement (PSGOUV) 2023</h1>
        <p>Tableau de bord des réalisations — Côte d'Ivoire</p>
    </div>
    """,
    unsafe_allow_html=True,
)

st.markdown(
    """
    <div class="intro-text">
    Le jeu de données porte sur les réalisations de l'<strong>État de Côte d'Ivoire</strong>
    dans le cadre du <strong>PSGOUV</strong> (Programme Social du Gouvernement).
    Il couvre des domaines essentiels tels que l'hydraulique, la protection sociale,
    la santé et l'électricité, offrant une vision globale des progrès réalisés en 2023.
    </div>
    """,
    unsafe_allow_html=True,
)

# ── Section 1 : Aperçu Global ─────────────────────────────────────────────────
st.markdown("### 👁️ Aperçu Global des Programmes")

row1 = st.container(horizontal=True, border=True, width="stretch", vertical_alignment="center")
with row1:
    st.metric("Programmes réalisés", total_programs(df), border=True)
    st.metric("Actions menées", total_actions(df), format="localized", border=True)

row2 = st.container(horizontal=True, border=True, width="stretch", vertical_alignment="center")
with row2:
    st.metric(
        "Districts impactés",
        count_unique(df, C["district"]),
        border=True,
        chart_data=sum_by_col(df, C["district"]),
        chart_type="bar",
    )
    st.metric(
        "Régions impactées",
        count_unique(df, C["region"]),
        border=True,
        chart_data=sum_by_col(df, C["region"]),
        chart_type="bar",
    )
    st.metric(
        "Catégories de programme",
        count_unique(df, C["category"]),
        border=True,
        chart_data=sum_by_col(df, C["category"]),
        chart_type="area",
    )
    st.metric(
        "Sous-catégories",
        count_unique(df, C["subcategory"]),
        border=True,
        chart_data=sum_by_col(df, C["subcategory"]),
        chart_type="area",
    )

# ── Section 2 : Top Bénéficiaires ────────────────────────────────────────────
st.markdown("### 🔝 Top Bénéficiaires par Dimension")

top_dims = [
    ("Top District", "district"),
    ("Top Région", "region"),
    ("Top Catégorie", "category"),
    ("Top Sous-Catégorie", "subcategory"),
]

row3 = st.container(horizontal=True, border=True, width="stretch", vertical_alignment="center")
with row3:
    for label, col_key in top_dims:
        name, value = top_beneficiary(df, C[col_key])
        st.metric(
            label,
            name,
            delta=value,
            format="localized",
            delta_arrow="off",
            border=True,
        )

# ── Section 3 : Répartition Géographique ─────────────────────────────────────
st.markdown("### 🌍 Répartition Géographique des Actions")

geo_df = treemap_data(df)
fig_treemap = px.treemap(
    geo_df,
    path=[px.Constant("Côte d'Ivoire"), C["district"], C["region"], C["category"]],
    values=C["value"],
    color=C["value"],
    color_continuous_scale="Purples",
    hover_data={C["value"]: ":,.0f"},
)
fig_treemap.update_layout(
    margin=dict(t=10, l=0, r=0, b=0),
    height=480,
    coloraxis_colorbar=dict(title="Actions"),
)
fig_treemap.update_traces(textinfo="label+value")
st.plotly_chart(fig_treemap, use_container_width=True)

# ── Section 4 : Répartition des Actions ──────────────────────────────────────
st.markdown("### 📊 Répartition des Actions Menées")

row4 = st.container(horizontal=True, border=True, width="stretch", vertical_alignment="center")
with row4:
    st.markdown("##### Par Région")
    st.bar_chart(sum_by_col(df, C["region"]))

row5 = st.container(horizontal=True, border=True, width="stretch", vertical_alignment="center")
with row5:
    st.bar_chart(sum_by_col(df, C["district"]))
    st.markdown("##### Par District")

row6 = st.container(
    horizontal=True, border=True, width="stretch", vertical_alignment="distribute"
)
with row6:
    st.bar_chart(sum_by_col(df, C["category"]), horizontal=True)
    st.bar_chart(sum_by_col(df, C["subcategory"]), horizontal=True)

# ── Footer ────────────────────────────────────────────────────────────────────
st.markdown("---")
_, col, _ = st.columns([1, 98, 1], vertical_alignment="center", gap="large")
with col:
    st.markdown(
        """
        ***PSGOUV-CI 2023*** — Données du Programme Social du Gouvernement — Réalisations 2023

        :material/copyright: Réalisé par [***Timothée AKANJI***](https://www.linkedin.com/in/timothee-olanyi-akanji/ "Data | BI | Python & SQL | Cloud | Santé & Humanitaire Afrique")
        """,
        text_alignment="center",
    )
