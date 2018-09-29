# Noteclip

Noteclip is a simple Python program to retrieve notes directly in the clipboard using the Pyperclip module. 

### Introduction

Given an <code>argument</code>, the program does 2 things:

1. Searches (bottom-up) for <code>argument.txt</code> and returns its filepath

2. Copies the content of <code>argument.txt</code> in the clipboard so it's ready to be pasted

### Use cases

Noteclip can be used to store medium/long pieces of information that can be kept in plaintext. 

Examples include:

* Frequently used / public contact information 

* Email / Messages templates for different situations

* Temporary useful stuff you usually keep on Sticky Notes

**I do not recommend to use this program to retrieve extremely sensitive information such as:**

* Identification information (Passport number, Social Security Number etc.)

* Bank details (Account information, card information etc.)

* Passwords and other secturity details

### Preparation

1. Create notes as .txt files

2. Install **pyperclip** 

3. Assign <code>notes_path</code> variable to highest level folder where all your notes are
    
NOTE: _Using a path too broad makes the scan too slow. I would suggest keeping everything at least 3 levels below_ C:\ 

### Execution from Run command

I included a batch file to run the program directly from the Run window simply typing <code> noteclip [note name] </code>. 

NOTE: _Change filepath in Batch file to reflect location of the program on your computer_

### Improvements

These are some of the things which I believe could be done to make this little program more useful:   

* Check input for case sensitivity and common mistakes  
* Compatibility with more file formats beyond <code> .txt </code>  
* In case of multiple files with same name, possibility to choose appropriate file 
* Optional argument to read part of the content (i.e. a number of lines from the top or from a given position)
