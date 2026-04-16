# ============================================================
# OPERACIONES CRUD BÁSICAS (con diccionarios)
# ============================================================

# CRUD = Create, Read, Update, Delete
# Son las 4 operaciones fundamentales sobre cualquier conjunto de datos.

# Declaramos e incializamos una lista global clientes
# Donde cadad cliente posee la siguiente estructura:
# Atributos: id_cliente | razon_social | email | cell

clientes = [
    {
        "id_cliente": 1,
        "razon_social": "YPF",
        "email": "compras@ypf.com",
        "cell": "+5491134567890",
    },
    {
        "id_cliente": 2,
        "razon_social": "Arcor",
        "email": "compras@arcor.com",
        "cell": "'+5491145671234",
    },
]

# Visualizamos la lista global clientes inicializada 
# print(clientes)


# CREATE (Alta de clientes) 
"""
1. Crear un nuevo cliente (cliente_3). 
2. Agregarlo a la lista clientes utilizando el método append(). 
3. Mostrar un mensaje confirmando la operación. 
"""


# READ (Búsqueda de cliente por id) 
"""
1. Buscar un cliente a partir de su id_cliente. 
2. Utilizar un for para recorrer la lista. 
3. Guardar el resultado en una variable. 
4. Mostrar el cliente encontrado. 
"""


# READ (Búsqueda de cliente por campo indicado clave:valor) 
"""
1. Buscar un cliente a partir de su id_cliente. 
2. Utilizar un for para recorrer la lista. 
3. Guardar el resultado en una variable. 
4. Mostrar el cliente encontrado. 
"""


# UPDATE (Modificación de un cliente según su id) 
"""
1. Recorrer la lista de clientes. 
2. Identificar un cliente por su id. 
3. Modificar su email. 
4. Mostrar el cliente actualizado. 
"""


# DELETE (Eliminación de un cliente según su id) 
"""
1. Buscar un cliente por su id_cliente. 
2. Eliminarlo de la lista utilizando remove(). 
3. Mostrar la lista final de productos. 
"""

