class Dictionary:

    def __init__(self):
        self.dizionario={}

    def append(self,key,value):
        self.dizionario[key]=value

    def addWord(self, parola):
        self.dizionario[parola.split()[0]]=parola.split()[1]
        with open ("dictionary.txt",'a') as file:
            file.write( parola.split()[0]+" "+parola.split()[1]+"\n")

    def translate(self,parola):
        if self.dizionario.get(parola) is not None:
            return self.dizionario[parola]
        raise ValueError(f"Parola non presente nel dizionario")


    def translateWordWildCard(self):
        pass

