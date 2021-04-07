#!/usr/local/bin/python3.9

# Filnamn: övn 14.6, sid. 38 - datorn gissar ett tal.py

# Sökning
# Programmeringsövningar till kapitel 14

# Programmet låter dig tänka på ett tal mellan 1 och 99. 
# Första gången gissar datorn på talet i mitten utifrån det givna intervallet 1 
# till 99. Dvs. talet 50. Svarar användaren at det är för högt 
# gissar dator på nedre halvans mitt, dvs 25, sedan tillfrågas användaren igen.
# 

# Import av modul
from random import randint

# Funktionsdefinitioner
def binGissning(ngräns, ögräns):
    return (ögräns - ngräns) // 2

# Huvudprogram
def main():

    # Variabeldeklarationer och initieringar
    # Talet som datorn tror människan tänker på
    talMänniska = 0
    
    # Antal gissningar som datorn gjort
    gissningar = 1

    # Talgränser
    nedre = 1
    övre = 100

    # Svar som ska anges av användaren
    svar = ''
    # Skriv ut en programrubrik
    print('Jag gissar vilket tal du tänker på') 
    print('==================================\n')
    print('Får jag be dig att tänka på ett tal mellan 1 och 100.')

    # Gissa i mitten av talgränserna
    talMänniska = binGissning(nedre, övre)
    
    # Skriv ut gissningen
    print('Jag gissar att du tänker på talet ' + str(talMänniska) + '.')

    # Fråga användaren om det är rätt, för högt eller lågt   
    svar = input('Är det [r]ätt, för [h]ögt eller [l]ågt: ')
    while svar not in ['r', 'rätt']:
        if svar in ['h', 'högt']:
            övre = talMänniska - 1
            oldtal = talMänniska
            talMänniska -= binGissning(nedre, övre)
            if oldtal == talMänniska:
                talMänniska -= 1

        if svar in ['l', 'lågt']:
            nedre = talMänniska + 1
            oldtal = talMänniska
            talMänniska += binGissning(nedre, övre)
            if oldtal == talMänniska:
                talMänniska += 1

        # Öka antal gissningar
        gissningar += 1

        # Skriv ut gissningen
        print('Jag gissar att du tänker på talet ' + str(talMänniska) + '.')

        # Och fråga användaren återigen om det är rätt, för högt eller lågt
        svar = input('Är det [r]ätt, för [h]ögt eller [l]ågt: ')

    print('Jag gissat rätt efter ' + str(gissningar) + ' försök.')
    
# Huvudprogram anropas 
main()