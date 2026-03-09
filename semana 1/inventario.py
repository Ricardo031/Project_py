"""
-Declara variables para nombre (string), precio (float) y cantidad (int).
-Solicita al usuario estos datos con la función input().
-Asegúrate de que el precio y la cantidad se conviertan correctamente a sus tipos numéricos usando float() e int().
-Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.
"""
name = input("Enter the name of product: " )

while True:
    try:
        price = float(input("Enter the price of product: "))
        break
    except ValueError:
        print("Please inter a valid number of price")

while True:
    try:
        quantity = int(input("ENter yout quantity: "))
        break
    except ValueError:
        print("Please Enter a valid number for quantity")

total_cost = price * quantity

print(name)
print(price)
print(quantity)
print(f"total cost: {total_cost}")
print("Welcome")