# ============================================================
# OPERACIONES CRUD BÁSICAS (con diccionarios)
# ============================================================

# CRUD = Create, Read, Update, Delete
# Son las 4 operaciones fundamentales sobre cualquier conjunto de datos.

# Funciones de soporte
def print_title(title):
    print("\n")
    print("***" * 20)
    print(f"{title}")

def print_productos():
    for p in productos:
        print(p)

# Declaramos e incializamos una lista global productos
# Donde cadad producto posee la siguiente estructura:
# Atributos: id_producto | categoria | nombre | precio_unitario

productos = [
    {
        "id_producto": 1,
        "categoria": "Escritura",
        "nombre": "Lápiz negro HB",
        "precio_unitario": 350
    },
    {
        "id_producto": 2,
        "categoria": "Escritura",
        "nombre": "Bolígrafo azul",
        "precio_unitario": 500
    }
]

# Visualizamos la lista global productos inicializada 
print_title("Primeros productos")
print_productos()


# CREATE (Alta de producto) 
"""
1. Crear un nuevo producto (producto_3). 
2. Agregarlo a la lista productos utilizando el método append(). 
3. Mostrar un mensaje confirmando la operación. 
"""

producto_3 = {
        "id_producto": 3,
        "categoria": "Escritura",
        "nombre": "Marcador permanente",
        "precio_unitario": 1200
    }
productos.append(producto_3)

print_title("CREATE: generar un nuevo registro producto")
print_productos()


# READ (Búsqueda de producto por id) 
"""
1. Buscar un producto a partir de su id_producto. 
2. Utilizar un for para recorrer la lista. 
3. Guardar el resultado en una variable. 
4. Mostrar el producto encontrado. 
"""
print_title("READ (Búsqueda de producto por id) ")

id_buscar = 5
producto_encontrado = None
for p in productos:
    if p["id_producto"] == id_buscar:
        producto_encontrado = p
        break

if  producto_encontrado:
    print(f"Producto encontrado: {producto_encontrado}")
else:
    print("No se ha encontrado")


# READ (Búsqueda de producto por campo indicado) 
"""
1. Buscar un producto a partir del campo indicado. 
2. Utilizar un for para recorrer la lista. 
3. Guardar el resultado en una lista. 
4. Mostrar los productos encontrados. 
"""
print_title("READ (Búsqueda de producto por campo indicado)")

clave_buscar = "categoria"
valor_buscar = "Escritura"
productos_encontrados = []

for p in productos:
    if p[clave_buscar] == valor_buscar:
        productos_encontrados.append(p)

if  productos_encontrados :
    print(f"Producto encontrado: {productos_encontrados}")
else:
    print("No se ha encontrado")



# UPDATE (Modificación de un producto según su id)
"""
1. Recorrer la lista de productos.
2. Identificar un producto por su id.
3. Modificar su precio_unitario.
4. Mostrar el producto actualizado.
"""
print_title("UPDATE (Modificación de un producto según su id)")

id_actualizar = 2
nuevo_precio = 750
producto_actualizado = None
for p in productos:
    if p["id_producto"] == id_actualizar:
        p["precio_unitario"] = nuevo_precio
        producto_actualizado = p

if producto_actualizado:
    print(f"Producto actualizado: {producto_actualizado}")
else:
    print("No se encontró el producto a actualizar")



# DELETE (Eliminación de un producto según su id)
"""
1. Buscar un producto por su id_producto.
2. Eliminarlo de la lista utilizando remove().
3. Mostrar la lista final de productos.
"""
print_title("DELETE (Eliminación de un producto según su id)")

id_eliminar = 1
producto_a_eliminar = None
for p in productos:
    if p["id_producto"] == id_eliminar:
        producto_a_eliminar = p

if producto_a_eliminar:
    productos.remove(producto_a_eliminar)
    print(f"Producto eliminado: {producto_a_eliminar}")
    print_productos()
else:
    print("No se encontró el producto a eliminar")

