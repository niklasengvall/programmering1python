#!/usr/local/bin/python3.9

# Filnamn: övn 15.4, sid. 39 - instickssortering.py

# Sortering
# Programmeringsövningar till kapitel 15

# Programmet skapar först upp en kortlek med 52 kort och där korten är 
# slumpmässigt placerade. Därefter utförs instickssortering med sorterings-
# ordning enligt hjärter, ruter, klöver och spader, där ess är 1 och kung är 13


# Import av modul
from random import randint, randrange # För att slumpa tal
from time import perf_counter

# Funktionsdefinitioner
def fixaNyKortlek(f,v,lista):
    # Skapa upp en sorterad kortlek för att se vilka kort vi använt vid 
    # generering av slumpad kortlek
    # sorterad_kortlek = alla kort
    # sorterad_kortlek[0] = (1, 'Hjärter', 1, 'Ett')
    # sorterad_kortlek[0][0] = 1
    # sorterad_kortlek[0][1] = 'Hjärter'
    # sorterad_kortlek[0][2] = 1
    # sorterad_kortlek[0][3] = 'Ett' 
    for j in range(len(f)):
        for i in range(len(v)):
            lista.append(f[j] + v[i])
    return lista

def skapaSlumpadKortlek(korthög, slumpadeKort):
    # Skapa upp en slumpad kortlek
    # Vi slumpar fram ett tal mellan 0 och längden på sorterad kortlek
    # Vi tar sedan kortet som slumpats från sorterad_kortlek[slumptal] och 
    # lägger det i slumpad_kortlek[i] och upprepar tills det inte längre finns
    # några kort kvar i sorterad_kortlek
    while len(korthög):
        slumptal = randint(0, len(korthög)-1)
        slumpadeKort.append(korthög[slumptal])
        del korthög[slumptal] #Tar bort 
    return slumpadeKort

def insticksSortering(lista):
    listansLängd = len(lista)

# Huvudprogram
def main():
    # Variabeldeklarationer
    Färger = ['Hjärter', 'Ruter', 'Klöver', 'Spader']
    Valörer = ['Ett', 'Två', 'Tre', 'Fyra', 'Fem', 'Sex', 'Sju', 'Åtta', 'Nio',
               'Tio', 'Knekt', 'Dam', 'Kung']

    sorterad_kortlek = []
    slumpad_kortlek = []

    # Skapa enumrerade listobjekt av färger och valörer. blir då enkelt att räkna
    f = list(enumerate(Färger,1))
    v = list(enumerate(Valörer,1))
    
    # Skapa upp en sorterad kortlek för att se vilka kort vi använt vid 
    sorterad_kortlek = fixaNyKortlek(f,v, sorterad_kortlek)

    # Skapa upp en slumpad kortlek
    slumpad_kortlek = skapaSlumpadKortlek(sorterad_kortlek, slumpad_kortlek)    
    print(slumpad_kortlek)

    #Insticksortera efter färgerna hjärter 1, ruter 2, klöver 3, spader 4
    index = 0
    while(index < len(slumpad_kortlek)-1):
        bytt_plats = False
        if(slumpad_kortlek[index][0] > slumpad_kortlek[index + 1][0]): # om draget kort har högre färgvalör än nästa kort
            temp_kort = slumpad_kortlek[index]
            del(slumpad_kortlek[index]) # Ta bort kortet och då blir nästa kort på index pos
            slumpad_kortlek.insert(index + 1, temp_kort) # och lägg det efter nästa kort
            index = 0
            bytt_plats = True
        if(not bytt_plats): index += 1

    #Insticksortera efter valörerna 1-3 för alla färger
    # Hjärter börjar på index 0, ruter på 13, klöver på 26, spader på 39
    index = 0
    while(index < 4): # Gå igenom alla kort
        bytt_plats = False
        if(slumpad_kortlek[0][index] > slumpad_kortlek[0][index + 1]): # om draget kort har högre färgvalör än nästa kort
            temp_kort = slumpad_kortlek[index] # Göras om
            del(slumpad_kortlek[index]) # Ta bort kortet och då blir nästa kort på index pos
            slumpad_kortlek.insert(index + 1, temp_kort) # och lägg det efter nästa kort
            index = 0
            bytt_plats = True
        if(not bytt_plats): index += 1

    print("Efter färgsortering")
    print(slumpad_kortlek)


#    antal = int(input('Hur många tal vill du sortera? '))

    # Sortera en lista med antal tal som är slumpade mellan 0 och 4 294 967 292 
#    lista = [randint(0, 4294967292) for i in range(antal)]
    #print("Före: ", lista)
#    start = perf_counter()
#    combsort(lista)
#    end = perf_counter()
    #print("Efter: ", lista)
#    print('Att sortera {:d} heltal tog {:f} sekunder med egen comsort-funktion'.format(antal, end - start))

    # Sortera med Pythons inbyggda funktion
#    lista = [randint(0,4294967292) for i in range(antal)]
#    start = perf_counter()
    # Sortera listan på plats
#    lista.sort()
#    end = perf_counter()
#    print('Att sortera {:d} heltal tog {:f} sekunder med inbyggd sorteringsfunktion'.format(antal, end - start))

# Huvudprogram anropas 
main()