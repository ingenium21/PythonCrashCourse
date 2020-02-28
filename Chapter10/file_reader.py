import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
filename = 'textFiles/pi_million_digits.txt'
with open(filename) as file_object:
    lines = file_object.readlines()

pi_string = ""
for line in lines:
    pi_string += line.strip()

#print(f"{pi_string[:52]}...")
#print(len(pi_string))

birthday = input("Enter your birthday, in the form mmddyy: ")
if birthday in pi_string:
    print("Your birthday appears in the first million digits of pi!")
else:
    print("Your birthday does not appear in the first million digits of pi :'(")