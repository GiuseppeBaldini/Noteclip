# Python 3.6 - Windows 10.0.16299
# Noteclip: a simple program to get notes copied directly in the clipboard

import sys
import os

# Pyperclip is not a built-in module, remind users to download it if necessary.
try:
    import pyperclip
except ImportError or ModuleNotFoundError:
    print('Pyperclip module not found. Please download it.')

# If the argument is missing, let users input it directly.
try:
    note_name = sys.argv[1]
except IndexError:
    note_name = input('Please input the name of your note here: > ')

# Define 3 key variables: current working directory, file name and path to scan.
start_working_dir = os.getcwd()
file_name = note_name + ".txt"
notes_path = 'C:\\Users\\Giuseppe\\Documents'

def find(file, path):
    """
    Return the folder where a given file is located by scanning every subfolder
    of the given path. In this case, assuming files are more likely to be
    at the end of the path, it is faster to scan bottom-up.
    """
    for root, dirs, files in os.walk(path, topdown = False):
        if file in files:
            print (file +' found in ' + root)
            temp_working_dir = root
            return temp_working_dir
    else:
        print('There is no file called ' + file_name + ' in ' + path +
            '\nPlease make sure spelling and capitalisation are correct.')
        exit()

twd = find(file_name, notes_path)

# Temporarily change the working directory to the one where we found the file.
os.chdir(twd)


def copy(the_file):
    """ Open file, copy content to the clipboard using pyperclip, close it."""
    file_text = open(the_file)
    content = file_text.read()
    pyperclip.copy(content)
    print('The content of ' + the_file + ' has been copied to the clipboard.')
    file_text.close()

copy(file_name)

# Come back to the starting working directory.
os.chdir(start_working_dir)
