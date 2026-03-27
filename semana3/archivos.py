import csv

def load_csv(path):
    """
    Carga productos desde un archivo CSV con validaciones.
    
    #?Args:
        path (str): Ruta del archivo CSV.
        
    #?Returns:
        tuple: (lista_de_productos, contador_errores) o (None, 0) si falla.
    """
    products = []
    error_count = 0
    
    try:
        # Intentar abrir el archivo con codificación UTF-8
        with open(path, mode='r', encoding='utf-8') as file:
            reader = csv.reader(file)
            
            # Leer encabezado
            try:
                header = next(reader)
            except StopIteration:
                print(f"Error: The file '{path}' is empty.")
                return None, 0
                
            # Validar encabezado: name,price,quantity
            expected_header = ["name", "price", "quantity"]
            if [h.lower().strip() for h in header] != expected_header:
                print(f"Error: Invalid header in '{path}'. Expected: {','.join(expected_header)}")
                return None, 0
                
            for row in reader:
                # Cada fila debe tener exactamente 3 columnas
                if len(row) != 3:
                    error_count += 1
                    continue
                
                name, price_str, quantity_str = row
                try:
                    # precio debe convertirse a float y cantidad a int
                    price = float(price_str)
                    quantity = int(quantity_str)
                    
                    # no negativos
                    if price < 0 or quantity < 0:
                        error_count += 1
                        continue
                        
                    # Almacenar con la misma estructura del inventario: nombre: {price, quantity}
                    # Pero retornamos una lista de dicts con el nombre incluido para procesar después
                    products.append({
                        "name": name.strip(),
                        "price": price,
                        "quantity": quantity
                    })
                except ValueError:
                    # Errores de conversión
                    error_count += 1
                    continue
                    
    except FileNotFoundError:
        print(f"Error: File '{path}' not found.")
        return None, 0
    except UnicodeDecodeError:
        print(f"Error: Unicode decoding error in '{path}'. Please ensure UTF-8 encoding.")
        return None, 0
    except Exception as e:
        print(f"\033[1;31mAn unexpected error occurred while loading CSV: {e}\033[0m")
        return None, 0
        
    return products, error_count

#* 4.Guardar CSV(persistencia de salida)
def save_csv(inventory, filename="store.csv"):
    """
    Guarda el inventario en un archivo CSV con el formato requerido.
    
    #?Args:
        inventory (dict): Inventario a guardar.
        filename (str, optional): Nombre del archivo. Defaults to "store.csv".
    """
    try:
        with open(filename, "w", newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            # Encabezado en español según requerimiento de carga
            writer.writerow(["name", "price", "quantity"])
            for name, details in inventory.items():
                writer.writerow([name.capitalize(), details['price'], details['quantity']])
        print(f"\033[1;32mInventory saved successfully to {filename}\033[0m")
        print("-----------------------------------")
    except Exception as e:
        print(f"\033[1;31mError saving inventory to CSV: {e}\033[0m")
