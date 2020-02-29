import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
filename = 'textFiles/programming.txt'

# with open(filename, 'w') as file_object:
#     file_object.write("I Love Programming!\n")
#     file_object.write("I love creating new games!\n")

with open(filename, 'a') as file_object:
    file_object.write("I also love finding meaning in large datasets!\n")
    file_object.write("I love creating apps that can run in a browser!\n")

