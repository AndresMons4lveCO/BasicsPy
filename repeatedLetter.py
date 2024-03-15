# cuantas veces se repite un caracter en una cadena dada
# how many times a character is repeated in a given string

def repeated_counter():
    given_string = input("give a string you want to count the repeated letter: ")
    letter_to_count = input(" give the letter to count the times is repeated in the string: ")
    print(given_string)
    print(type(given_string))
    
    
    if letter_to_count in given_string:
        counter = 0
        #given_string = list(given_string)
        print(given_string)
        print(type(given_string))
        for letter in given_string:
            if letter_to_count == letter:
                counter += 1
                print(counter)
                print(type(counter))    
        return counter
    else:
        print("the letter you input dont in the string you give")

repeated_counter()