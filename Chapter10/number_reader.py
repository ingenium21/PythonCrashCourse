import os
import json
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

filename = 'textFiles/numbers.json'
with open(filename) as f:
    numbers = json.load(f)

print(numbers)