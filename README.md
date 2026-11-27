# TP Integrador — Minería de Datos y Aprendizaje Automático (UNLP, 2026)

Análisis del dataset **MathE**: 9.546 respuestas de estudiantes a preguntas de matemática de nivel universitario.
Objetivo: predecir si una respuesta es correcta o incorrecta (`Type of Answer`).

## Integrantes

- Erbity Joaquín – 17992/7
- Flaherty Delfina – 18018/1
- Vignau Pedro – 18420/7

## Consignas

1. **EDA** del dataset y transformación de variables categóricas a numéricas.
2. **Clasificación**: dos técnicas, 5 configuraciones de hiperparámetros cada una, evaluadas con cross-validation. Promediar métricas y comparar.
3. **Stacking** con los 10 modelos del punto 2 como modelos débiles: 5 ejecuciones con CV, promediar y comparar con el punto 2.

Detalle completo en [`consignas.txt`](consignas.txt).

## Estructura

```
TPMineria/
├── data/raw/            # Datos originales (no modificar)
│   ├── Datos.txt
│   └── descripcion.txt
├── data/processed/      # Datos preprocesados (los genera el notebook 01)
├── notebooks/
│   ├── 01_EDA.ipynb             # Tarea 1: EDA, variable Est_Topic_Level y transformación de variables
│   ├── 02_clasificacion.ipynb   # Tarea 2: árbol y regresión logística + importancia de variables
│   └── 03_stacking.ipynb        # Tarea 3: Stacking y comparación con la Tarea 2
├── src/                 # Funciones reutilizables
├── resultados/          # Métricas de cada tarea en CSV
├── requirements.txt
└── consignas.txt
```

## Cómo levantar el entorno

```bash
git clone https://github.com/Delfina-Flaherty/TPMineria.git
cd TPMineria

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac / Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

Después abrí la carpeta en VS Code (o ejecutá `jupyter notebook`) y elegí el kernel `.venv`.

## Cómo reproducir los resultados

1. Se requiere **scikit-learn 1.8 o superior** (se usó la 1.9.1).
2. Ejecutar los notebooks **en orden: 01, 02 y 03**. Cada uno usa los archivos que genera el anterior: el 01 crea los datos procesados y el 02 guarda los resultados que lee el 03.

Todas las semillas están fijadas (42), así que los resultados son reproducibles. En otra computadora pueden aparecer diferencias de ±0,001 en valores que caen justo en el límite del redondeo.