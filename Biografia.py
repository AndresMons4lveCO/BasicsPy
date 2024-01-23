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
              su fecha de nacimiento es el dia {self.dia} del mes {self.mes} del año {self.año}
              su direccion de residencia es: {self.direccion}
              y su meta personal es: {self.meta}
              """)
# se crea el objeto usuario1
ususario1 = Biografia(input("introduzca su primer nombre seguido de su primer apellido: "),
                          input("introduzca su dia de nacimiento: "),
                          input("introduzca su mes de nacimiento: "),
                          input("introduzca su año de nacimiento: "),  
                          input("introduzca su direccion de residencia: "),
                          input("introduzca su meta actual: ")
                          )

verificadordenombre = ususario1.nombre.isalpha()

# se crea una funcion para obtener un nombre valido.
def obtener_nombre_valido():
    while True:
        # usando la expresion regular de abajo se valida que el nombre solo contenga
        # letras y espacios.
        if re.match("^[a-zA-Z ]+$", ususario1.nombre):
            #al final retornamos el nombre a su respectiva variable.
            return ususario1.nombre
        # si no lo cumple salta el aviso de ingresar un nuevo nombre.
        else:
            ususario1.nombre = input("por favor ingresa un nombre valido: ")
        
print(verificadordenombre)
print(ususario1.nombre)
print(obtener_nombre_valido())

# ejecutamos las funciones.
ususario1.nombre = obtener_nombre_valido()
ususario1.imprimir_biografia()


# como ultima anotación estaba utilizando el metodo especial .isalpha
# para obtener la veracidad de un nombre valido, pero este solo admite
# una sola palabra sin espacios, por lo tanto usamos la libreria "re"
