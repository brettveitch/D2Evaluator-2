from armor import Armor
from loadout import Loadout
import csv

doubleStatCombinations = (
    ("mobility","resilience"),
    ("mobility","recovery"),
    ("mobility","discipline"),
    ("mobility","intellect"),
    ("mobility","strength"),

    ("resilience","mobility"),
    ("resilience","recovery"),
    ("resilience","discipline"),
    ("resilience","intellect"),
    ("resilience","strength"),

    ("recovery","resilience"),
    ("recovery","mobility"),
    ("recovery","discipline"),
    ("recovery","intellect"),
    ("recovery","strength")
)
tripleStatCombinations = (
    ("mobility","resilience","discipline"),
    ("mobility","resilience","intellect"),
    ("mobility","resilience","strength"),
    ("mobility","recovery","discipline"),
    ("mobility","recovery","intellect"),
    ("mobility","recovery","strength"),

    ("mobility","discipline","intellect"),
    ("mobility","discipline","strength"),
    ("mobility","intellect","strength"),
    
    ("resilience","recovery","discipline"),
    ("resilience","recovery","intellect"),
    ("resilience","recovery","strength"),
    ("resilience","discipline","intellect"),
    ("resilience","discipline","strength"),
    ("resilience","intellect","strength"),
    
    ("recovery","discipline","intellect"),
    ("recovery","discipline","strength"),
    ("recovery","intellect","strength")
)
quadStatCombinations = (
    ("mobility","resilience","discipline","intellect"),
    ("mobility","resilience","discipline","strength"),
    ("mobility","resilience","intellect","strength"),

    ("mobility","recovery","discipline","intellect"),
    ("mobility","recovery","discipline","strength"),
    ("mobility","recovery","intellect","strength"),

    ("resilience","recovery","discipline","intellect"),
    ("resilience","recovery","discipline","strength"),
    ("resilience","recovery","intellect","strength"),
    
)
allCombos = (doubleStatCombinations, tripleStatCombinations, quadStatCombinations)

class Character():
    def __init__(self, classType):
        self.name = classType
        self.armor = {"helmets":[], "gauntlets":[], "chestplates":[], "boots":[]}
        self.exoticArmor = {"helmets":[], "gauntlets":[], "chestplates":[], "boots":[]}
        self.allLoadouts = set()
        self.bestLoadouts = {}
        self.bestArmorPieces = set()
    
    def getCombinations(self):
        return len(self.armor["helmets"])*len(self.armor["gauntlets"])*len(self.armor["chestplates"])*len(self.armor["boots"])
    
    def getBestLoadout(self,statSet):
        for combo in self.bestLoadouts.keys():
            if set(combo) == statSet:
                return self.bestLoadouts[combo]

    def extractArmorFromCSV(self, filename):
        importantIndices = [0,2,4,24,25,26,27,28,29,30,31]
        with open("csv_folder/"+filename, newline='') as csvfile:
            spamreader = csv.reader(csvfile, delimiter=',', quotechar='"')
            for row in spamreader:
                tier, armorType, classType = row[4], row[5], row[7]
                importantStats = [row[i] for i in importantIndices]
                if classType == self.name:
                    if tier == "Legendary":
                        dictToAdd = self.armor
                    else:
                        dictToAdd = self.exoticArmor
                    if armorType == "Helmet":
                        dictToAdd["helmets"].append(Armor(*importantStats))
                    elif armorType == "Gauntlets":
                        dictToAdd["gauntlets"].append(Armor(*importantStats))
                    elif armorType == "Chest Armor":
                        dictToAdd["chestplates"].append(Armor(*importantStats))
                    elif armorType == "Leg Armor":
                        dictToAdd["boots"].append(Armor(*importantStats))
                    


    def loadArmor(self):

        # Fill bestLoadouts dictionary with first loadout as best for everything
        for double in doubleStatCombinations:
            self.bestLoadouts[double] = Loadout(self.armor["helmets"][0], self.armor["gauntlets"][0],self.armor["chestplates"][0],self.armor["boots"][0])
        for triple in tripleStatCombinations:
            self.bestLoadouts[triple] = Loadout(self.armor["helmets"][0], self.armor["gauntlets"][0],self.armor["chestplates"][0],self.armor["boots"][0])
        for quad in quadStatCombinations:
            self.bestLoadouts[quad] = Loadout(self.armor["helmets"][0], self.armor["gauntlets"][0],self.armor["chestplates"][0],self.armor["boots"][0])
        
        for h in self.armor["helmets"]:
            for g in self.armor["gauntlets"]:
                for c in self.armor["chestplates"]:
                    for b in self.armor["boots"]:
                        tempLoadout = Loadout(h, g, c, b)
                        self.allLoadouts.add(tempLoadout)
                        for comboNum in allCombos:
                            for combo in comboNum:
                                if tempLoadout.noWastedStats(threshold = 105):
                                    if tempLoadout.getCustomStatTotal(combo) > self.bestLoadouts[combo].getCustomStatTotal(combo):
                                        self.bestLoadouts[combo] = tempLoadout
        
        for bestLoadout in self.bestLoadouts.keys():
            for armorPiece in self.bestLoadouts[bestLoadout].armorList:
                self.bestArmorPieces.add(armorPiece)
        print(f"\nThere are {len(self.bestArmorPieces)} ideal pieces of armor. {87 - len(self.bestArmorPieces)} armor pieces are used in multiple builds")




            



