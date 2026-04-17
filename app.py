import streamlit as st
import pandas as pd

from utils import data, dim, count_col, top_N_par_col, sum_actions_par_col, nbre_program, nbre_actions_effectuee, most_benefit


# CSS de base 
st.markdown("""
<style>
    .main-header {
        padding: 1rem 0;
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        text-align: center;
        margin-bottom: 2rem;
        border-radius: 10px;
    }
</style>
""", unsafe_allow_html=True)


# Interface principale
st.markdown(f"""
<div class="main-header">
    <h1>🏠 Programme Social du Gouvernement <br> (PSGOUV) 2023 </h1>
</div>
""", unsafe_allow_html=True)

st.set_page_config(page_title="Accueil | PSGOUV 2023",
                   page_icon="🚀",
                   layout="wide",
                   initial_sidebar_state= "expanded",
                    menu_items= {
                        "Get help" : "https://www.linkedin.com/in/timothee-olanyi-akanji/",
                        "Report a Bug" : "https://github.com/TimFirst3005/PSGOUV-CI-2023-ANALYSIS/issues",                        
                        "About" : "Cette application Web met en lumière les programmes de l'état de Côte d'Ivoire dans le cadre du **PSGOUV 2023** ainsi que les actions ménées lors de la réalisation de chacun de ces programmes."
                    }
                   )


st.sidebar.title("Aperçu Global")
#st.sidebar.selectbox(
#    "Filtres",
#    ["Région","Type d'action"],
#    label_visibility= "hidden",
#    accept_new_options=False
#)


st.markdown("""
            Le jeu de données utilisé porte sur les réalisations de **l'Etat de Côte d'Ivoire** dans le cadre du **PSGOUV (Programme Social du Gouvernement)**. 
            Cette application est un outil précieux pour évaluer l'impact des initiatives gouvernementales sur la vie des populations en Côte d'Ivoire. 
            Elle couvre des domaines essentiels tels que l'hydraulique, la protection sociale, la santé, et l'électricité, offrant une vision globale 
            des progrès réalisés dans ces secteurs clés. Les données détaillées sur les PMH, les programmes de filets sociaux, les interventions en matière de santé, 
            et l'électrification des localités montrent l'engagement du gouvernement à améliorer les conditions de vie et à promouvoir le bien-être des citoyens. \n
""", unsafe_allow_html=True)


# Overview
st.markdown("### 👁️ Aperçu Global des Programmes")

row = st.container(horizontal=True, border=True, width="stretch", vertical_alignment="center")
with row:
    st.metric(
        "Nombre de Programmes réalisés", nbre_program, border=True
    )

    st.metric(
        "Nombre d'actions ménées", nbre_actions_effectuee, format='localized', border=True
    )


row = st.container(horizontal=True, border=True, width="stretch", vertical_alignment="center")
with row:
    st.metric(
        "Districts impactés", count_col("District"), border=True, chart_data=sum_actions_par_col("District"), chart_type="bar"
    )

    st.metric(
        "Régions impactées", count_col("Région"), border=True, chart_data=sum_actions_par_col("Région"), chart_type="bar"
    )

    st.metric(
        "Catégories de Programme", count_col("Catégorie"), border=True, chart_data=sum_actions_par_col("Catégorie"), chart_type="area"
    )

    st.metric(
        "Sous-catégories de Programme", count_col("Sous-catégorie"), border=True, chart_data=sum_actions_par_col("Sous-catégorie"), chart_type="area"
    )


st.markdown("### 🔝 TOP_N (Actions menées) ")
row = st.container(horizontal=True, border=True, width="stretch", vertical_alignment="center")
with row:
    st.metric(
        "Top District Bénéficiaire", most_benefit("District")[1], delta=most_benefit("District")[0], format="localized", delta_arrow="off", border=True
    )
    st.metric(
        "Top Région Bénéficiaire", most_benefit("Région")[1], delta=most_benefit("Région")[0], format="localized", delta_arrow="off", border=True
    )
    st.metric(
        "Top Catégorie d'action", most_benefit("Catégorie")[1], delta=most_benefit("Catégorie")[0], format="localized", delta_arrow="off", border=True
    )
    st.metric(
        "Top Sous-Catégorie d'action", most_benefit("Sous-catégorie")[1], delta=most_benefit("Sous-catégorie")[0], format="localized", delta_arrow="off", border=True
    )


st.markdown("### 🌍 Repartition Géographique des action")
st.map( size="Valeur")


st.markdown("### 📊 Repartition des Actions ménées")


row = st.container(horizontal=True, border=True, width="stretch", vertical_alignment="center")
with row:
    st.markdown("##### Repartition \n ##### par Régions")
    st.bar_chart(sum_actions_par_col("Région"))

row = st.container(horizontal=True, border=True, width="stretch", vertical_alignment="center")
with row:
    st.bar_chart(sum_actions_par_col("District"))
    st.markdown("##### Repartition \n ##### par District")

row = st.container(horizontal=True, border=True, width="stretch", vertical_alignment="distribute")
with row:
    st.bar_chart(sum_actions_par_col("Catégorie"), horizontal=True)
    st.bar_chart(sum_actions_par_col("Sous-catégorie"), horizontal=True)


st.markdown("---")
    
_,col,_ = st.columns([1,98,1], vertical_alignment="center", gap="large")
with col :
    st.markdown("""
                ***PSGOUV-CI 2023*** — Données du Programme Social du Gouvernement(PSGOUV) - Les réalisations en 2023

                Cette application vient pour en lumière les activités du PSGOUV 2023 en Côte d'Ivoire.

                :material/copyright: Réalisé par [***Timothée AKANJI***](https://www.linkedin.com/in/timothee-olanyi-akanji/ "Expertise Data | BI | Python & SQL Expert | Cloud | Santé & Humanitaire Afrique") 
        """, text_alignment="center")
    