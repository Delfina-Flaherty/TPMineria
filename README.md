# TP Integrador — Minería de Datos y Aprendizaje Automático (UNLP, 2026)

Análisis del dataset **MathE**: 9.546 respuestas de estudiantes a preguntas de matemática de nivel universitario.
Objetivo: predecir si una respuesta es correcta o incorrecta (`Type of Answer`).

## 👥 Integrantes y reparto de tareas

| Integrante | Tarea |
|---|---|
| Delfina Flaherty | _a definir_ |
| _Nombre_ | _a definir_ |
| _Nombre_ | _a definir_ |
| _Nombre_ | _a definir_ |

## 📋 Consignas

1. **EDA** del dataset y transformación de variables categóricas a numéricas.
2. **Clasificación**: dos técnicas, 5 configuraciones de hiperparámetros cada una, evaluadas con cross-validation. Promediar métricas y comparar.
3. **Stacking** con los 10 modelos del punto 2 como modelos débiles: 5 ejecuciones con CV, promediar y comparar con el punto 2.

Detalle completo en [`consignas.txt`](consignas.txt).

## 📁 Estructura

```
tp-mineria-mathe/
├── data/raw/            # Datos originales (no modificar)
│   ├── Datos.txt
│   └── descripcion.txt
├── data/processed/      # Datos ya preprocesados (se generan desde las notebooks)
├── notebooks/
│   ├── 01_EDA.ipynb
│   ├── 02_clasificacion.ipynb
│   └── 03_stacking.ipynb
├── src/                 # Funciones reutilizables
├── resultados/          # Tablas de métricas y gráficos exportados
├── informe/             # Informe final en PDF
├── requirements.txt
└── consignas.txt
```

## ⚙️ Cómo levantar el entorno

```bash
git clone https://github.com/Delfina-Flaherty/tp-mineria-mathe.git
cd tp-mineria-mathe

python -m venv .venv
# Windows:
.venv\Scripts\activate
# Mac / Linux:
source .venv/bin/activate

pip install -r requirements.txt
```

Después abrí la carpeta en VS Code (o ejecutá `jupyter notebook`) y elegí el kernel `.venv`.

## 🔁 Cómo trabajar en grupo

- Antes de empezar: `git pull`
- Cada uno trabaja **en su propia notebook** para evitar conflictos (los conflictos en `.ipynb` son difíciles de resolver).
- Al terminar: `git add .` → `git commit -m "mensaje claro"` → `git push`
- Si agregás una librería nueva, sumala a `requirements.txt`.

## 📅 Fechas

- Coloquio: desde el 13/11
- Fecha límite: 11/12 o 14/12
