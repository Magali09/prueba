from Package_input.validate import *
from Package_input.Input import *


validate_number(get_int("Ingrese numero: ", "Erros, fuera de rango: ", 1, 10, 3))

# respuesta = get_int("Ingrese un numero entre el 1 y 10: ", "Error, Ingrese un numero entre el 1 o 10: ", 1, 10,3)
# print(respuesta)

# respuesta = get_float("Ingrese un numero decimal entre 1.1 y 10.1: ", "Error, Ingrese un numero entre el 1.1 o 10.1: ", 1.0, 10.0,3)
# print(respuesta)

# respuesta = get_string(10)
# print(respuesta)
