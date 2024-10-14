


        

           
            
            
# def get_float(mensaje:str, mensaje_error:str, minimo:float, maximo:float, reintentos:int)->float|None:
#     """pedir un número decimal por consola.

#     Args:
#         mensaje (str): es el mensaje que se va a imprimir antes de pedirle al usuario el dato por consola.

#         mensaje_error (str):  mensaje de error en el caso de que el dato ingresado sea invalido.

#         minimo (float): valor mínimo admitido (inclusive)

#         maximo (float):  valor maximo admitido (inclusive)

#         reintentos (int):  cantidad de veces que se volverá a pedir el dato en caso de error.

#     Returns:
#         int|None: numero
#     """
#     contador = 0
#     while reintentos > contador:
#         try:
#             numero = float(input(mensaje))
#             if numero >= maximo or numero <= minimo:
#                 print(mensaje_error)
#                 contador += 1
#             else:
#                 return numero
            
#         except ValueError:
#             return "Eso no es un numero"
    
        
#     return "Ingreso un numero fuera del rango, intentelo mas tarde"
        


# def get_string(longitud:int)->str|None:
#     """ validará la longitud de la cadena ingresada en el parámetro actual recibido

#     Args:
#         longitud (int): cantidad de caracteres

#     Returns:
#         string|None: cadena o None
#     """
#     # while True:
#     cadena = input("ingrese palabra: ")
    
    
#     while len(cadena) < longitud or not cadena.isalpha():
#         if len(cadena) < longitud:
#             cadena = input(f"Reingrese una longitud válida, máximo {longitud} caracteres: ")
#         elif not cadena.isalpha():
#             cadena = input("Error, NO ingrese números, solo letras: ")

#     return cadena 
    
        

def validate_number(numero):
    
    if type(numero) == int:
        print(numero)
    return numero    

        
   
    
        
 
    


            

            

   
            
     
              
     
        
        
    

