"""
Guardar y cargar el inventario desde archivos CSV para conservar los datos entre sesiones, compartirlos y consultar estadísticas del negocio.
Aplicar listas, diccionarios y tuplas junto con módulos y funciones en Python para construir un inventario modular y persistente: operaciones CRUD, estadísticas y lectura/escritura de archivos CSV con validaciones y manejo de errores.
"""
import csv 
import servicios

# Inicialización del inventario como un diccionario vacío
inventory = {}
option = None

# Bucle principal del programa
while option != 0:
    try:
        # Solicitar opción al usuario
        option = int(input("Add product (1), view inventory (2), search product (3), Update product (4), delete (5), calculate statistics (6) or exit (0):"))
    except ValueError:
        # Manejo de error para entradas no numéricas
        print("Invalid input. Please enter a valid integer.")
        continue
