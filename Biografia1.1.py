#libreria "re" necesaria para el metodo empleado cuando se verifica el nombre ingresado
import re
#Programación orientada a objetos:

class Biografia:
    #se definen los parametros o caracteristicas del objeto
    def __init__(self, nombre, dia_n, mes_n, año_n, direccion, meta_personal):
        self.nombre = nombre
        self.dia = dia_n
        self.mes = mes_n
        self.año = año_n
        self.direccion = direccion
        self.meta = meta_personal
    #se definen las habilidades o funciones del objeto
    def imprimir_biografia(self):
        print(f""" 
              el nombre del usuario es: {self.nombre}
              su fecha de nacimiento es el dia {self.dia} del mes de {self.mes} del año {self.año}
              su direccion de residencia es: {self.direccion}
              y su meta personal es: {self.meta}
              """)
# se crea el objeto usuario1
usuario1 = Biografia(input("introduzca su primer nombre seguido de su primer apellido: "),
input("introduzca su dia de nacimiento: "),
input("introduzca su mes de nacimiento: "),
input("introduzca su año de nacimiento: "),
input("introduzca su direccion de residencia: "),
input("introduzca su meta actual: "))        

verificadordenombre = usuario1.nombre.isalpha()

# se crea una funcion para obtener un nombre valido.

def obtener_nombre_valido():
    while True:
        # usando la expresion regular de abajo se valida que el nombre solo contenga
        # letras y espacios..
        if re.match("^[a-zA-Z ]+$", usuario1.nombre): # esta linea nos dara un TRUE si se
            # se cumple los requisitos escritos en la expresion si nos da false salta al else
            #al final retornamos el nombre a su respectiva variable.
            nombreSpliteado = usuario1.nombre.split()
            nombreCapitalized = " ".join(word.capitalize() for word in nombreSpliteado)
            return nombreCapitalized
        # si no lo cumple salta el aviso de ingresar un nuevo nombre.
        else:
            usuario1.nombre = input("por favor ingresa un nombre valido: ")
            
# se crea una funcion para obtener un mes valido.

def obtener_mes_valido():
    meses = {
        1: "Enero",
        2: "Febrero",
        3: "Marzo",
        4: "Abril",
        5: "Mayo",
        6: "Junio",
        7: "Julio",
        8: "Agosto",
        9: "Septiembre",
        10: "Octubre",
        11: "Noviembre",
        12: "Diciembre"
    }

    while True:
        try:
            print(usuario1.mes)
            print(type(usuario1.mes))
            usuario1.mes = int(usuario1.mes)
            print(type(usuario1.mes))
            
            if usuario1.mes > 0 and usuario1.mes <= 12:
                return meses[usuario1.mes]
            else:
                try:
                    mes_numero = int(input("Ingrese el mes de nacimiento en forma numérica: "))
                    if mes_numero in meses:
                        return meses[mes_numero]
                    else:
                        print("El valor numérico del mes tiene que estar entre 1 y 12.")
                except ValueError:
                    print("Por favor, ingrese el mes de nacimiento en forma numérica y dentro del rango de 1 a 12.")
        except ValueError:
            try:
                mes_numero = int(input("Ingrese el mes de nacimiento en forma numérica y dentro del rango de 1 a 12: "))
                if mes_numero in meses:
                    return meses[mes_numero]
                else:
                    print("El valor numérico del mes tiene que estar entre 1 y 12.")
            except ValueError:
                print("Por favor, ingrese el mes de nacimiento en forma numérica y dentro del rango de 1 a 12.")

# se crea una funcion para obtener un dia valido.

def obtener_dia_valido():
    while True:
        try:
            usuario1.dia = int(usuario1.dia)
            if usuario1.dia > 0 and usuario1.dia <= 31:
                return usuario1.dia
            else:
                try:
                    usuario1.dia = int(input("Ingrese el dia de nacimiento en forma numérica y dentro del rango de 1 a 31: "))
                
                except ValueError:
                    print("Por favor, ingrese el dia de nacimiento en forma numérica y dentro del rango de 1 a 12.")
        
        except ValueError:
            try:
                usuario1.dia = int(input("Ingrese el dia de nacimiento en forma numérica y dentro del rango de 1 a 31: "))
                if usuario1.dia > 0 and usuario1.dia <= 31:
                    return usuario1.dia
                else:
                    print("El valor numérico del dia tiene que estar entre 1 y 31.")
            except ValueError:
                print("Por favor, ingrese el dia de nacimiento en forma numérica y dentro del rango de 1 a 31.")     

# se crea una funcion para obtener un año valido.

def obtener_año_valido():
    while True:
        try:
            usuario1.año = int(usuario1.año)
            if usuario1.año > 1920 and usuario1.año <= 2024:
                return usuario1.año
            else:
                try:
                    usuario1.año = int(input("Ingrese el año de nacimiento en forma numérica y dentro de lo razonable: "))
                
                except ValueError:
                    print("Por favor, ingrese el año de nacimiento en forma numérica y dentro de lo razonable.")
        
        except ValueError:
            try:
                usuario1.año = int(input("Ingrese el año de nacimiento en forma numérica y dentro de lo razonable "))
                if usuario1.año > 1920 and usuario1.año <= 2024:
                    return usuario1.año
                else:
                    print("El valor numérico del año tiene que estar dentro de lo razonable.")
            except ValueError:
                print("Por favor, ingrese el año de nacimiento en forma numérica y dentro de lo razonable.")

# Ejemplo de uso:

print("El mes es:", usuario1.mes)

# se crea la funcion para obtener un dia valido. 

# ejecutamos las funciones.
usuario1.dia = obtener_dia_valido()
usuario1.mes = obtener_mes_valido()
usuario1.año = obtener_año_valido()
usuario1.nombre = obtener_nombre_valido()
usuario1.imprimir_biografia()


# como ultima anotación estaba utilizando el metodo especial .isalpha
# para obtener la veracidad de un nombre valido, pero este solo admite
# una sola palabra sin espacios, por lo tanto usamos la libreria "re"
