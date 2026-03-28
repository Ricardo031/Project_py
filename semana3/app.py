"""
Guardar y cargar el inventario desde archivos CSV para conservar los datos entre sesiones, compartirlos y consultar estadísticas del negocio.
Aplicar listas, diccionarios y tuplas junto con módulos y funciones en Python para construir un inventario modular y persistente: operaciones CRUD, estadísticas y lectura/escritura de archivos CSV con validaciones y manejo de errores.
"""
import servicios
import archivos
# Inicialización del inventario como un diccionario vacío
inventory = {}
option = None

# Bucle principal del programa
while option != 0:
    try:
        # Solicitar opción al usuario
        print("\033[32mWelcome to the inventory management system.\033[0m")
        print("-----------------------------------")
        print("Add product (1) \nview inventory (2) \nsearch product (3) \nUpdate product (4) \ndelete (5) \ncalculate statistics (6) \nLoad CSV (7) \nexit (0)")
        option = int(input("Enter your option:"))
        if option == 0:
            break
        elif option == 1:
            count = int(input("Enter the quantity of the product do you want to add: "))
            if count <= 0:
                print("\033[1;31mInvalid quantity. Please enter a positive integer.\033[0m")
                continue
            for i in range(count):
                name = input(f"Enter product name {i+1}: ").strip()
                try:
                    price = float(input(f"Enter product price {i+1}: "))
                except ValueError:
                    print("\033[1;31mInvalid price. Please enter a valid number.\033[0m")
                    continue
                if price <= 0:
                    print("\033[1;31mInvalid price. Please enter a positive number.\033[0m")
                    continue
                quantity = int(input(f"Enter product quantity {i+1}: "))
                if quantity <= 0:
                    print("\033[1;31mInvalid quantity. Please enter a positive integer.\033[0m")
                    continue
                else:
                    servicios.add_product(inventory, name, price, quantity)

        elif option == 2:
                servicios.show_invetory(inventory)
        
        elif option == 3:
            if not inventory:
                print("\033[1;31mthere is not any product in the inventory.\033[0m")
                continue    
            name = input("Enter product name: ").strip()
            result = servicios.search_product(inventory, name)
            print(result)
        
        elif option == 4:
            if not inventory:
                print("\033[1;31mthere is not any product in the inventory.\033[0m")
                continue
            name = input("Enter product name: ").strip()
            if name in inventory: 
                print(f"Product '{name}' found.")
                try:
                    new_price = float(input("Enter new price: "))
                except ValueError:
                    print("\033[1;31mInvalid price. Please enter a valid number.\033[0m")
                    continue
                if new_price <= 0:
                    print("\033[1;31mInvalid price. Please enter a positive number.\033[0m")
                    continue
                try:
                    new_quantity = int(input("Enter new quantity: "))
                except ValueError:
                    print("\033[1;31mInvalid quantity. Please enter a valid number.\033[0m")
                    continue
                if new_quantity <= 0:
                    print("\033[1;31mInvalid quantity. Please enter a positive integer.\033[0m")
                    continue
            else:
                print(f"\033[1;31mProduct '{name}' not found or does not exist.\033[0m")
                continue
            servicios.update_product(inventory, name, new_price, new_quantity)
        
        elif option == 5:
            if not inventory:
                print("\033[1;31mthere is not any product in the inventory.\033[0m")
                continue
            name = input("Enter product name: ").strip()
            if name == "":
                print("\nInvalid input. Please enter a valid product name.")
                continue
            elif name not in inventory:
                print(f"\033[1;31mProduct '{name}' not found or does not exist.\033[0m")
                continue
            elif name in inventory:
                print(f"Product '{name}' found.")
                servicios.delete_product(inventory, name)

        elif option == 6:
            print("\033[1;32mStatistics:\033[0m")
            statistics = servicios.calculate_statistics(inventory)

        elif option == 7:
            path = input("Enter the path of the CSV file: ").strip()
            loaded_products, error_count = archivos.load_csv(path)
            
            if loaded_products is not None:
                print(f"\n{len(loaded_products)} products found in file.")
                if error_count > 0:
                    print(f"{error_count} invalid rows skipped.")
                
                overwrite = input("Replace current inventory? (S/N): ").strip().upper()
                action_taken = ""
                
                if overwrite == 'S':
                    inventory.clear()
                    servicios.merge_inventory(inventory, loaded_products)
                    action_taken = "Replacement"
                elif overwrite == 'N':
                    servicios.merge_inventory(inventory, loaded_products)
                    action_taken = "Merge"
                
                print(f"\n--- Load Summary ---")
                print(f"Products loaded: {len(loaded_products)}")
                print(f"Invalid rows: {error_count}")
                print(f"Action taken: {action_taken}")
                print(f"--------------------\n")
                
                # Refresh output
                print("\033[2J\033[H", end="")  # Clear screen
                print("\033[1;32mInventory updated successfully.\033[0m")
                servicios.show_invetory(inventory)
        else:
            print("\033[1;31mInvalid option. Please enter a valid option between 0 and 7.\033[0m")

    except ValueError:
        # Manejo de error para entradas no numéricas
        print("\033[1;31mInvalid input. Please enter a valid integer.\033[0m")
        continue
    

    archivos.save_csv(inventory)
