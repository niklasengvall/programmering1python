#!/usr/local/bin/python3.9

# Filnamn: övn 6.10 - översätta från rövarspråk - kap. 6, sid. 17.py

# Mer om teckensträngar i Python
# Programmeringsövningar till kapitel 6

# Programmet läser in en mening från användaren och översätter den sedan från
# rövarspråket till svenska.

# Låt användaren mata in en sträng på rövarspråket
mening = input('Ange en mening på rövarspråket: ')

# Konvertera den inmatade meningen till stora bokstäver för att minska antal
# jämförelser
attÖversätta = mening.upper()

# Sträng med alla konsonanter som används vid jämförelse mot den VERSALA 
# meningen i strängen attÖversätta
konsonanter = 'BCDFGHJKLMNPQRSTVWXZ'

# Används av systemet för att se om konsonant hittats
hittat = False
# Initiera en ny sträng som ska lagra svenskan
nyMening = ''
i = 0

# Yttre loopför att gå igenom alla tecken som finns i meingen
while i < len(attÖversätta):
    # Inre loop för att testa varje tecken i meningen om det är en konsonant
    for konsonant in konsonanter:
        # Om tecknet är en konsonant lägg in konsonant och hoppa över 2 tecken
        if attÖversätta[i] == konsonant:
            # Test om det är korrekt rövarspråk, dvs konsonant + o + konsonant
            if attÖversätta[i + 1] == 'O' and attÖversätta[i + 2] == konsonant:
                # Spara konsonant i nya meningen
                nyMening += attÖversätta[i]
                i += 3 # i rövarspråkssträngen så hoppar vi över nästkommande 
                # o + konsonant
                hittat = True # Tala om at vi hittat en konsonant
                break # Om konsonant hittats sluta leta efter fler
            else:
                print('Det som skrivits in, utgör inte ett korrekt rövarspråk!')
                exit()
        
    # Om konsonant hittats spara inget tecken det är redan gjort annars spara
    # vokalen och tala om att vi ska undersöka nästa tecken genom att öka index 
    # med ett
    if hittat:
        hittat = False
        pass
    else:
        nyMening += attÖversätta[i]
        hittat = False
        i += 1

# Ändra den nya meningen till Inlednade stor bokstav
nyMening = nyMening.capitalize()

# Skriv ut den nya meningen
print('\nBlir på svenska: \n\n' + nyMening)