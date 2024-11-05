import dictionary as diz

class Translator:

    def __init__(self):
        pass

    def printMenu(self):
        # 1. Aggiungi nuova parola
        # 2. Cerca una traduzione
        # 3. Cerca con wildcard
        # 4. Exit
        print("1. Aggiungi nuova parola")
        print("2. Cerca una traduzione")
        print("3. Cerca con wildcard")
        print("4. Stampa dizionario")
        print("5. Exit")

    def loadDictionary(self, dict):
        # dict is a string with the filename of the dictionary
        diz={}
        valore=""
        with open(dict, 'r') as file:
            righe=file.readlines()
        i=0
        while i<len(righe):
            valore=""
            parole=righe[i].split()
            chiave=parole[0]
            for parola in parole[1::]:
                valore+=parola+" "
            diz[chiave]=valore[:-1]
            i+=1
        return diz

    def handleAdd(self, entry):
        # entry is a tuple <parola_aliena> <traduzione1 traduzione2 ...>
        pass

    def handleTranslate(self, query):
        # query is a string <parola_aliena>
        pass

    def handleWildCard(self,query):
        # query is a string with a ? --> <par?la_aliena>
        pass