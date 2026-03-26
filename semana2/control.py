"""
Gestionar varios productos en el inventario mediante un menú interactivo.
Organizar registros, validar datos y obtener estadísticas básicas de forma sencilla.
Aplicar estructuras condicionales (if/elif/else) y bucles (while y for) en Python, utilizando listas y diccionarios para almacenar productos, validar entradas y calcular estadísticas del inventario.
"""


def get_int(message):
    while True:
        try:
            value = int(input(message))
            return value
        except ValueError:
            print("Invalid input. Please enter a valid integer.")


def get_float(message):
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Invalid input. Please enter a valid float.")


def add_products(inventory):
    count = get_int("Enter the number of products to add: ")
    if count <= 0:
        print("Please enter a number greater than zero.")
        return

    for i in range(count):
        name = input(f"Enter name of product {i + 1}: ").strip()

        price = get_float(f"Enter price of product {i + 1}: ")
        quantity = get_int(f"Enter quantity of product {i + 1}: ")
        if quantity <= 0:
            print("Please enter a quantity greater than zero.")
            continue
        # cuando ya se realizan las validaciones ahora pasamos al sigueinte paso de crear el producto y agregarlo al inventario

        product = {
            "name": name,
            "price": price,
            "amount": quantity,
        }  # aqui creamos un diccionario para cada producto con sus atributos
        inventory.append(
            product
        )  # y con este append lo agregamos a la lista de inventario

        print(f"Product added: {name}, Price: {price}, Quantity: {quantity}")
        print("-----------------------------------------------")

    print("All products were added successfully.")
    print("-----------------------------------------------")


# * 3.Mostrar todos los productos del inventario.
def show_inventory(inventory):
    if not inventory:
        print("The inventory is empty.")
        return

    print("Inventory products:")
    for i, product in enumerate(
        inventory, start=1
    ):  # aqui solo usamos un for con un enumerate para mostrar cada producto con su name, price y amount
        total = product["price"] * product["amount"]
        print(
            f"Product {i}: {product['name']} | price: {product['price']} | quantity: {product['amount']} | total: {total}"
        )
    print("-----------------------------------------------")


# * 4.Calcular estadísticas básicas.
def calculate_statistics(inventory):
    if not inventory:
        print("The inventory is empty. No statistics available.")
        return

    total_value = sum(
        p["price"] * p["amount"] for p in inventory
    )  # usamos una comprensión de listas para calcular el valor total del inventario multiplicando el precio por la cantidad de cada producto y sumando esos valores
    total_quantity = sum(
        p["amount"] for p in inventory
    )  # aqui igual pero para la cantidad total de productos sumando la cantidad de cada producto en el inventario

    print("Inventory statistics:")
    print(f"- Total inventory value: {total_value}")
    print(f"- Total quantity of products: {total_quantity}")
    print("-----------------------------------------------")


def main():
    inventory = []
    # * 1.Validación de datos con condicionales.
    while True:
        # este es un bucle que se ejecuta hasta que el usuario elija salir
        try:
            option = get_int(
                "Add product (1), view inventory (2), calculate statistics (3) or exit (0): "
            )
            if option == 1:
                add_products(inventory)
            elif option == 2:
                show_inventory(inventory)
            elif option == 3:
                calculate_statistics(inventory)
            elif option == 0:
                print("Exiting program.")
                break
            else:
                print("Please choose a valid option (0, 1, 2, or 3).")

        except ValueError:
            print("Invalid option, try again.")


main()
# * 5 Documentación y limpieza del código.
# este programa permite al usuario agregar productos a un inventario, ver los productos almacenados y calcular estadísticas básicas como el valor total del inventario y la cantidad total de productos. El programa utiliza validación de datos para asegurar que las entradas sean correctas y maneja múltiples registros utilizando listas y diccionarios.
