#pedir el nombre de una organizacion e imprimir su acronimo.
print("""ingresa el nombre de la empresa u organizacion
      de la cual quieres obtener su acronimo.
      """)
def obtener_acronimo(cadena_texto):
    # Dividir la cadena en palabras usando split que por defecto serpara por los "espacios"
    palabras = cadena_texto.split()  
    # Tomar la primera letra de cada palabra y convertirla a mayúsculas
    # las comillas dobles nos daran la separacion de las letras obtenidas
    # en este caso "" sin espacios ni nada todo pegado
    # .join es el metodo para concatenar elementos de una secuencia sea una lista o tupla
    #para unirlos en una sola cadena.
    acronimo = "".join(word[0].upper() for word in palabras)  
    #usamos junto ".upper" para volver las letras todas mayusculas
    # junto con un ciclo for para hacer cada letra en mayuscula.
    return acronimo

cadena_texto = input("Introduce una cadena de texto: ")
acronimo = obtener_acronimo(cadena_texto)

print("El acrónimo es:", acronimo)
