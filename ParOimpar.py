#creando un programa que te pide un numero y te dice si 
#   es par o impar.


def ParOiMpar():
    while True:
        numero_dado1 = input("dame un numero, te dire si es par o impar: ")
        try:
            resultado = float(numero_dado1)
        except:
            print("ingresaste algo diferente a un numero, vuelve a intentarlo...")
            continue
        if resultado == 0:
            print("¡el numero es CERO!")
        elif resultado % 2 == 0:
            print("¡es un numero par!")
        elif resultado % 2 == 1:
            print("¡es un numero impar!")   
    
print(ParOiMpar())                    