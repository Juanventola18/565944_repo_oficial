from shared import utilities

# Funcion leer consola
# Parametros: none
# Retorno: diccionario producto
def leer_producto():
    # Ingresar categoria
    while True:
        categoria = input("Ingrese la categoria: ")
        if utilities.validar_categoria(categoria):
            break
        print("Categoría no válido intente nuevamente...")

    # Ingresar nombre
    while True:
        nombre = input("Ingrese el nombre: ")
        if utilities.validar_nombre(nombre):
            break
        print("Nombre no válido intente nuevamente...")

    # Ingresar precio_unitario
    while True:
        precio_unitario = input("Ingrese el precio unitario: ")
        if utilities.validar_precio_unitario(precio_unitario):
            break
        print("Precio no válido intente nuevamente...")

    # Normalizacion y carga en variable temporal
    producto = {
        "categoria": categoria.strip().title(),
        "nombre": nombre.strip().title(),
        "precio_unitario": float(precio_unitario.strip()),
    }

    return producto