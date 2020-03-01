import json
import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

numbers = [2,3,5,7,11,13]
filename = 'textFiles/numbers.json'

with open(filename, 'w') as f:
    json.dump(numbers,f)