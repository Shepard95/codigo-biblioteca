import requests
from models.libro import Libro

# Deserializacion de un JSON a una instancia
libros = requests.get("https://poo.nsideas.cl/api/libros")
for libro in libros.json():
        print(f"Libro: {libro["titulo"]},Autor: {libro["autor"]},ISBN {libro["isbn"]}, Categorias: {libro["categorias"]}, Descripcion: {libro["descripcion"]}, Numero_paginas: {libro["numero_paginas"]}")
response = requests.get("https://poo.nsideas.cl/api/libros{isbn}")
if response.status_code == 200:
    data = response.text
    libro2 = Libro.from_json(data)
    print(f"Libro: {libro2.titulo} | Autor: {libro2.autor}")