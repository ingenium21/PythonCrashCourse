import json
import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

#Load the username, if it has been stored previously.
#Otherwise, prompt for the username and store it

filename = 'textFiles/username.json'

try:
    with open(filename) as f:
        username = json.load(f)

except FileNotFoundError:
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
        print(f"We'll remember you when you come back, {username}!")

else:
    print(f"Welcome back, {username}!")