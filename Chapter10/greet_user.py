import json
import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)

filename = 'textFiles/username.json'

with open(filename) as f:
    username = json.load(f)
    print(f"Welcome back, {username}!")