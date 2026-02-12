# app/io/paths.py
from pathlib import Path

# __file__ aponta para este arquivo; subimos até /app
APP_DIR = Path(__file__).resolve().parents[1]   # .../app
DATA_DIR = APP_DIR / "data"                     # .../app/data

PEDIDOS_XLSX = DATA_DIR / "pedidos.xlsx"
DEPARA_XLSX = DATA_DIR / "depara_agencias.xlsx"