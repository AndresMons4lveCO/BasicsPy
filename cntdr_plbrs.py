# contador de palabras....

def contador_de_palabras():
    while True:
        entrada_usuario = str(input("introduce un texto, te dire cuantas palabras tiene: "))
        cantidad_de_palabras = len (entrada_usuario.split(" "))
        if cantidad_de_palabras == 1:
            print(f"tu texto tiene solo {cantidad_de_palabras} palabra")    
        else:
            print(f"tu texto tiene {cantidad_de_palabras} palabras")
    return

contador_de_palabras()