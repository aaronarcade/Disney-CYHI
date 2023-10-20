class BrainzTranslator:
    def __init__(self):
        self.brainCount = 0
        self.groans = ""
        self.zombieMoves = {
            "Start epidemic": self.start_epidemic,
            "Infect person": self.infect_person,
            "Check number of infections": self.check_infections,
            "Bulk deinfect": self.bulk_deinfect,
            "Develop vaccine": self.develop_vaccine
        }

    def start_epidemic(self):
        self.brainCount = 0

    def infect_person(self):
        self.brainCount += 1

    def check_infections(self):
        self.groans += chr(self.brainCount)

    def bulk_deinfect(self):
        self.brainCount = 0

    def develop_vaccine(self):
        self.groans = self.groans[:-1]

    def amplify_bite(self):
        self.zombieMoves["Infect person"] = self.infect_person

    def chant(self, necroScript):
        for spell in necroScript:
            if spell in self.zombieMoves:
                self.zombieMoves[spell]()
            elif spell == "Add Infect person":
                self.amplify_bite()
        return self.groans

def main():
    darkWizard = BrainzTranslator()

    with open('contagion.txt', 'r') as necronomicon:
        evilSpells = necronomicon.readlines()

    if False:#(not evilSpells or evilSpells[0].strip() != "Start epidemic") or ("Develop vaccine" not in [curse.strip() for curse in evilSpells]):
        print("Zombies feasted on your brains!")
        return  # End the end times

    necroScript = [curse.strip() for curse in evilSpells]
    print(darkWizard.chant(necroScript))

if __name__ == "__main__":
    main()
