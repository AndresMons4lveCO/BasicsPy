# word counter whit regular expressions
import re # library for work with Regular Expressions.

def wordToCount():
    words = input("enter the phrase to count the words: ")
    words = words.strip() # el metodo strip elimina los espacios sobrantes de una cadena
                          # tanto al inicio como al final.
                          
    words = re.sub(r"\s+", " " , words) # el metodo .sub() nos permite subscribir expreciones
                                       # regulares por la cadena que queramos en este caso
                                       # \s+ uno o mas espacios por " " un solo espacio.
    
    quantity = len(words.split(" ")) # con el metodo split, separamos una cadena por medio
                                     # del argumento que nosotros le pasemos en este caso
                                     # " " un espacio que es el que se encuentra entre cada
                                     # palabra en una oracion. obteniendo una lista.
                                     # y con la funcion len obtenemos la cantidad palabras.
    print(words.split(" "))                                     
    print(len(words))
    print(words)
    print(quantity)
    return quantity

wordToCount()