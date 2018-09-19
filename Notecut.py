# Notecut: a simple program to get notes pasted directly in your clipboard

import os, pyperclip

input = input("Please insert file name: > ")

title = input.lower() + ".txt"

if title in notes:
    pyperclip.copy(title.open())
    print('Your ' + input +'note has been copied to the clipboard.')
    title.close()
else:
    print('There is no note called ' + title + 'in this folder.')
