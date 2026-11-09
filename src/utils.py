"""Funciones compartidas del TP."""
from pathlib import Path

import pandas as pd

RAIZ = Path(__file__).resolve().parents[1]
DATOS_RAW = RAIZ / "data" / "raw" / "Datos.txt"
DATOS_PROCESADOS = RAIZ / "data" / "processed"

TARGET = "Type of Answer"


def cargar_datos() -> pd.DataFrame:
    """Lee el dataset original (separado por ';' y codificado en Windows-1252)."""
    return pd.read_csv(DATOS_RAW, sep=";", encoding="cp1252")
