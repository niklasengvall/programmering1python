#!/usr/bin/python3

# Filnamn: while-loopar, program för att addera tal, kap. 5, sid. 69.py

# Program för att addera tal

while True: # fortsätt tills användaren bryter
    antal = int(input('Hur många tal vill du addera? '))
    summa = 0 # Talsumman sätts till noll från början
    
    for i in range(1, antal + 1):
        tal = float(input('ange tal ' + str(i) + ': ')) # Fråga efter tal
        summa += tal # Öka summan meddet inmatade talet
    
    print('Summan av inmatade tal är {:.2f}'.format(summa))
    print('och medelvärdet är {:.2f}'.format(summa / antal))
    
    forts = input('\nVill du göra fler beräkningar (J/N)? ')
    if forts == 'N' or forts == 'n':
        break # Avbryt loopen 

print('Ok, tack för idag!')