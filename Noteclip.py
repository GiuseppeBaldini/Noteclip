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

starting_dir = os.getcwd()
file_name = note_name + ".txt"
notes_dir = 'C:\\Users\\Giuseppe\\Documents'

def find(file, path):
    for root, dirs, files in os.walk(notes_dir):
        if file_name in files:
            print (file_name +' found in ' + root)
            new_working_dir = root
            return new_working_dir
    else:
        print('There is no file called ' + file_name + ' in ' + path)
        exit()

nwd = find(file_name, notes_dir)
working_dir = os.chdir(nwd)
dir_list = os.listdir(nwd)

if file_name in dir_list:
    file_text = open(file_name)
    content = file_text.read()
    pyperclip.copy(content)
    print('The content of ' + file_name + ' has been copied to the clipboard.')
    file_text.close()
else:
    print('There is no file called ' + file_name + ' in this folder.')

os.chdir(starting_dir)
