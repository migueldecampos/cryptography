import fileinput
import sys
import os.path
import re

import converter



def launcher():

    if len(sys.argv) > 2:
        print("Too many arguments.")
        exit()

    if len(sys.argv) == 2 and not os.path.isfile(sys.argv[1]):
        print(converter.converter(sys.argv[1]))
    
    else:
        for line in fileinput.input():
            print(converter.converter(line))


launcher()
