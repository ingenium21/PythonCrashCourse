import json
import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

#Load the username, if it has been stored previously.
#Otherwise, prompt for the username and store it
def getStoredUsername():
    filename = 'textFiles/username.json'
    try:
        with open(filename) as f:
            username = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return username

def getNewUsername():
    #prompt for a new Username
    filename = 'textFiles/username.json'
    username = input("What is your name? ")
    with open(filename, 'w') as f:
        json.dump(username, f)
    return username

def greetUser():
    #greet user by name
    username = getStoredUsername()
    if username:
        quest = input(f"Are you {username}(y/n)? ")
        if quest == "y":
            print(f"Welcome back, {username}!")
        else:
            username = getNewUsername()
            print(f"We'll remember you when you come back, {username}!")
    else:
        username = getNewUsername()
        print(f"We'll remember you when you come back, {username}!")

greetUser()