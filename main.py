from helperCommands import *
from inputHelpers import getCommand

clear()

def runProgram():
    while(True):
        command = getCommand()
        if command == "q":
            break
        if command == "c":
            clear()
        if command == "e":
            evaluate()
        if command == "h":
            helpMenu()
        if command == "f":
            find()
        if command == "i":
            invalid()
        if command == "t":
            trim()

runProgram()