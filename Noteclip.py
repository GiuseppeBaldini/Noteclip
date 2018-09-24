# Python 3
# Noteclip: a simple program to get notes pasted directly in your clipboard

import os, sys, pyperclip

note_name = sys.argv[1]
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
