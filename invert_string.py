# invertir una cadena dada.
# dentro de una lista [-1] nos da el ultimo dato de la lista
# dentro de una lista [:-1] ilimina el ultimo dato de la lista
# word[0].upper() si se coloca el upper() en la linea del join volvemos la salida todo en mayusculas.
def revert_string(string):
    """funcion que nos permite invertir una cadena dada
    Args:
        string (str): cadena a ser invertida
    Returns:
        str : cadena ya invertida
    """
    string = list(string)
    print(string)
    print(type(string))
    string = string[::-1]
    print(string)
    string = "".join( word[0] for word in string) 
    print(string)
    return string

revert_string(input("ingresa un texto: "))
    
def revert_string_using_for(string_f):
    """_summary_

    Args:
        string_f (_type_): _description_

    Returns:
        _type_: _description_
    """
    inverted_string = ""
    print(inverted_string)
    print(type(inverted_string))
    for character in string_f[::-1]:
        print(inverted_string)
        print(type(inverted_string))
        inverted_string += character
        print(inverted_string)
    return inverted_string
    
revert_string_using_for(input("ingresa un texto a ser invertido usando for: "))