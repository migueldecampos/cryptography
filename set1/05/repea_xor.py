import sys
import os.path


def encrypter(f_cont, key):
	file_len = len(f_cont)
	key_len = len(key)

	i = 0
	out = ""
	while i < file_len:
		new_byte = ord(f_cont[i]) ^ ord(key[i % key_len])
		out = out + format(new_byte, '02x')
		i = i + 1
	
	return out
		

def launcher():
	if len(sys.argv) != 3:
		print("usage:\n> python3 repea_xor.py file_to_encrypt.txt \"repeating-key\"")
		exit()

	if not os.path.isfile(sys.argv[1]):
		print("File does not exist.")
		exit()

	f = open(sys.argv[1], 'r')

	print(encrypter(f.read(), sys.argv[2]))



launcher()
