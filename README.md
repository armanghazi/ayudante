# Ayudante

[![Python](https://img.shields.io/badge/python-3.8%2B-blue)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)

**Ayudante** es un paquete en Python diseñado para agilizar el flujo de trabajo en proyectos de Machine Learning y análisis predictivo. Proporciona herramientas integradas para:

- Análisis exploratorio de datos (EDA)
- Visualización de correlaciones
- Diagnóstico de modelos de regresión
- Evaluación automática de modelos

---

## Instalación

```bash
pip install git+https://github.com/armanghazi/ayudante.git
```

Para desarrollo local:

```bash
git clone https://github.com/armanghazi/ayudante.git
cd ayudante
pip install -e .
```

---

## Estructura del paquete

```
ayudante/
├── eda/                  # Análisis exploratorio de datos
│   └── eda.py
├── ml/                   # Evaluación de modelos
│   └── regresion.py
├── visualizaciones/      # Gráficos y visualizaciones
│   ├── correlacion.py
│   └── regresiones.py
├── setup.py
└── README.md
```

---

## Uso rápido

```python
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

from eda import eda
from ml.regresion import evaluar_modelo
from visualizaciones.correlacion import heatmap_corr
from visualizaciones.regresiones import par_real_predicho, par_real_predicho_res

# Cargar datos
df = pd.read_csv("data/hormigon.csv")

# ─────────────────────────────────────────────
# 1. Análisis exploratorio de datos
# ─────────────────────────────────────────────
eda.resumen_general(df)          # Dimensiones, tipos, nulos
eda.estadisticos(df)             # Estadísticas descriptivas
eda.distribuciones(df)           # Histogramas + KDE
eda.boxplots(df)                 # Diagramas de caja
eda.correlaciones(df)            # Mapa de calor de correlaciones
outliers = eda.detectar_outliers(df)
# ó todo en uno:
eda.reporte_eda(df)

# ─────────────────────────────────────────────
# 2. Entrenar modelo
# ─────────────────────────────────────────────
X = df.drop("strength", axis=1)
y = df["strength"]
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
modelo = LinearRegression().fit(X_train, y_train)
y_pred = modelo.predict(X_test)

# ─────────────────────────────────────────────
# 3. Evaluación del modelo
# ─────────────────────────────────────────────
metricas = evaluar_modelo(modelo, X_test, y_test, magnitud="resistencia")

# ─────────────────────────────────────────────
# 4. Gráficos de diagnóstico
# ─────────────────────────────────────────────
par_real_predicho(y_test, y_pred, magnitud="resistencia")
res_metrics = par_real_predicho_res(y_test, y_pred, magnitud="resistencia")
```

---

## Módulos

### `eda.eda`

| Función | Descripción |
|---|---|
| `resumen_general(df)` | Muestra dimensiones, primeras filas, tipos de dato y valores nulos |
| `estadisticos(df)` | Estadísticas descriptivas (`df.describe(include="all")`) |
| `distribuciones(df)` | Histogramas con KDE para todas las columnas numéricas |
| `boxplots(df)` | Diagramas de caja para todas las columnas numéricas |
| `correlaciones(df)` | Mapa de calor de la matriz de correlación |
| `detectar_outliers(df, metodo="IQR")` | Detecta outliers usando el método IQR |
| `reporte_eda(df)` | Ejecuta todas las funciones anteriores secuencialmente |

### `ml.regresion`

| Función | Descripción |
|---|---|
| `evaluar_modelo(modelo, X_test, y_test, magnitud="")` | Evalúa un modelo de regresión y devuelve MAE, RMSE, R², media y desviación de residuos |

### `visualizaciones.correlacion`

| Función | Descripción |
|---|---|
| `heatmap_corr(df)` | Mapa de calor de correlaciones con máscara triangular superior y paleta divergente |

### `visualizaciones.regresiones`

| Función | Descripción |
|---|---|
| `par_real_predicho(y_test, y_pred, magnitud="")` | Gráfico de valores reales vs. predichos con bisectriz y distribuciones marginales |
| `par_real_predicho_res(y_test, y_pred, magnitud="", mostrar_normal=True)` | Gráfico de diagnóstico de residuos con tendencia y KDE |

---

## Dataset de ejemplo

El paquete incluye el dataset **Concrete Compressive Strength** (`data/hormigon.csv`) con 1030 registros y 9 columnas:

| Columna | Descripción |
|---|---|
| `cement` | Cemento (kg/m³) |
| `slag` | Escoria de alto horno (kg/m³) |
| `ash` | Ceniza volante (kg/m³) |
| `water` | Agua (kg/m³) |
| `superplastic` | Superplastificante (kg/m³) |
| `coarseagg` | Árido grueso (kg/m³) |
| `fineagg` | Árido fino (kg/m³) |
| `age` | Edad (días) |
| `strength` | Resistencia a compresión (MPa) — **variable objetivo** |

---

## Dependencias

- numpy
- pandas
- matplotlib
- seaborn
- scipy
- scikit-learn

---

## Autor

**Arman Ghaziaskari**  
[GitHub](https://github.com/armanghazi/ayudante)
