# Inventory Management System

## Overview
This project is a modular inventory management system built with Python. It allows users to manage products, perform CRUD operations, calculate statistics, and persist data using CSV files.

The system is divided into three main modules:
- `app.py`: Main program and user interaction (menu system)
- `servicios.py`: Business logic (inventory operations)
- `archivos.py`: File handling (CSV load/save)

---

## Features

### 1. Product Management (CRUD)
- Add new products
- View all products
- Search for a product
- Update product price and quantity
- Delete products

### 2. Inventory Operations
- Merge inventories from external sources
- Validate inputs (price, quantity, names)
- Handle empty inventory cases

### 3. Statistics
- Total inventory value
- Total quantity of products
- Most expensive product

### 4. Data Persistence
- Load inventory from CSV files
- Save inventory automatically after each operation
- Skip invalid rows when loading data

---

## How It Works

1. The program initializes an empty inventory (dictionary).
2. A loop displays a menu and waits for user input.
3. Based on the selected option, the corresponding function is executed.
4. Input validation ensures correct data types and values.
5. After each operation, the inventory is saved to a CSV file.

---

## Key Concepts Used

- Dictionaries and lists for data storage
- Functions and modular design
- File handling with CSV
- Error handling using `try/except`
- Loops and conditional logic