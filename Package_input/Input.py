
def get_int(mensaje:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)->int|None:
    """pedir un número por consola.

    Args:
        mensaje (str): es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.

        mensaje_error (str):  mensaje de error en el caso de que el dato ingresado sea invalido.

        minimo (int): valor mínimo admitido (inclusive)

        maximo (int):  valor maximo admitido (inclusive)

        reintentos (int):  cantidad de veces que se volverá a pedir el dato en caso de error.

    Returns:
        int|None: numero
    """
    contador = 0
    while reintentos > contador:
        try:
            numero = int(input(mensaje))
            if numero >= maximo or numero <= minimo:
                print(mensaje_error)
                contador += 1
            else:
                return numero
            
        except ValueError:
            return "Eso no es un numero"
    
        
    return "Ingreso un numero fuera del rango, intentelo mas tarde"
    