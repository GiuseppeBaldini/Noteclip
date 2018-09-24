# Notecut: a simple program to get notes pasted directly in your clipboard

import os, sys, pyperclip

note_name = sys.argv[1]
file = note_name.lower() + ".txt"
current_dir = os.getcwd()

dir_list = os.listdir(current_dir)

if file in dir_list:
    file_text = open(file, 'r')
    content = file_text.read()
    pyperclip.copy(content)
    print('The content of ' + file + ' has been copied to the clipboard.')
    file_text.close()
else:
    print('There is no note called ' + file + ' in this folder.')
