class Armor():
    def __init__(self, name, id, tier, mobility, resilience, recovery, discipline, intellect, strength, total, source):
        self.name = name
        if (source == "artifice"):
            self.name += " (A)"
        self.id = id
        self.type = type
        self.isExotic = tier == "Exotic"
        self.stats = {"mobility":int(mobility)+2, "resilience":int(resilience)+2, "recovery":int(recovery)+2, "discipline":int(discipline)+2, "intellect":int(intellect)+2, "strength":int(strength)+2}
        self.total = int(total)
        self.artifice = source == "artifice"
    
    def __str__(self):
        return f"id:{self.id}"
    
    def getCustomStatTotal(self, stats):
        total = 0
        
        for stat in stats:
            total += self.stats[stat]

        if self.artifice:
            total += 3
        
        return total
