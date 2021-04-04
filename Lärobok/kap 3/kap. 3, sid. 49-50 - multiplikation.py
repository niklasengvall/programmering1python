#!/usr/local/bin/python3.9

# Filnamn: kap. 3, sid. 49-50 - multiplikation.py

# Kapitel 3 - Skapa program eller skript
# Programmering 1 med Python - Lärobok

# Programmet frågar användaren efter två faktorer och multiplicerar dessa 
# därefter visas resultatet på skärmen.

# Skriv ut programmets rubrik
print('Multiplikation')
print('==============\n')

# Fråga efter två tal som också omvandlas från sträng till int (heltal)
t1 = int(input('Skriv ett heltal: '))
t2 = int(input('Skriv ett heltal till: '))

# Beräkna produkten av dessa två tal och placera resultatet i variabeln p
p = t1 * t2

# Skriv ut resultatet på skärmen (alt 1, långsamare metod)
print('Produkten av', t1, 'och', t2, 'blir', p)

# Skriv ut resultatet på skärmen (alt 2, allt blir en sträng, snabbast)
print('Produkten av ' + str(t1) + ' och ' + str(t2) + ' blir ' + str(p))

# Skriv ut resultatet på skärmen (alt 3, med möjlighet till formatering)
print('Produkten av {} och {} blir {}'.format(t1, t2, p))
