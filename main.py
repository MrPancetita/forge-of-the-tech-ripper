import os
import json

# Obtener todos los archivos .json en un directorio dado
def obtener_archivos_json(directorio):
    return [archivo for archivo in os.listdir(directorio) if archivo.endswith('.json')]

# Especificar el directorio
directorio = './assets/json'
json_files = obtener_archivos_json(directorio)

# Recorrer cada archivo JSON
for archivo in json_files:
    archivo_path = os.path.join(directorio, archivo)
    with open(archivo_path, 'r', encoding='utf-8') as f:
        data = json.load(f)
        # Verificar si el contenido es una lista
        if isinstance(data, list):
            for item in data:
                nombre = item.get('name', 'No especificado')
                edad = item.get('age', 'No especificado')
                puntos_necesarios = item.get('needed_fp', 'No especificado')
                print(f"Archivo: {archivo}")
                print(f"Nombre: {nombre}")
                print(f"Edad: {edad}")
                print(f"Puntos Necesarios: {puntos_necesarios}")
                print('-' * 40)
        else:
            print(f"El archivo {archivo} no contiene una lista de objetos.")
