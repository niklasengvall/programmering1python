#!/usr/local/bin/python3.9

# Filnamn: övn 6.9 - översätta till rövarspråket - kap. 6, sid. 16.py

# Mer om teckensträngar i Python
# Programmeringsövningar till kapitel 6

# Programmet läser in en mening från användaren och översätter den sedan till 
# rövarspråket. genom att infoga bokstaven o + konsonant vid varje konsonantställe i texten.

# Låt användaren mata in en sträng på svenska
mening = input('Ange en mening på svenska: ')

# Konvertera den inmatade meningen till stora bokstäver för att minska antal
# jämförelser
attÖversätta = mening.upper()

# Sträng med alla konsonanter som används vid jämförelse mot den VERSALA 
# meningen i strängen attÖversätta
konsonanter = 'BCDFGHJKLMNPQRSTVWXZ'

# Initiera en ny sträng som ska lagra rövarspråket
nyMening = ''

# Yttre loopför att gå igenom alla tecken som finns i meingen
for tecken in attÖversätta:
    # Inre loop för att testa varje tecken i meningen om det är en konsonant
    for konsonant in konsonanter:
        # Om tecknet är en konsonant lägg in konsonant + o  
        if tecken == konsonant:
            nyMening += tecken + 'O'
            break # Om konsonant hittats sluta leta efter fler

    # Omingen konsonant hittades lägg till vokalen, eller 
    # avsluta med samma konsonant igen då rövarspråk kräva så
    nyMening += tecken

# Ändra den nya meningen till Inlednade stor bokstav
nyMening = nyMening.capitalize()

# Skriv ut den nya meningen
print('\nBlir på rövarspråket: \n\n' + nyMening)