#!/usr/bin/python3

# Filnamn: nästlade if-else - kap. 4, sid. 57.py

# betygssättning på ett prov med max 100 poäng

p = int(input('Ange poäng på provet (0 - 100): '))

if p >= 90:
    print('Betyg - A')
else:
    # hit kommer vi bara om poängen är mindre än 90
    if p >= 80:
        print('Betyg - B')
    else:
        # hit kommer vi bara om poängen är mindre än 80
        if p >= 70:
            print('Betyg - C')
        else:
            # hit kommer vi bara om poängen är mindre än 70
            if p >= 60:
                print('Betyg - D')
            else:
                # hit kommer vi bara om poängen är mindre än 60
                if p >= 50:
                    print('Betyg - E')
                else:
                    # hit kommer vi bara om poängen är mindre än 50
                    print('Betyg - F')

                    
