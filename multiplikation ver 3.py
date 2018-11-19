#!/usr/bin/python3                         
# Filnamn: multiplikation ver 3.py
# Kodexempel, lärobok sid. 49-50

print('Multiplikation')                                 # Skriver ut programmets rubrik
print('==============\n')                               # 
tal1 = int(input('Ange ett heltal: '))                  # Frågar användaren efter två heltal
tal2 = int(input('Och ett heltal till: '))              # int omvandlar sträng till heltal
prod = tal1 * tal2                                      # Beräknar produkten och resultatet hamnar i prod
print('Produkten av {} och {} blir {}'.format(tal1, tal2, prod))
# Formaterad utskrift tar längst tid at skriva ut