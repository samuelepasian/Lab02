import translator as tr
import dictionary as diz

t = tr.Translator()
d=diz.Dictionary()

def controllo(parola):
    for char in parola:
        if char.isdigit():
            raise ValueError("Non inserire numeri")
    parola=parola.lower()
    return parola

finito=True
while(finito):

    t.printMenu()

    a=t.loadDictionary("dictionary.txt")
    for key,value in a.items():
        d.append(key,value)

    txtIn = input()
    # Add input control here!

    if int(txtIn) == 1:
        print("Ok, quale parola devo aggiungere?")
        txtIn = input()
        txtIn = controllo(txtIn)
        d.addWord(txtIn)
        print("Aggiunta")
        print()
    elif int(txtIn) == 2:
        print("Ok, quale parola devo tradurre")
        txtIn=input()
        txtIn = controllo(txtIn)
        print("Traduzione: "+d.translate(txtIn))
        print()
    elif int(txtIn) == 3:
        print("Ok, quale parola devo tradurre")
        txtIn = input()
        txtIn=controllo(txtIn)
        print("Traduzione wild card: "+d.translateWordWildCard(txtIn))
        print()
    elif int (txtIn) == 4:
        print(d.dizionario)
        print()
    elif int(txtIn) == 5:
        finito=False

