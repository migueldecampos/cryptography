import sys
import re


def xorer():
	
	if len(sys.argv) != 3:
		print("Wrong number of parameters.")
		exit()
	
	if len(sys.argv[1]) != len(sys.argv[2]):
		print("Strings must be of the same lenght.")
		exit()
	
	if not re.match('^[0-9a-fA-F]{1,}$', sys.argv[1]) or not re.match('^[0-9a-fA-F]{1,}$', sys.argv[2]):
		print("Those are not hex strings.")
		exit()
	
	de_hexer = {"0": 0, "1": 1, "2": 2, "3": 3, "4": 4, "5": 5, "6": 6, "7": 7, "8": 8, "9": 9, "a": 10, "b": 11, "c": 12, "d": 13, "e": 14, "f": 15, "A": 10, "B": 11, "C": 12, "D": 13, "E": 14, "F": 15}
	hexer = "0123456789abcdef"

	xord_string = ""
	ln = len(sys.argv[1])
	i = 0
	while i < ln:
		um = de_hexer[sys.argv[1][i]]
		dois = de_hexer[sys.argv[2][i]]
		res = um ^ dois
		xord_string = xord_string + hexer[res]
		i = i + 1
	
	print(xord_string)

xorer()
