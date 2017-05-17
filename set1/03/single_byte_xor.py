import sys
import re

def decode(hex_string, byte):
	
	hexa = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8":8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
	
	
	i = 1
	ln = len(hex_string)
	output = ""
	while i < ln:
		value = hexa[hex_string[i - 1]] << 4
		value = value | hexa[hex_string[i]]
		value = value ^ byte
		output = output + chr(value)
		i = i + 2
	
	return output


def print_possibilities():





	if len(sys.argv) != 2:
		print("Pass one hex string as parameter.")
		exit()
	if not re.match('^[0-9a-fA-F]{1,}$', sys.argv[1]):
		print("Pass one hex string as parameter.")
		exit()
	i = 0
	while i < 256:
		print("(", i, ")", decode(sys.argv[1], i))
		i = i + 1

print_possibilities()
