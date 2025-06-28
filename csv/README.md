# CSV Product Analyzer

Esta carpeta contiene un pequeño script para analizar un archivo CSV de productos. El script lee una columna de descripciones y extrae, mediante expresiones regulares, el color y el tamaño de cada producto.

## Requisitos

- Python 3.8+
- `pandas`

Instala las dependencias con:

```bash
pip install pandas
```

## Uso

1. Coloca tu archivo `productos.csv` (o el nombre que corresponda) en esta carpeta.
2. Ejecuta el script indicando la ruta del CSV:

```bash
python analyze.py productos.csv --salida productos_con_parametros.csv --columna descripcion
```

La columna de descripciones debe llamarse `descripcion` o el nombre que indiques mediante `--columna`.

El script generará un nuevo archivo con las columnas `color` y `tamano` agregadas.

## Interfaz Gráfica

Para quienes prefieran una herramienta visual, `analyze_gui.py` ofrece una pequeña interfaz basada en `tkinter`.

Ejecuta el script así:

```bash
python analyze_gui.py
```

Selecciona el archivo CSV de entrada, elige la ubicación del archivo de salida y la columna que contiene las descripciones. Al finalizar se mostrará un mensaje con la ruta del nuevo archivo.

### Crear un ejecutable

Si deseas generar un ejecutable sin depender de Python instalado, puedes usar `pyinstaller` (o herramienta similar):

```bash
pip install pyinstaller
pyinstaller --onefile analyze_gui.py
```

El ejecutable resultante estará en la carpeta `dist/`.
