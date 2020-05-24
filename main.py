import csv

class Atom:
    def __init__(self, name, weight, valence, numShells):
        self.weight = int(weight)
        self.valence = int(valence)
        self.name = name
        self.freeElectrons = int(valence)
        self.molecule = None
        self.numShells = int(numShells)
        self.neededToBeFull = calculateFullnessRequirement(int(valence), int(numShells))

def calculateFullnessRequirement(valence, numShells):
    if numShells == 1:
        return 2
    if numShells == 2:
        return 8
    if numShells == 3:
        return 18
    if numShells == 4:
        return 32
    if numShells == 5:
        return 50



class Molecule:
    def __init__(self, description):
        self.description = description

def findAtomInTable(inputText):
    with open('periodicTable.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1] == inputText or row[2] == inputText:
                atom = Atom(row[1], row[0], row[27] if row[27] != "" else 0, row[26])
                return atom

atoms = []

molecules = []

while (True):
    print("")
    inputAtom = input("Enter an atom name ")
    atoms.append(findAtomInTable(inputAtom))
    print("")
    print("Atoms in system:")
    for a in atoms:
        for b in atoms:
            if a != b:
                if int(a.valence) < a.neededToBeFull and int(b.valence) < b.neededToBeFull:
                    molecule = ""
                    if a.molecule != None and b.molecule == None:
                        molecule = a.molecule + " and " + b.name
                    elif a.molecule == None and b.molecule != None:
                        molecule = b.molecule + " and " + a.name
                    elif a.molecule == None and b.molecule == None:
                        molecule = a.name + " and " + b.name
                    
                    if (molecule != ""):
                        a.molecule = molecule
                        b.molecule = molecule

                    a.valence = int(a.valence) + 1
                    b.valence = int(b.valence) + 1

        print (a.name + " with " + str(a.valence) + " outer shell electrons in a molecule of " + str(a.molecule) )

    