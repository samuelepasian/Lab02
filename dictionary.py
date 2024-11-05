import string


class Dictionary:

    def __init__(self):
        self.dizionario={}

    def append(self,key,value):
        self.dizionario[key]=value

    def addWord(self, frase):
        parole=frase.split()
        key=parole[0]
        value=""
        for parola in parole[1::]:
            value+=parola
        for chiave,val in self.dizionario.items():
            if chiave==key:
                value=val+" "+value
        self.dizionario[key]=value
        with open ("dictionary.txt",'w') as file:
            for c,v in self.dizionario.items():
                file.write(c+" "+str(v)+"\n")


    def translate(self,parola):
        if self.dizionario.get(parola) is not None:
            return self.dizionario[parola]
        raise ValueError(f"Parola non presente nel dizionario")


    def translateWordWildCard(self,parolaAliena):
        traduzioni=[ ]
        parolaAliena=parolaAliena.lower()
        count=-1
        stringa=""
        for i in range(len(parolaAliena)):
            if parolaAliena[i]=='?':
                count=i
        if count==-1:
            raise ValueError("Non hai inserito nessuna parola con carattere speciale ?")
        lettere=list(string.ascii_lowercase)
        for lettera in lettere:
            for key in self.dizionario.keys():
                parolaAliena= parolaAliena[:count]+lettera+parolaAliena[count+1:]
                if parolaAliena==key:
                    traduzioni.append(self.dizionario[key])
        for trad in traduzioni:
            stringa+=trad+" "
        return stringa[:-1]

