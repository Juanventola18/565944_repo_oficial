# PREGUNTA 2

from datetime import datetime

# Funcion que valida la fecha ingresada
def validar_fecha(fecha_str):
    try:
        datetime.strptime(fecha_str, "%Y-%m-%d")
        return True
    except ValueError:
        return False

# Funcion que convierte el tipo de dato
def parsear_fecha(fecha_str):
    try:
        return datetime.strptime(fecha_str, "%Y-%m-%d").date()
    except ValueError:
        return None
    
fecha = input("Ingrese una fecha (YYYY-MM-DD): ")

if validar_fecha(fecha):
    print(f"Formato de fecha ingresado correcto!\n Tipo de dato ingresado {type(fecha)} - Fecha parseada {type(parsear_fecha(fecha))}")
else:
    print("Formato inválido")


