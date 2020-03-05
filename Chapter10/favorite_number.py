import os
import json
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

filename = 'textFiles/fav_number.json'

def newFavoriteNumber():
    number = input("What is your favorite number? ")
    with open(filename,'w') as f:
        json.dump(number, f)

def getfavoriteNumber():
    filename = 'textFiles/fav_number.json'
    try:
        with open(filename) as f:
            number = json.load(f)
    except FileNotFoundError:
        return None
    else:
        return number
    
def guessNumber():
    number = getfavoriteNumber()
    if number:
        print(f"Your favorite number is {number}!")
    else:
        newFavoriteNumber()

guessNumber()