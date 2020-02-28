import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
filename = 'textFiles/learning_python.txt'

with open(filename) as file_object:
    print(file_object.read())
    
with open(filename) as file_object:
    for line in file_object:
        print(line)

with open(filename) as file_object:
    lines = file_object.readlines()

strang = ""
for line in lines:
    strang += line
print(strang.replace('Python', 'C++'))


