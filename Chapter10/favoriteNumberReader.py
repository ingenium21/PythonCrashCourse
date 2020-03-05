import json
import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

filename = 'textFiles/fav_number.json'

with open(filename) as f:
    number = json.load(f)

print(f"Your favorite number is {number}!")