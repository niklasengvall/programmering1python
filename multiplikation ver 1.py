#!/usr/local/bin/python3.7                          
# Filnamn: multiplikation ver 1.py
# Kodexempel, lärobok sid. 49-50

print('Multiplikation')                                 # Skriver ut programmets rubrik
print('==============\n')                               # 
tal1 = int(input('Ange ett heltal: '))                  # Frågar användaren efter två heltal
tal2 = int(input('Och ett heltal till: '))              # int omvandlar sträng till heltal
prod = tal1 * tal2                                      # Beräknar produkten och resultatet hamnar i prod
print('Produkten av', tal1, 'och', tal2, 'blir', prod)  # SKriver ut resultatet av multiplikationen
                                                        # Vi blandar sträng och numerisk utskrift i printsatsen
                                                        