# 🇨🇮 PSGOUV-CI 2023 — Tableau de Bord

Tableau de bord interactif des réalisations du **Programme Social du Gouvernement (PSGOUV)** de Côte d'Ivoire pour l'année 2023.

[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/TimFirst3005/PSGOUV-CI-2023-ANALYSIS)

---

## Aperçu

Cette application Streamlit visualise les 363 actions menées par l'État ivoirien dans le cadre du PSGOUV 2023, réparties sur **33 régions** et **24 districts**, couvrant trois domaines principaux :

| Domaine | Description |
|---|---|
| **Électricité & Hydraulique** | Électrification des localités, réparation de pompes à motricité humaine (PMH) |
| **Protection Sociale** | Filets sociaux, transferts monétaires |
| **Santé** | Interventions en santé communautaire |

---

## Fonctionnalités

- **Indicateurs clés** : nombre de programmes, total des actions, districts et régions impactés
- **Top bénéficiaires** : classement par district, région, catégorie et sous-catégorie
- **Treemap interactif** : vue hiérarchique District > Région > Catégorie
- **Graphiques de répartition** : distributions par région, district, catégorie et sous-catégorie

---

## Stack Technique

| Composant | Technologie |
|---|---|
| Framework web | [Streamlit](https://streamlit.io) ≥ 1.56 |
| Manipulation de données | [Pandas](https://pandas.pydata.org) ≥ 3.0 |
| Visualisations | [Plotly](https://plotly.com/python/) ≥ 6.7 |
| Gestionnaire de paquets | [uv](https://docs.astral.sh/uv/) |
| Runtime | Python 3.11 |

---

## Lancer l'application

### Prérequis

- Python 3.11+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

### Installation & démarrage

```bash
# Cloner le dépôt
git clone https://github.com/TimFirst3005/PSGOUV-CI-2023-ANALYSIS.git
cd PSGOUV-CI-2023-ANALYSIS

# Installer les dépendances
uv sync

# Lancer l'application
uv run streamlit run app.py
```

L'application sera disponible sur [http://localhost:8501](http://localhost:8501).

### Dev Container (VS Code / GitHub Codespaces)

Ouvrez le projet dans VS Code avec l'extension **Dev Containers** ou directement dans **GitHub Codespaces** — l'environnement et l'application se lancent automatiquement.

---

## Structure du Projet

```
psgouv-ci-2023/
├── .devcontainer/
│   └── devcontainer.json       # Configuration Dev Container
├── .streamlit/
│   └── config.toml             # Thème et configuration Streamlit
├── config/
│   ├── __init__.py
│   ├── css.py                  # Styles CSS centralisés
│   └── settings.py             # Constantes de l'application
├── data/
│   └── psgouv_2023_data.csv    # Jeu de données (363 enregistrements)
├── notebooks/
│   └── data_profiling.ipynb    # Analyse exploratoire des données
├── app.py                      # Point d'entrée Streamlit
├── data_loader.py              # Chargement et mise en cache des données
├── utils.py                    # Fonctions d'agrégation et KPIs
└── pyproject.toml              # Configuration du projet (uv)
```

---

## Données

- **Source** : Programme Social du Gouvernement de Côte d'Ivoire — Réalisations 2023
- **Format** : CSV (UTF-8), 363 lignes × 6 colonnes
- **Colonnes** : Région, District, Catégorie, Sous-catégorie, Désignation, Valeur

---

## Auteur

**Timothée AKANJI** — Data | BI | Python & SQL | Cloud | Santé & Humanitaire Afrique

[![LinkedIn](https://img.shields.io/badge/LinkedIn-0077B5?style=flat&logo=linkedin&logoColor=white)](https://www.linkedin.com/in/timothee-olanyi-akanji/)

---

*Licence MIT — voir [LICENSE](LICENSE)*
