#!/usr/local/bin/python3.7                          
# Filnamn: multiplikation ver 2.py
# Kodexempel, lärobok sid. 49-50

print('Multiplikation')                                 # Skriver ut programmets rubrik
print('==============\n')                               # 
tal1 = int(input('Ange ett heltal: '))                  # Frågar användaren efter två heltal
tal2 = int(input('Och ett heltal till: '))              # int omvandlar sträng till heltal
prod = tal1 * tal2                                      # Beräknar produkten och resultatet hamnar i prod
print('Produkten av ' + str(tal1) + ' och ' + str(tal2) + ' blir ' + str(prod))
# Vi har bara stränguttryck i print-satsen, vilket snabbar upp utskriftshanteringen