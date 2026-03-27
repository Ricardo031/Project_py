# Solución de Ejercicios Riwi - Fundamentos de Python

Este repositorio centraliza los proyectos desarrollados durante las tres primeras semanas del módulo de Python en **Riwi**. El objetivo principal ha sido evolucionar un sistema de gestión de inventarios, aplicando conceptos desde lo más básico hasta la modularización avanzada y persistencia de datos.

## Estructura del Proyecto

El proyecto se divide en tres fases incrementales:

### 📁 [Semana 1: Fundamentos Básicos](file:///c%3A/Users/rjtb-/OneDrive/Desktop/Codigos/Riwi/Project_py/semana1)
En esta etapa inicial se establecieron las bases del manejo de datos en Python:
- **Variables y Tipos:** Uso de `string`, `float` e `int`.
- **Entrada/Salida:** Interacción con el usuario mediante `input()` y `print()`.
- **Validación:** Implementación de bloques `try/except` para asegurar entradas numéricas correctas.
- **Lógica Simple:** Cálculo automático del costo total por producto.

### 📁 [Semana 2: Estructuras de Control y Colecciones](file:///c%3A/Users/rjtb-/OneDrive/Desktop/Codigos/Riwi/Project_py/semana2)
Se introdujo la gestión de múltiples elementos y la organización del código:
- **Colecciones:** Uso de `listas` y `diccionarios` para agrupar productos.
- **Bucles y Condicionales:** Menú interactivo basado en `while` y toma de decisiones con `if/elif/else`.
- **Modularización Temprana:** Creación de funciones específicas para agregar productos, mostrar el inventario y calcular estadísticas básicas.
- **Estadísticas:** Uso de funciones integradas como `sum()` y comprensiones de listas.

### 📁 [Semana 3: Modularización Avanzada y Persistencia](file:///c%3A/Users/rjtb-/OneDrive/Desktop/Codigos/Riwi/Project_py/semana3)
La fase más compleja, enfocada en la escalabilidad y el manejo de archivos:
- **Arquitectura Modular:** Separación de responsabilidades en archivos distintos (`app.py`, `servicios.py`, `archivos.py`).
- **Persistencia CSV:** Lectura y escritura de datos en archivos CSV para conservar la información entre sesiones.
- **Validaciones Robustas:** Control estricto de encabezados, columnas y valores no negativos al cargar archivos externos.
- **Lógica de Fusión:** Capacidad de sobrescribir el inventario o fusionarlo (actualizando precios y sumando cantidades).
- **Interfaz de Usuario:** Mejora visual con códigos de colores ANSI en la terminal y resúmenes de carga detallados.

---
*Este proyecto refleja el progreso en el dominio de Python, desde la sintaxis básica hasta patrones de diseño utilizables*
