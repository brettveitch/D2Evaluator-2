class Loadout():
    def __init__(self, helmet, gauntlet, chestplate, boot):
        self.armorList = [self.helmet, self.gauntlet, self.chestplate, self.boot] = [helmet, gauntlet, chestplate, boot]
        self.stats = {"mobility":2, "resilience":2, "recovery":2, "discipline":2, "intellect":2, "strength":2}
        for armor in self.armorList:
            for stat in armor.stats.keys():
                self.stats[stat] += armor.stats[stat]

    def noWastedStats(self, threshold = 105):
        for stat in self.stats.keys():
            if self.stats[stat] > threshold:
                return False
        return True
    
    def getArtificeCount(self):
        count = 0
        for a in self.armorList:
            if a.artifice:
                count += 1
        return count
    
    # Returns total based on given stats. Includes artifice +3 per armor
    def getCustomStatTotal(self, stats):
        total = 0
        for armor in self.armorList:
            total += armor.getCustomStatTotal(stats)
        return total
    
    # Will slot artifice to maximize tiers
    def getCustomMaxTierTotal(self, stats):
        artificeCount = self.getArtificeCount()
        tiers = 0
        for stat in stats:
            tiers += self.stats[stat]//10
            if artificeCount > 0 and self.stats[stat]%10 > 6:
                tiers += 1
                artificeCount -= 1
        return tiers

    def getDimQuery(self):
        output = ""
        for armor in self.armorList:
            output += armor.__str__() + " or "
        return output[:-4]
    
    def __str__(self):
        output = ""
        for armor in self.armorList:
            output += f"{armor.stats} | {armor.name} ({armor.id}) \n"
        output += f"{self.stats} | Total"
        output += f"\n{self.getDimQuery()}\n"
        return output




    """
    def getTotalStats(self, masterWorked = True):
        return sum(self.getStats(masterWorked)) + self.getArtificeBonus()
    
    def getArtificeBonus(self):
        bonus = 0
        for a in self.armorList:
            if a.artifice:
                bonus += 3
        return bonus
    
    """