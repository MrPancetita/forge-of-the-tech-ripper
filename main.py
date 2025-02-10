import os
import json

# Obtener todos los archivos .json en un directorio dado
def obtener_archivos_json(directorio):
    return [archivo for archivo in os.listdir(directorio) if archivo.endswith('.json')]

class Tech:
    def __init__(self, nombre, edad, puntos_necesarios):
        self.nombre = nombre
        self.edad = edad
        self.puntos_necesarios = puntos_necesarios

    def __str__(self):
        return f"Nombre: {self.nombre}, Edad: {self.edad}, Puntos Necesarios: {self.puntos_necesarios}"

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
                tech = Tech(nombre, edad, puntos_necesarios)
                print(tech)
                print('-' * 40)
        else:
            print(f"El archivo {archivo} no contiene una lista de objetos.")
