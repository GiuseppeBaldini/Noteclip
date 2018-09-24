# Noteclip

Noteclip is a simple Python program to retrieve notes directly in the clipboard using the Pyperclip module. 

### Why is it useful?

Noteclip can be used to store medium/long pieces of information that can be kept in plaintext. 

Examples include:

1. Frequently used / public contact information 

2. Email / Messages templates for different situations

3. Temporary useful stuff you usually keep on Sticky Notes

**I do not recommend to use this program to retrieve extremely sensitive information such as:**

* Identification documents (Passport info, Social Security Number etc.)

* Bank details (Account information, card information etc.)

* Passwords and other secturity details

### What is needed?

* Text files with the information to retrieved, named appropriately (e.g. "work_address.txt")

* Modules **sys**, **os** and **pyperclip** 

* Pyhton program which can be found in this repo

* Batch file to automate the execution of the program directly from the "Run" command

### How does it work? 

Assuming to work on Windows, the program would work as follow:

1. Type **Win + R** and insert the name of the file where your needed information is stored

2. The content of the file is read and **copied in the clipboard** using the Pyperclip module

3. **Paste**. Done.
