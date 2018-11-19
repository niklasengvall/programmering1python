#!/usr/bin/python3

# Filnamn: elif - kap. 4, sid. 57.py

# betygssättning på ett prov med max 100 poäng

p = int(input('Ange poäng på provet (0 - 100): '))

if p >= 90:
    print('Betyg - A')
elif p >= 80:
    # hit kommer vi bara om poängen är mindre än 90
    print('Betyg - B')
elif p >= 70:
    # hit kommer vi bara om poängen är mindre än 80
    print('Betyg - C')
elif p >= 60:
    # hit kommer vi bara om poängen är mindre än 70
    print('Betyg - D')
elif p >= 50:
    # hit kommer vi bara om poängen är mindre än 60
    print('Betyg - E')
else:
    # hit kommer vi bara om poängen är mindre än 50
    print('Betyg - F')             
