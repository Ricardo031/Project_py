"""
Guardar y cargar el inventario desde archivos CSV para conservar los datos entre sesiones, compartirlos y consultar estadísticas del negocio.
Aplicar listas, diccionarios y tuplas junto con módulos y funciones en Python para construir un inventario modular y persistente: operaciones CRUD, estadísticas y lectura/escritura de archivos CSV con validaciones y manejo de errores.
"""
import servicios
import csv 
# Inicialización del inventario como un diccionario vacío
inventory = {}
option = None

# Bucle principal del programa
while option != 0:
    try:
        # Solicitar opción al usuario
        option = int(input("Add product (1), view inventory (2), search product (3), Update product (4), delete (5), calculate statistics (6) or exit (0):"))
        if option == 0:
            break
        elif option == 1:
            count = int(input("Enter the quantity of the product do you want to add: "))
            if count <= 0:
                print("Invalid quantity. Please enter a positive integer.")
                continue
            for i in range(count):
                name = input(f"Enter product name {i+1}: ").strip()
                try:
                    price = float(input(f"Enter product price {i+1}: "))
                except ValueError:
                    print("Invalid price. Please enter a valid number.")
                    continue
                if price <= 0:
                    print("Invalid price. Please enter a positive number.")
                    continue
                quantity = int(input(f"Enter product quantity {i+1}: "))
                if quantity <= 0:
                    print("Invalid quantity. Please enter a positive integer.")
                    continue
                else:
                    servicios.add_product(inventory, name, price, quantity)

        elif option == 2:
                servicios.show_invetory(inventory)
        
        elif option == 3:
            if not inventory:
                print(f"there is not any product in the inventory.")
                continue    
            name = input("Enter product name: ").strip()
            result = servicios.search_product(inventory, name)
            print(result)
        
        elif option == 4:
            name = input("Enter product name: ").strip()
            if name in inventory: 
                print(f"Product '{name}' found.")
                try:
                    new_price = float(input("Enter new price: "))
                except ValueError:
                    print("Invalid price. Please enter a valid number.")
                    continue
                if new_price <= 0:
                    print("Invalid price. Please enter a positive number.")
                    continue
                try:
                    new_quantity = int(input("Enter new quantity: "))
                except ValueError:
                    print("Invalid quantity. Please enter a valid number.")
                    continue
                if new_quantity <= 0:
                    print("Invalid quantity. Please enter a positive integer.")
                    continue
            else:
                print(f"Product '{name}' not found or does not exist.")
                continue
            servicios.update_product(inventory, name, new_price, new_quantity)
        
        elif option == 5:
            name = input("Enter product name: ").strip()
            servicios.delete_product(inventory, name)

        elif option == 6:
            statistics = servicios.calculate_statistics(inventory)
            print(statistics)

    except ValueError:
        # Manejo de error para entradas no numéricas
        print("Invalid input. Please enter a valid integer.")
        continue
    
    servicios.save_csv(inventory)
