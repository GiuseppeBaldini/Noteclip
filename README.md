# Noteclip

Noteclip is a simple Python program to retrieve notes directly in the clipboard using the Pyperclip module. 

### Introduction

Given an <code>argument</code>, the program does 2 things:

1. Searches (bottom-up) for <code>argument.txt</code> and returns its filepath

2. Copies the content of <code>argument.txt</code> in the clipboard so it's ready to be pasted

### Use cases

Noteclip can be used to store medium/long pieces of information that can be kept in plaintext. 

Examples include:

1. Frequently used / public contact information 

2. Email / Messages templates for different situations

3. Temporary useful stuff you usually keep on Sticky Notes

**I do not recommend to use this program to retrieve extremely sensitive information such as:**

* Identification information (Passport number, Social Security Number etc.)

* Bank details (Account information, card information etc.)

* Passwords and other secturity details

### Preparation

1. Create notes as .txt files

2. Install **pyperclip** 

3. Assign <code>notes_path</code> variable to highest level folder where all your notes are*

4. Change filepath in Batch file to reflect location of the program on your computer  
    
\* **NOTE**: _Using a path too broad makes the scan too slow.  I would suggest keeping everything at least 3 levels below C:\ _

### Execution from Run command

I included a batch file to run the program directly from the Run window.  
All I need to do now is use the shortcut <code> Win + R</code> to open the Run window and the type <code> noteclip [note name] </code>. 

### Limitations


