# Demo proyecto
# La idea es que vayan analizando la estructura de archivos para su proyecto
# Para ejecutarlo pararse en Demo_TPO y ejecutar en consola python -m app.main

# Importamos librerias externas
from tabulate import tabulate
from core import services
from interface import inputHandler


# Declaración de la Funcion Principal
def main():
    print("Bienvenido!!")

    while True:
        print(
            """
    Ingrese:
    1. Para crear un nuevo producto
    2. Para listar todos los productos
    3. Para buscar producto por id_producto
    4. Para buscar producto por nombre de producto
    5. Para salir
            """
        )
        opcion = input("Ingrese su opción: ")
        match opcion:
            case "1":
                # Alta de producto
                producto = inputHandler.leer_producto()
                response = services.persistir_producto(productos, producto)
                print("Producto insertado exitosamente") if response else None

            case "2":
                # Listar productos
                print(tabulate(productos[:5], headers="keys", tablefmt="grid"))

            case "3":
                id_producto = int(input("Ingrese el id_producto a buscar: "))
                productos_found = services.get_producto_by_id(productos, id_producto)
                if productos_found:
                    print(tabulate(productos_found, headers="keys", tablefmt="grid"))
                else:
                    print("No match")
            case "4":
                nombre = input("Ingrese el nombre del producto a buscar - total o parcial: ")
                productos_found = services.get_producto_by_nombre(productos, nombre)
                print(tabulate(productos_found[:5], headers="keys", tablefmt="grid"))
            case "5":
                # Terminar App
                print("Saliendo...")
                break
            case _:
                print("Opción inválida, intente nuevamente...")


# Invocar a la función principal
if __name__ == "__main__":

    # Declaramos la variable global (se pueden cargar algunos registros para inicializarla)
    productos = [
        {
            "id_producto": 1,
            "categoria": "Escritura",
            "nombre": "Lápiz negro HB",
            "precio_unitario": 350,
        },
        {
            "id_producto": 2,
            "categoria": "Escritura",
            "nombre": "Bolígrafo azul",
            "precio_unitario": 500,
        },
    ]
    main()