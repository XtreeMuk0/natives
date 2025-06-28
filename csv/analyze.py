import pandas as pd
import re
import argparse

PARAM_COLORS = [
    'rojo', 'azul', 'verde', 'negro', 'blanco',
    'amarillo', 'gris', 'marron', 'naranja', 'rosa'
]

SIZE_PATTERN = re.compile(r'(\d+(?:x\d+)*\s*(?:cm|mm|m))', re.I)
COLOR_PATTERN = re.compile(r'(' + '|'.join(PARAM_COLORS) + r')', re.I)


def extraer_parametros(descripcion):
    """Extrae color y tamaño de la descripcion del producto."""
    if not isinstance(descripcion, str):
        return None, None
    color_match = COLOR_PATTERN.search(descripcion)
    size_match = SIZE_PATTERN.search(descripcion)
    color = color_match.group(1).lower() if color_match else None
    size = size_match.group(1) if size_match else None
    return color, size


def procesar_csv(ruta_entrada, ruta_salida, columna_desc='descripcion'):
    """Procesa el CSV de productos y guarda uno nuevo con parametros."""
    df = pd.read_csv(ruta_entrada)
    if columna_desc not in df.columns:
        raise ValueError(f"La columna '{columna_desc}' no existe en el CSV")
    df[['color', 'tamano']] = df[columna_desc].apply(
        lambda desc: pd.Series(extraer_parametros(desc))
    )
    df.to_csv(ruta_salida, index=False)
    print(f"Archivo guardado en {ruta_salida}")


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Extrae parametros de productos desde un CSV')
    parser.add_argument('entrada', help='Ruta del CSV de entrada')
    parser.add_argument('--salida', default='productos_con_parametros.csv', help='Ruta del CSV resultante')
    parser.add_argument('--columna', default='descripcion', help='Nombre de la columna con descripciones')
    args = parser.parse_args()
    procesar_csv(args.entrada, args.salida, args.columna)
