#!/usr/local/bin/python3.9

# Filnamn: övn 5.12 - ränta på pengar - kap 5, sid. 10.py

# Loopar - upprepning, iteration
# Programmeringsövningar till kapitel 5 - Arbetsbok

# Programmet beräknar hur mycket pengar du har på ditt sparkonto vid en årsränta på 2 %, startkapital på 1 krona och efter 2017 år

# Skriv ut rubrik
print('Ränta på pengar')
print('===============')

# Deklarera och initiera variablerna
ränta = 1.02
kapital = 1.00
år = 0

for år in range(1, 2018):      
    kapital = kapital * ränta 
    print('År {:4d} är kapitalet {:.0f} kr'.format(år, 1 * ränta ** år))

print('År 2017 är kapitalet {:.2f} kr'.format(1 * 1.02 ** 2017))

input('\nTryck på en tangent...\n')
