#!/usr/local/bin/python3.9

# Filnamn: övn 14.2, sid. 36 - söka tal med funktion.py

# Sökning
# Programmeringsövningar till kapitel 14

# Programmet slumpar först fram ett tal mellan 1 och 99 och lagrar det talet. 
# Därefter frågar datorn användaren vilke tal datorn tänker på och användaren 
# får gissa tills han/hon gissat rätt och då får man även reda på hur många 
# gissningar man gjort. Om användaren gissar ett för lågt tal så sägger datorn 
# att det är för lågt och för högt om det är tvärs om.

# Import av modul
from random import randint

# Funktionsdefinitioner

# Huvudprogram
def main():

    # Variabeldeklarationer och initieringar
    # Talet som datorn tänker på
    talDator = randint(1,100)
    # Antal gissningar som användaren gjort
    gissningar = 1

    # Skriv ut en programrubrik
    print('Gissa vilket tal jag tänker på') 
    print('==============================\n')

    # Fråga användaren vilket tal datorn tänker på 
    talAnvändare = int(input('Vilket tal tänker jag på? ')) 
    while talDator != talAnvändare:
        # Beroende på om användarens gissade tal  är för högt eller lågt
        # i förhållande till vad datorn tänker på för tal,skriv ut en ledtråd
        if talAnvändare > talDator:
            print('För högt!')
        else:
            print('För lågt!')
        # Öka antal gissningar
        gissningar += 1
        # Låt användaren gissa på ett nytt tal
        talAnvändare = int(input('Vilket tal tänker jag på? ')) 

    print('Rätt gissat på ' + str(gissningar) + ' försök.')
    
## Huvudprogram anropas 
main()