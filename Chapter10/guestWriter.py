import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

filename = 'textFiles/guest.txt'
guest = input("Please type your name: ")
with open(filename, 'w') as file_object:
    file_object.write(guest+"\n")