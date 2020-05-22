import csv

class Atom:
    def __init__(self, name, weight, valence):
        self.weight = weight
        self.valence = valence
        self.name = name
        self.freeElectrons = valence

def findAtomInTable(inputText):
    with open('periodicTable.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for row in csv_reader:
            if row[1] == inputText or row[2] == inputText:
                atom = Atom(row[1], row[0], row[27] if row[27] != "" else 0)
                return atom

stuff = []

while (True):
    print("")
    inputAtom = input("Enter an atom name ")
    stuff.append(findAtomInTable(inputAtom))
    print("")
    print("Stuff in system:")
    for a in stuff:
        for b in stuff:
            if a != b:
                if int(a.freeElectrons) > 0 and int(b.freeElectrons) > 0:
                    print ("molecule made from " + a.name + " and " + b.name)
                    a.freeElectrons = int(a.freeElectrons) - 1
                    b.freeElectrons = int(b.freeElectrons) - 1
        print (a.name + " " + str(a.freeElectrons))