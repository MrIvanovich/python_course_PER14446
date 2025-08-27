

# Curso Python PER14446

Este repositorio contiene los ejercicios y ejemplos del curso previo de Python (UNIR).

## Requisitos

- Python 3.11 (o versión compatible)
- Entorno virtual recomendado (`.venv`)

## Configuración del entorno

Crear y activar el entorno virtual:

```bash
python3 -m venv .venv
source .venv/bin/activate   # macOS/Linux
.venv\Scripts\activate      # Windows
```

Instalar dependencias desde `requirements.txt`:

```bash
pip install -r requirements.txt
```

## Dependencias

El archivo `requirements.txt` contiene las librerías externas necesarias para ejecutar los ejercicios.  
Para actualizarlo después de instalar nuevos paquetes:

```bash
pip freeze > requirements.txt
```

## Estructura del proyecto

- `.venv/` → entorno virtual (ignorado en git)
- `ejercicios/` → scripts y prácticas del curso
- `README.md` → documentación del proyecto
- `requirements.txt` → dependencias instaladas
- `.gitignore` → reglas para ignorar archivos no deseados