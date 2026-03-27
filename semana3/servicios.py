#utilizar la extension better comments para que puedan ver mejor los comentarios que coloque en el codigo
import csv
from datetime import datetime
#* 4. Guardar CSV(persistencia de salida)
def save_csv(inventory, filename="store.csv", header=True):
    with open(filename, "a", newline="", encoding="utf-8" ) as f:
        try:
            if header:
                f.write("Name,Price,Quantity\n")
                for name, details in inventory.items():
                    writer = csv.writer(f)
                    writer.writerow([
                        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                    ])
                    writer.writerow([
                        name.capitalize(),
                        details['price'],
                        details['quantity']
                        ])
        except Exception as e:
            print(f"Error saving to CSV: {e}")
        print(f"Inventory saved to {filename}")
    print("-----------------------------------------------")



#* 2. Estructura de datos y modularización
#? agregar producto
def add_product(inventory, name, price, quantity):
    """
    Agrega un nuevo producto al inventario.
    #?Args:
        inventory (dict): Agregar el producto al inventario.
        name (str): El nombre del producto.
        price (float): El precio del producto.
        quantity (int): La cantidad disponible.
    """
    if name in inventory:
        # Informar que el producto ya existe
        print(f"The product '{name}' already exists. Use update_product to modify it.")
    else:
        # Agregar nuevo producto al diccionario
        product = {
            "price": price,
            "quantity": quantity,
        } 
        inventory[name] = product
    print(f"Product '{name}' added successfully.")
    print("-----------------------------------------------")


#? mostrar inventario
def show_invetory(inventory):
    """
    Muestra todos los productos en el inventario.
    #?Args:
        inventory (dict): El diccionario del inventario.
    """
    if not inventory:
        # Caso inventario vacío
        print("The inventory is empty.")
    else:
        # Recorrer y mostrar cada producto
        print("Current Intentory:")
        for name, details in inventory.items():
            total = details['price'] * details['quantity']
            print(f"Name: '{name}' Price: {details['price']:.2f} | Quantity: {details['quantity']} | Total: {total:.2f}")
        print("-----------------------------------------------")

#? buscar producto
def search_product(inventory, name):
    """
    Busca un producto por su nombre y muestra su información.
    Si no se encuentra, pregunta nuevamente hasta que el usuario decida salir.

    #?Args:
        inventory (dict): El diccionario del inventario.
        name (str): El nombre del producto a buscar inicialmente.
    """    
    current_name = name
    while True:
        if current_name in inventory:
            # Producto encontrado: mostrar detalles y salir de la función
            print(f"\nProduct '{current_name}' found.")
            print(f"Name: '{current_name}' | Price: {inventory[current_name]['price']:.2f} | Quantity: {inventory[current_name]['quantity']}")
            return f"Success. if you want to continue searching, press '3'."
        # Producto no encontrado o nombre vacío
        if current_name == "":
            print("\nInvalid input. Please enter a valid product name.")
        else:
            print(f"\nProduct '{current_name}' not found or does not exist.")
        
        # Preguntar si desea intentar con otro nombre o salir
        leave = input("Do you want to try searching for another product? (Enter new name or 'exit' to cancel): ").strip()
        
        if leave.lower() == "exit":
            return f"Search for '{current_name}' completed."
        
        
        # Actualizar el nombre para la siguiente iteración
        current_name = leave

#? actualizar producto
def update_product(inventory, name, new_price=None, new_quantity=None):
    """
    Actualiza el precio o la cantidad de un producto existente.
    #?Args:
        inventory (dict): El diccionario del inventario.
        name (str): El nombre del producto a actualizar.
        new_price (float, optional): El nuevo precio. Por defecto es None.
        new_quantity (int, optional): La nueva cantidad. Por defecto es None.
    """
    if name in inventory:
        
        # Actualizar precio si se proporciona
        if new_price is not None:
            inventory[name]['price'] = new_price
            print(f"Price of '{name}' updated to {new_price:.2f}")
        # Actualizar cantidad si se proporciona
        if new_quantity is not None:
            inventory[name]['quantity'] = new_quantity
            print(f"Quantity of '{name}' updated to {new_quantity}")
    else:
        # Producto no encontrado
        print(f"Product '{name}' not found or does not exist.")

#? eliminar producto
def delete_product(inventory, name): 
    """
    Elimina un producto del inventario.
    #?Args:
        inventory (dict): El diccionario del inventario.
        name (str): El nombre del producto a eliminar.
    """
    if name in inventory:
        # Eliminar entrada del diccionario
        del inventory[name]
        print(f"Product '{name}' deleted successfully.")
    else:
        # Producto no encontrado
        print(f"Product '{name}' not found or does not exist.")

#? calcular estadísticas
def calculate_statistics(inventory): #return tupla/dict 
    """
    Calcula el valor total del inventario y la cantidad total de productos.
    #?Args:
        inventory (dict): El diccionario del inventario.
    #?Returns:
        tuple: Una tupla con (precio_total, cantidad_total).
    """
    total_price = 0
    total_quantity = 0
    product_most_exp_name = ""
    product_most_exp_price = 0
    product_most_exp_quantity = 0
#* 3.Estadísticas del inventario
    if not inventory:
        # Caso inventario vacío
        return "The inventory is empty."
    # Iterar sobre todos los productos para sumar valores
    for name, details in inventory.items():
        if details['price'] > product_most_exp_price:
            product_most_exp_price = details['price']
            product_most_exp_name = name
            product_most_exp_quantity = details['quantity']
        total_price += details['price'] * details['quantity']
        total_quantity += details['quantity']
    print(f"total price: {total_price:.2f}")
    print(f"total quantity: {total_quantity}")
    print(f"product most expensive price is {product_most_exp_name}: {product_most_exp_price:.2f}")
    print(f"product most expensive quantity is {product_most_exp_name}: {product_most_exp_quantity}")

#todo: seguir con las demas funciones faltantes