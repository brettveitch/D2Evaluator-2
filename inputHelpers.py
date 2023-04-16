import os

availableCommands = {"evaluate","quit","clear","help"}
availableCommandShortcuts = {"e","q","c","h"}
assessedCharacters = {}

def commandFormat(commandString):
    return "(" + commandString[0].upper() + ")" + commandString[1:]

def getInputFromNumberedList(question, answerList):
    print(question)
    for i,answer in enumerate(answerList):
        print("  " + str(i + 1) + ") " + str(answer))
    return getIntInput("Type your selection here: ",1,len(answerList))

def getInputFromList(question, answerList):
    print(question)
    potentialAnswers = set()
    for answer in answerList:
        potentialAnswers.add(answer[0].lower())
        print("  " + commandFormat(answer))
    while(True):
        userInput = input("Type your selection here: ")
        if userInput[0].lower() in potentialAnswers:
            return userInput
        else:
            print("Not a valid option")

def addPostEvaluateCommands():
    global availableCommands
    global availableCommandShortcuts
    availableCommands = availableCommands.union({"find","trim"})
    availableCommandShortcuts = availableCommandShortcuts.union({"f","t"})

def getAssessedCharacter():
    print("Here are the following characters that are availble")
    for assessedCharacter in assessedCharacters.keys():
        print("  " + commandFormat(assessedCharacters[assessedCharacter].name))
    while(True):
        characterChoice = input("Type the first letter of the characters you'd like to assess: ").lower()
        isValidInput = ("h" in characterChoice or "t" in characterChoice or "w" in characterChoice or "q" in characterChoice)
        if isValidInput:
            return assessedCharacters[characterChoice]

def getIntInput(message,min = 1, max = 100):
    while(True):
        try:
            userInput = int(input(message))
        except:
            print("Not a number")
        else:
            if (userInput < min or userInput > max):
                continue
            return userInput

def getStatSet():
    statList = set()
    validStats = {"mobility","resilience","recovery","discipline","intellect","strength"}
    print("Type the full name of each stat you'd like to focus on (type s to stop)")
    while(True):
        potentialStat = input("Add stat: ")
        if potentialStat in validStats:
            statList.add(potentialStat)
        elif (len(statList) > 1 and potentialStat == "s") or len(statList) == 4:
            break
        else:
            print("Invalid input")
    return statList

def getCommand():
    commandList = "* - - - - - - - - - - - - - - - - - - - - - - * \nWhat would you like to do: \n"
    for command in availableCommands:
        commandList += "  " + "(" + command[0].upper() + ")" + command[1:] + "\n"
    print(commandList)
    currentCommand = input('\nEnter command: ').lower()
    if len(currentCommand) == 1 and currentCommand in availableCommandShortcuts:
        return currentCommand[0]
    if currentCommand in availableCommands:
        return currentCommand[0]
    else:
        return "i"

def getUserCharacter():
    while(True):
        characterChoice = input("Type the first letters of the characters you'd like to assess (H)unter, (W)arlock, (T)itan, or (C)ancel: ").lower()
        if "h" == characterChoice:
            return "Hunter"
        elif "t" == characterChoice:
            return "Titan"
        elif "w" == characterChoice:
            return "Warlock"
        elif "c" == characterChoice:
            return "cancel"
        elif len(characterChoice) > 1:
            print("Only type one letter")
        else:
            print("Not a valid character")

def getFileChoice():
    fileList = "I've detected the following compatible files:\n"
    count = 1
    choices = []
    #print(os.listdir(os.getcwd()+"/csv_folder"))
    for x in os.listdir(os.getcwd()+"/csv_folder"):
        if x.endswith(".csv"):
            choices.append(x)
            fileList += f"({count}) {x}\n"
            count += 1
    if (count == 1):
        input("\nNo file found.\n\nPress anything to quit...")
        return None
    elif (count == 2):
        return choices[0]
    print(fileList)
    fileChoice = -1
    fileNum = getIntInput("Type the number of the file: ")
    return choices[fileNum - 1]