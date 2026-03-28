# Sistema de Gestión de Inventario

## Descripción
Este proyecto es un sistema de gestión de inventario modular desarrollado en Python. Permite administrar productos, realizar operaciones CRUD, calcular estadísticas y guardar los datos en archivos CSV.

El sistema está dividido en tres módulos principales:
- `app.py`: Programa principal e interacción con el usuario (menú)
- `servicios.py`: Lógica del negocio (operaciones del inventario)
- `archivos.py`: Manejo de archivos (carga y guardado en CSV)

---

## Funcionalidades

### 1. Gestión de Productos (CRUD)
- Agregar nuevos productos
- Ver todos los productos
- Buscar un producto
- Actualizar precio y cantidad
- Eliminar productos

### 2. Operaciones de Inventario
- Fusionar inventarios desde archivos externos
- Validar entradas (precio, cantidad, nombre)
- Manejar casos de inventario vacío

### 3. Estadísticas
- Valor total del inventario
- Cantidad total de productos
- Producto más costoso

### 4. Persistencia de Datos
- Cargar inventario desde archivos CSV
- Guardar automáticamente después de cada operación
- Ignorar filas inválidas al cargar datos

---

## Cómo Funciona

1. El programa inicia con un inventario vacío (diccionario).
2. Se muestra un menú en un bucle continuo.
3. El usuario selecciona una opción y se ejecuta la función correspondiente.
4. Se validan los datos ingresados para evitar errores.
5. Después de cada operación, el inventario se guarda en un archivo CSV.

---

## Conceptos Clave Utilizados

- Diccionarios y listas para almacenar datos
- Funciones y modularidad
- Manejo de archivos CSV
- Manejo de errores con `try/except`
- Estructuras de control (condicionales y bucles)