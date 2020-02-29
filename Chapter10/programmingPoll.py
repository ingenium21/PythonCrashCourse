import os
path = os.path.dirname(os.path.realpath(__file__))
os.chdir(path)
filename = 'textFiles/pollResults.txt'
exitFlag = ""
while(exitFlag != "no" and exitFlag != "n"):
    reason = input("Why do you love programming? \n")
    with open(filename,'a') as file_object:
        file_object.write(reason + "\n")
    exitFlag = input("Would you like to continue (yes/no): ")
