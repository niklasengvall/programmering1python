#!/usr/local/bin/python3.9

# Filnamn: övn 13.2, sid. 32 - rekursiv omvandling dec till bin.py

# Rekursion- Funktioner som anropar sig själva
# Programmeringsövningar till kapitel 13

# Programmet omvandlar ett decimalt tal till en binär sträng med hjälp av en 
# rekursiv funktion

# Funktionsdefinitioner
def decToBinStr(decimal, lista):
    if decimal > 0:      
        # Lagra 1 om det är ett udda tal
        # Lagra 0 om det är ett jämt tal
        lista.append(decimal % 2)
        # Anropa funktionen rekursivt,
        # heltalsdividera talet med 2 och skicka med referens till lista
        return decToBinStr(decimal // 2, lista) 

# Huvudprogram
def main():
    binStr = ''
    binaryList = []
    # Be användaren matat in ett heltal
    number = int(input('Skriv in ett heltal: '))

    # Anropa den rekursiva funktionen 
    decToBinStr(number, binaryList)
    # Vänd på listans innehåll för at få det binära talet rätvänt 
    binaryList.reverse()
    
    # Omvandla listans ettor och nollor till en sträng och skriv ut den
    for c in range(len(binaryList)):
        binStr += str(binaryList[c])
    print(binStr)

## Huvudprogram anropas 
main()