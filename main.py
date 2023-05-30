from helperCommands import *
from inputHelpers import getCommand

clear()
print("Welcome to Destiny 2 Armor Trimmer!\n")

commands = {
    "c": clear,
    "e": evaluate,
    "h": helpMenu,
    "f": find,
    "t": trim,
    "i": invalid,
    "q": quit
}

def runProgram():
    running = True
    while(running):
        running = commands[getCommand()]()

runProgram()