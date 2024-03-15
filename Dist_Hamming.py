# medir la distancia de hamming entre 2 strings

string_a = "patitosw"
string_b = "paratosa"

def hammingDistance(str_A , str_B):
    
    if len(str_A) == len(str_B):
        counter_distance = 0
        str_A = list(str_A)
        str_B = list(str_B)
        count = 0
        for letter in str_A:
            if letter != str_B[count]:
                count += 1
                counter_distance += 1
            else:
                count += 1
                   
        return counter_distance
    else:
        print("strings are not the same length")
    
print(hammingDistance(string_a, string_b))