# Python 3
# Noteclip: a simple program to get notes pasted directly in your clipboard

import sys
import os

try:
    import pyperclip
except ImportError or ModuleNotFoundError:
    print('Pyperclip module not found. Please download it.')

try:
    note_name = sys.argv[1]
except IndexError:
    note_name = input('Please input the name of your note here: > ')

file = note_name.lower() + ".txt"
working_dir = os.chdir('C:\\Users\\Giuseppe\\Documents\\Notes')

dir_list = os.listdir(working_dir)

if file in dir_list:
    file_text = open(file)
    content = file_text.read()
    pyperclip.copy(content)
    print('The content of ' + file + ' has been copied to the clipboard.')
    file_text.close()
else:
    print('There is no note called ' + file + ' in this folder.')
