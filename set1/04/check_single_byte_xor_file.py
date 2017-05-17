import sys
import re
import fileinput

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


def checker(string):
	ln = len(string)
	spaces = 0
	capitals = 0
	lowercase = 0
	punctuation = 0
	numbers = 0
	for c in string:
		asc = ord(c)
		if asc == 32:
			spaces = spaces + 1
		elif asc >= 65 and asc <= 90:
			capitals = capitals + 1
		elif asc >= 97 and asc <= 122:
			lowercase = lowercase + 1
		elif asc == 33 or asc == 34 or asc == 40 or asc == 41 or asc == 44 or asc == 46 or asc ==39:
			punctuation = punctuation + 1
		elif asc >= 48 and asc <= 57:
			numbers = numbers + 1
	
	if spaces + capitals + lowercase + punctuation + numbers < 4 * ln / 5:
		return False
	if capitals + lowercase < punctuation:
		return False
	if capitals > lowercase:
		return False
	if spaces < ln / 10:
		return False
	return True



def print_possibilities(line):

#	if len(sys.argv) != 2:
#		print("Pass one hex string as parameter.")
#		exit()
#	if not re.match('^[0-9a-fA-F]{1,}$', sys.argv[1]):
#		print("Pass one hex string as parameter.")
#		exit()
	i = 0
	while i < 256:
		string = decode(line, i)
		if checker(string):
			print("(", i, ") ", string, sep='')
		i = i + 1


def launcher():
	cnt = 1
	for line in fileinput.input():
		print(f"## Line {cnt}")
		print_possibilities(line)
		print()
		cnt = cnt + 1


launcher()
