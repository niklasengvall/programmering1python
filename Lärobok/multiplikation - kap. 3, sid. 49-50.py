#!/usr/bin/python3

# Filnamn: multiplikation - kap. 3, sid. 49-50.py

# Programmet frågar användaren efter två faktorer och multiplicerar dessa 
# därefter visas resultatet på skärmen.

# Skriv ut programmets rubrik
print('Multiplikation')
print('==============\n')

# Fråga efter två tal som också omvandlas från sträng till int (heltal)
tal1 = int(input('Ange ett heltal: '))
tal2 = int(input('Och ett heltal till: '))

# Beräkna produkten av dessa två tal och placera resultatet i variabeln prod
prod = tal1 * tal2

# Skriv ut resultatet på skärmen (alt 1, långsamare metod)
print('Produkten av', tal1, 'och', tal2, 'blir', prod)

# Skriv ut resultatet på skärmen (alt 2, allt blir en sträng, snabbast)
print('Produkten av ' + str(tal1) + ' och ' + str(tal2) + ' blir ' + str(prod))

# Skriv ut resultatet på skärmen (alt 3, med möjlighet till formatering)
print('Produkten av {} och {} blir {}'.format(tal1, tal2, prod))
