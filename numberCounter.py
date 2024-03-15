# number counter with regular expressions 
import re

string = "oaij#d930u!asgd78sat$d8fa9f87a&s8=d°as8f9d7"

def numberCounter(userString):
    print(userString)
    stringOnlyLetters = re.sub(r"[^a-zA-Z]", "" , userString) # sustituye todos los caracteres excepto letras
    print(stringOnlyLetters)
    stringOnlyDigits = re.sub(r"[a-zA-Z]", "" , userString) # sustituye solo las letras del alfabeto
    print(stringOnlyDigits)
    stringOnlyNumbers = re.sub(r"[^0-9]", "" , userString) # sustituye todo lo que no sea un numero natural
    print(stringOnlyNumbers)
    quantityNumbers = len(stringOnlyNumbers)
    print(quantityNumbers)
    
numberCounter(string)












