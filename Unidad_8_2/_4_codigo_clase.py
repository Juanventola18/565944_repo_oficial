import math

estudiantes = [
    {"nombre": "Ana",     "nota": 8},
    {"nombre": "Bruno",   "nota": 3.5},
    {"nombre": "Carla",   "nota": 9},
    {"nombre": "Diego",   "nota": 9.75},
    {"nombre": "Elena",   "nota": 3},
    {"nombre": "Franco",  "nota": 6.5}
]

# for e in estudiantes:
#     # print(math.ceil(e["nombre"]))
#     print(e["nombre"].lower())

# lista por comprension
# estudiantes_nombres = [ e["nombre"].lower() for e in estudiantes]
estudiantes_nombres = [ math.ceil(e["nota"]) * 2 for e in estudiantes]

print(estudiantes_nombres)