import os
from character import Character
from inputHelpers import *

armorInitials = {"h":"helmets", "g":"gauntlets", "c":"chestplates", "b":"boots"}

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

def helpMenu():
    print("This is the help menu. Congratulations")

def invalid():
    print("That was an invalid command")

def trim():
    selectedCharacter = getAssessedCharacter()
    print("Here is the set of armor pieces that make up all of your best builds.")
    output = ""
    for armor in selectedCharacter.bestArmorPieces:
        output += "id:" + armor.id + " or "
    print(f"\n{selectedCharacter.name} ids ({len(selectedCharacter.bestArmorPieces)}): \n" + output[:-4] + "\n")


def find():
    searchType = getInputFromList("Would you like to search for a loadout or armor piece?",["Loadout","Armor"])
    selectedCharacter = getAssessedCharacter()
    if searchType == "l":
        findLoadout(selectedCharacter)
    elif searchType == "a":
        findArmor(selectedCharacter)
    else:
        print("Bug: find shouldn't allow anything other than loadout and armor")

def findArmor(selectedCharacter):
    armorChoice = getInputFromList("What piece of armor would you like to search for?",["Helmet","Gauntlets","Chestplates","Boots"])
    focusedStats = getStatSet()
    
    listOfArmor = selectedCharacter.armor[armorInitials[armorChoice]]
    top5 = []
    for armorPiece in listOfArmor:
        indexToPlace = len(top5)
        for spot,topArmor in enumerate(top5):
            if armorPiece.getCustomStatTotal(focusedStats) > topArmor.getCustomStatTotal(focusedStats):
                indexToPlace = spot
                break
        top5.insert(indexToPlace,armorPiece)
    top5 = top5[:5]

    output = ""
    for a in top5:
        output += a.__str__() + " or "
    
    print(output[:-4])


def findLoadout(selectedCharacter):
    focusedStats = getStatSet()
    print(selectedCharacter.getBestLoadout(focusedStats))
    print(selectedCharacter.getBestLoadout(focusedStats).getCustomMaxTierTotal(focusedStats))

def evaluate():
    className = getUserCharacter()
    if className == "cancel":
        return
    selectedCharacter = Character(className)
    fileName = getFileChoice()
    selectedCharacter.extractArmorFromCSV(fileName)
    if input(f"\nThere are {selectedCharacter.getCombinations()} combinations. Okay to proceed? (y or n): ") == "n":
        return
    selectedCharacter.loadArmor()
    assessedCharacters[selectedCharacter.name[0].lower()] = selectedCharacter
    addPostEvaluateCommands()