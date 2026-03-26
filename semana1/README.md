# README
## Fundamentos de Python - Semana 1
- Declara variables para nombre (string), precio (float) y cantidad (int).
- Solicita al usuario estos datos con la función input().
- Asegúrate de que el precio y la cantidad se conviertan correctamente a sus tipos numéricos usando float() e int().
- Si el usuario ingresa un valor inválido, muestra un mensaje y vuelve a pedirlo.

## Code solution

```python
#? Entrada de nombre(solicita datos del producto)
name = input("Enter the name of product: " )

while True:
    try:
        #?Entrada de precio
        price = float(input("Enter the price of product: "))
        break
    except ValueError: #si hay un error pedira que repita
        print("Please inter a valid number of price")

while True:
    #? Entrada de cantidad
    try:
        quantity = int(input("ENter yout quantity: "))
        break
    except ValueError: #si hay un error pedira que repita
        print("Please Enter a valid number for quantity")

# calculo de total
total_cost = price * quantity

#? mostrar resultado
print(f"Product: {name} | price:{price} | quantity: {quantity} | total: {total_cost}")
```
## explication
This program is used to store and to calculate the total price of a product that a user enters. 
it has your validations for price and quantity, and messages to display the result