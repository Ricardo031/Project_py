# Control Flow - Inventory Management

## Description
An interactive Python program for managing inventory using a menu. Demonstrates control flow with loops and conditionals, storing products in a list of dictionaries.

## Features
- **Add products (1)**: Input multiple products with name, price, quantity. Includes data validation.
- **View inventory (2)**: Display all products with individual totals. Shows empty message if no products.
- **Calculate statistics (3)**: Compute total inventory value (price × quantity sum) and total quantity.
- **Exit (0)**: Quit the program.

## How to Run
Ensure Python is installed. Run `python Control.py` and follow the on-screen menu.

## Usage
- Select options by entering the number.
- Add products by specifying count and details.
- Options 2 and 3 require products in inventory.
- Handles invalid inputs with error messages.

## Concepts Demonstrated
- **While loop**: Menu runs until exit.
- **For loops**: Iterate over product additions and inventory display.
- **Try/except**: Input validation for numbers.
- **Data structures**: List of dictionaries for products.

## Example
```
Add product (1), view inventory (2), calculate total (3) or exit (0): 1
Enter the number of products to add: 1
Enter the name of product 1: Pencil
Enter the price of product 1: 500
Enter the quantity of product 1: 3
Product added: Pencil, Price: 500.0, Quantity: 3
-----------------------------------------------
Add product (1), view inventory (2), calculate total (3) or exit (0): 2
Inventory products:
Product 1: Pencil | price: 500.0 | amount: 3 | total: 1500.0
-----------------------------------------------
Add product (1), view inventory (2), calculate total (3) or exit (0): 3
Inventory statistics:
- Total inventory value: 1500.0
- Total quantity of products: 3
-----------------------------------------------
Add product (1), view inventory (2), calculate total (3) or exit (0): 0
Exiting program.
```