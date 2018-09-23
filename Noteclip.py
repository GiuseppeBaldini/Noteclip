# Notecut: a simple program to get notes pasted directly in your clipboard

import sys, pyperclip

note = sys.argv[1]
file = note_name.lower() + ".txt"

if file in files:
    pyperclip.copy(file.open())
    print('The content of '+ file +'has been copied to the clipboard.')
    file.close()
else:
    print('There is no note called ' + file + 'in this folder.')
