from pathlib import Path

ROOT_DIR = Path(__file__).parent.parent
DATA_PATH = ROOT_DIR / "data" / "psgouv_2023_data.csv"

APP_TITLE = "PSGOUV 2023 — Tableau de Bord"
APP_ICON = "🇨🇮"
APP_DESCRIPTION = (
    "Cette application met en lumière les réalisations de l'État de Côte d'Ivoire "
    "dans le cadre du Programme Social du Gouvernement (PSGOUV) 2023."
)

MENU_ITEMS = {
    "Get help": "https://www.linkedin.com/in/timothee-olanyi-akanji/",
    "Report a Bug": "https://github.com/TimFirst3005/PSGOUV-CI-2023-ANALYSIS/issues",
    "About": APP_DESCRIPTION,
}

COLUMNS = {
    "region": "Région",
    "district": "District",
    "category": "Catégorie",
    "subcategory": "Sous-catégorie",
    "designation": "Désignation",
    "value": "Valeur",
}

CHART_PRIMARY_COLOR = "#667eea"
CHART_COLOR_SCALE = "Purples"
