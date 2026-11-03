print("------------Paso 1: Cargar y explorar--------------------")
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib as mpl
import matplotlib.pyplot as plt
import re
from pathlib import Path


# Construye las rutas desde la ubicación de este archivo, no desde la
# carpeta actual de la terminal.
project_dir = Path(__file__).resolve().parents[1]
data_dir = project_dir / "data"

traffic = pd.read_csv(data_dir / "tomtom_traffic.csv")
eco = pd.read_csv(data_dir / "oecd_city_economy.csv")

print("Tráfico:")
print(traffic.head())
print("\nEconomía:")
print(eco.head())

print("------------Paso 2: Explorar, limpiar y preparar los datos--------------------")

