#utilizar la extension better comments para que puedan ver mejor los comentarios que coloque en el codigo
#* 2. Estructura de datos y modularización
def add_product(inventory, name, price, quantity):
    """
    Agrega un nuevo producto al inventario.
    #?Args:
        inventory (dict): El diccionario del inventario.
        name (str): El nombre del producto.
        price (float): El precio del producto.
        quantity (int): La cantidad disponible.
    """
    if name in inventory:
        # Informar que el producto ya existe
        print(f"The product '{name}' already exists. Use update_product to modify it.")
    else:
        # Agregar nuevo producto al diccionario
        inventory[name] = {'price': price, 'quantity': quantity}
        print(f"Product '{name}' added successfully.")
        
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
            print(f"Name: {name} Price: {details['price']} Quantity: {details['quantity']}")

def search_product(inventory, name):
    """
    Busca un producto por su nombre y muestra su información.

    #?Args:
        inventory (dict): El diccionario del inventario.
        name (str): El nombre del producto a buscar.
    """
    if name in inventory:
        # Mostrar detalles del producto encontrado
        print(f"Product {name} found. Price: {inventory[name]['price']:.2f}")
        print(f"Quantity: {inventory[name]['quantity']}")
    else:
        # Informar si no se encontró
        print(f"Product {name} not found.")
        return None

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
            print(f"Price of {name} updated to {new_price:.2f}")
        # Actualizar cantidad si se proporciona
        if new_quantity is not None:
            inventory[name]['quantity'] = new_quantity
            print(f"Quantity of {name} updated to {new_quantity}")
    else:
        # Producto no encontrado
        print(f"Product {name} not found.")

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
        print(f"Product {name} deleted successfully.")
    else:
        # Producto no encontrado
        print(f"Product {name} not found.")

def calculate_total(inventory): #return tupla/dict 
    """
    Calcula el valor total del inventario y la cantidad total de productos.
    #?Args:
        inventory (dict): El diccionario del inventario.
    #?Returns:
        tuple: Una tupla con (precio_total, cantidad_total).
    """
    total_price = 0
    total_quantity = 0
    # Iterar sobre todos los productos para sumar valores
    for name, details in inventory.items():
        total_price += details['price'] * details['quantity']
        total_quantity += details['quantity']
    # Retornar los totales acumulados
    return (total_price, total_quantity)

#todo: seguir con las demas funciones faltantes