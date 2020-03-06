import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
from name_function import getFormattedName

print("Enter 'q' at any time to quit")
while True:
    first = input("\nplease give me a first name: ")
    if first == 'q':
        break
    last = input("\nPLease give me a last name: ")
    if last == 'q':
        break

    formattedName = getFormattedName(first, last)
    print(f"\nNeatly formatted name: {formattedName}")