import random

numero_secreto = int(random.randint(1,50))
cantidad_de_intentos = 1
print("""
      .......................................................
      Hola Acontinuacion jugaremos a adivina el numero.
      tienes que adivinar un numero que esta dentro del
      rango 1 - 50 en la menor cantidad de intentos posibles.
      .......................................................
      """)

while True:
    try:
        numero_del_usuario = int(input("dame un numero: "))
    except:
        print("tienes que darme un numero entre 1 y 50")
        continue
    if numero_del_usuario > 50 or numero_del_usuario < 1:
        print("ese numero esta fuera del rango de 1 y 50, vuelve a intentarlo..")
    elif numero_del_usuario != numero_secreto:
        cantidad_de_intentos += 1
        print("ese no es el numero secreto...")
    elif numero_del_usuario == numero_secreto:
        print("correcto ese es el numero secreto")
        break

    
     

print(f" el numero secreto fue: {numero_secreto}")
print(f" Hallar el numero secreto te tomo: {cantidad_de_intentos} intentos.")