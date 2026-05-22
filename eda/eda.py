import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


def resumen_general(df):
    print("📌 Dimensiones del dataset:")
    print(f"Filas: {df.shape[0]}, Columnas: {df.shape[1]}\n")

    print("📌 Primeras filas:")
    print(df.head())

    print("\n📌 Tipos de datos:")
    print(df.dtypes)

    print("\n📌 Valores nulos por columna:")
    print(df.isnull().sum())


def estadisticos(df):
    print("📌 Estadísticos descriptivos:")
    print(df.describe(include="all"))


def distribuciones(df):
    num_cols = df.select_dtypes(include=np.number).columns

    for col in num_cols:
        plt.figure(figsize=(8, 4))
        sns.histplot(df[col], kde=True, color="steelblue")
        plt.title(f"Distribución de {col}")
        plt.tight_layout()
        plt.show()


def boxplots(df):
    num_cols = df.select_dtypes(include=np.number).columns

    for col in num_cols:
        plt.figure(figsize=(6, 4))
        sns.boxplot(x=df[col], color="orange")
        plt.title(f"Boxplot de {col}")
        plt.tight_layout()
        plt.show()


def correlaciones(df):
    num_cols = df.select_dtypes(include=np.number)

    plt.figure(figsize=(10, 8))
    sns.heatmap(num_cols.corr(), annot=True, cmap="coolwarm", fmt=".2f")
    plt.title("Matriz de correlación")
    plt.tight_layout()
    plt.show()


def detectar_outliers(df, metodo="IQR"):
    outliers = {}

    for col in df.select_dtypes(include=np.number).columns:
        q1 = df[col].quantile(0.25)
        q3 = df[col].quantile(0.75)
        iqr = q3 - q1

        limite_inf = q1 - 1.5 * iqr
        limite_sup = q3 + 1.5 * iqr

        outliers[col] = df[(df[col] < limite_inf) | (df[col] > limite_sup)][col]

    return outliers


def reporte_eda(df):
    print("========== 🧠 REPORTE COMPLETO DE EDA 🧠 ==========\n")

    resumen_general(df)
    estadisticos(df)

    print("\n========== 📊 DISTRIBUCIONES ==========\n")
    distribuciones(df)

    print("\n========== 📦 BOXPLOTS ==========\n")
    boxplots(df)

    print("\n========== 🔥 CORRELACIONES ==========\n")
    correlaciones(df)

    print("\n========== 🚨 OUTLIERS DETECTADOS ==========\n")
    outliers = detectar_outliers(df)
    for col, vals in outliers.items():
        print(f"{col}: {len(vals)} outliers")

    print("\n========== ✔️ FIN DEL REPORTE ==========\n")
