# Movilidad urbana y productividad económica

Proyecto exploratorio para estudiar la relación entre la congestión del tráfico y algunos indicadores económicos de ciudades, con foco en Latinoamérica. Se utilizan datos de TomTom Traffic Index y OECD Cities. El análisis está en desarrollo y sus resultados son iniciales.

## Contenido

- `data/`: archivos fuente en formato CSV.
- `notebooks/mobility_economy_project_student.ipynb`: notebook con la guía y el análisis en curso.
- `src/`: scripts de Python de apoyo.
- `requirements.txt`: dependencias de Python.

## Preparar el entorno

Desde la carpeta del proyecto, instala las dependencias:

```bash
python -m pip install -r requirements.txt
```

Para abrir el notebook, inicia Jupyter desde esta carpeta:

```bash
jupyter notebook
```

Ejecuta sus celdas en orden. Los scripts de `src/` leen los CSV desde `data/`.

## Datos y alcance

Los datos de tráfico contienen mediciones repetidas por ciudad y fecha; los datos económicos contienen indicadores por ciudad y año. El notebook propone limpiar y estandarizar ambos conjuntos, resumir el tráfico por ciudad y año, y combinarlos para explorar sus relaciones. La guía se centra en 2024, sujeto a que ese año esté disponible en ambos archivos. La asociación observada no implica causalidad.

## Estado

Estructura y exploración inicial preparadas. La limpieza, integración, visualizaciones y resumen de resultados siguen en desarrollo.
