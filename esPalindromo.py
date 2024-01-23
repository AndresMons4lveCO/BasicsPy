# LA CADENA DE TEXTO INGRESADA ES UN PALINDROMO ?
# el codigo no es mio, solo le añadi los print() y los comentarios de analisis al codigo
# muy bueno este codigo para comprender mejor el manejo de listas y el uso de funciones
# los print() que le añadi son para ver como la cadena de texto que ingreaste
# se va transformando con el manejo de listas y un limpio uso de funciones..
# dejo el link de donde lo tome https://github.com/kuzmicheff/palindrome/blob/master/palindrome.py

def convertInputToStringList():
    #aqui nos pedira la cadena de texto.
    rawInput = input("\nPlease enter a word, phrase, or a sentence \nto check if it is a palindrome: ") 
    print(rawInput)
    # la primera funcion toma la cadena de texto ingresada y vuelve todas las letras en minusculas
    rawString = rawInput.lower()
    print(rawString)
    # luego esa cadena de texto la vuelve una lista y a esa lista le da un return.
    rawList = list(rawString)
    print(rawList)
    return rawList

# en esta funcion se encarga de eliminar puntos, espacios y unos cuantos signos para que
# solo queden las letras a comparar, si se quisiera eliminar otros simbolos o signos solo
# se tienen que añadir a la lista "analphabeticList". te da return a esa lista sin simbolos.
def stripAnalphabetics(dirtyList): 
    analphabeticList = [" ", "-", ".", ",", ":", ";", "!", "?", "'", "\""] 
    for character in analphabeticList: 
        if character in dirtyList: 
            dirtyList.remove(character) 
            return stripAnalphabetics(dirtyList)
    print(dirtyList)
    return dirtyList 

# en esta funcion se hace el chek de si lo ingresado por el usuario es un palindromo
# por medio de comparacion de las listas una en orden natural y la otra con el orden
# invertido por medio del manejo de listas "[::-1]" donde ese "-1" nos invierte las
# posiciones de cada caracter en la lista.
# si al final las listas son iguales nos retorna un texto o el otro si no son iguales.
def runPalindromeCheck(straightList):
    reversedList = straightList[::-1]
    print(reversedList)
    if reversedList == straightList: 
        return "The text you have entered is a palindrome!" 
    else: 
        return "The text you have entered is not a palindrome." 

# muy bueno este bloque de funcion que incluye las funciones creadas anteriormente.
# donde la primera funcion que nos returnaba "rawlist" es el equivalente aqui a "originalList"
# luego esa lista pasara como parametro al eliminador de simbolos asi returnandonos una nueva "originalList"
# por ultimo esta pasara a ser parametro del runpalindromeChek retornandonos el texto
# de si es un palindromo o no...
def main(): 
    print("\nPalindrome checker") 
    originalList = convertInputToStringList()
    originalList = stripAnalphabetics(originalList) 
    palindromeCheck = runPalindromeCheck(originalList)
    print(palindromeCheck)

#por ultimo solo nos queda ejecutar el bloque de funciones principal "main()"

main() 