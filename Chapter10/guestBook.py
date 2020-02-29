import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
filename = 'textFiles/guest_book.txt'

name = ""
exitFlag = ""
while (exitFlag != 'no' and exitFlag != 'n'):
    name = input("Please enter your name: ")
    with open(filename, 'a') as file_object:
        file_object.write(name+'\n')
    exitFlag = input("would you like to add more names (yes/no)?")
