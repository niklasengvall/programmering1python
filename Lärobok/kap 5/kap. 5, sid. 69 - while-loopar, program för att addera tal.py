#!/usr/local/bin/python3.9

# Filnamn: kap. 5, sid. 69 - while-loopar, program för att addera tal.py

# Kapitel 5 - Loopar - upprepning, itteration
# Programmering 1 med Python - Lärobok

# Program för att addera tal

while 1: # answerätt tills användaren bryter
    c = int(input('Ange antal tal du vill du addera? '))
    tot = 0 # Talsumman sätts till noll från början
    
    for i in range(1, c + 1):
        num = float(input('ange tal ' + str(i) + ': ')) # Fråga efter tal
        tot += num # Öka summan med det inmatade talet
    
    print('Summan av talen är {:.1f}'.format(tot))
    print('och medelvärdet är {:.1f}'.format(tot / c))
    
    answer = input('\nVill du göra mer beräkningar (J/N)? ')
    if answer == 'N' or answer == 'n':
        break # Avbryt loopen 

print('Ok, välkommen åter!')