# =========================
# CREATIVIDAD DIGITAL
# =========================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# -----------------
# Cargar datos
# ----------------

# el archivo está en el mismo directorio
df = pd.read_csv("campanas_creatividad_digital.csv")

# limpiar nombres de columnas
df.columns = df.columns.str.strip().str.lower()

print("Columnas disponibles:")
print(df.columns)


# --------------------
# Métricas derivadas
# -------------------

df["ctr"] = df["clicks"] / df["impresiones"]
df["cvr"] = df["conversiones"] / df["clicks"]
df["roi"] = (df["ingresos_usd"] - df["costo_usd"]) / df["costo_usd"]

print("\nPrimeros datos con métricas:")
print(df.head())


# --------------------
# Métricas generales
# --------------------

total_campanas = len(df)
costo_total = df["costo_usd"].sum()
ingresos_totales = df["ingresos_usd"].sum()
roi_promedio = df["roi"].mean()

print("\n--- RESUMEN GENERAL ---")
print("Total campañas:", total_campanas)
print("Costo total:", round(costo_total, 2))
print("Ingresos totales:", round(ingresos_totales, 2))
print("ROI promedio:", round(roi_promedio, 2))


# ---------------
# Análisis
# ---------------

ctr_formato = df.groupby("formato")["ctr"].mean().sort_values(ascending=False)
roi_plataforma = df.groupby("plataforma")["roi"].mean().sort_values(ascending=False)

print("\nCTR promedio por formato:")
print(ctr_formato.to_string())

print("\nROI promedio por plataforma:")
print(roi_plataforma.to_string())


# -----------
# Outliers
# -----------

Q1 = df["ctr"].quantile(0.25)
Q3 = df["ctr"].quantile(0.75)
IQR = Q3 - Q1

lim_inf = Q1 - 1.5 * IQR
lim_sup = Q3 + 1.5 * IQR

outliers = df[(df["ctr"] < lim_inf) | (df["ctr"] > lim_sup)]

print("\nOutliers detectados en CTR:", len(outliers))


# -----------------
# Top y Bottom
# -----------------

top5 = df.sort_values("roi", ascending=False).head(5)
bottom5 = df.sort_values("roi", ascending=True).head(5)

print("\n--- TOP 5 CAMPAÑAS POR ROI ---")
print(top5[["id_campana", "plataforma", "formato", "roi"]].to_string(index=False))

print("\n--- BOTTOM 5 CAMPAÑAS POR ROI ---")
print(bottom5[["id_campana", "plataforma", "formato", "roi"]].to_string(index=False))


# -----------
# Gráficas
# -----------

plt.figure()
df.groupby("plataforma")["roi"].mean().plot(kind="bar")
plt.title("ROI promedio por plataforma")
plt.ylabel("ROI")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

plt.figure()
df.groupby("formato")["ctr"].mean().plot(kind="bar")
plt.title("CTR promedio por formato")
plt.ylabel("CTR")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()