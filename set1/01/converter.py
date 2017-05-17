import re

def converter(hex_string):
    if len(hex_string) > 0 and hex_string[-1] == "\n":
        hex_string = hex_string[:-1] 
    if not re.match('^[0-9a-fA-F]{1,}$', hex_string):
        print("ola")
        return None
    

    base64 = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    hexa = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8":8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
    ln = len(hex_string)
    i = 0
    to_add = 0;
    bits_in = 0;
    tmp = 0
    base64_string = ""
    while i < ln:
        tmp = hexa[hex_string[i]]
        if bits_in == 0:
            to_add = 0
            tmp = tmp << 2
            to_add = tmp
            bits_in = 4
        elif bits_in == 4:
            tmp2 = tmp >> 2
            to_add = to_add | tmp2
            base64_string = base64_string + base64[to_add]
            tmp = tmp & 0b11
            to_add = tmp << 4
            bits_in = 2
        elif bits_in == 2:
            to_add = to_add | tmp
            base64_string = base64_string + base64[to_add]
            to_add = 0
            bits_in = 0
        else:
            print("ERRRRRRRRRRROOOOOOOOOOOOO")
            return "ERRRROOROROROOROROROOROROROROOROROORO"
        i = i + 1

    if bits_in != 0:
        base64_string = base64_string + base64[to_add]

#    print("<" + base64_string + ">")

    return base64_string

if converter("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d") == "SSdtIGtpbGxpbmcgeW91ciBicmFpbiBsaWtlIGEgcG9pc29ub3VzIG11c2hyb29t":
    print("sucesso meu puto")

