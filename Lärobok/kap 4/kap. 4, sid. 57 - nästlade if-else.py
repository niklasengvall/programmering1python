#!/usr/bin/python3.7

# Filnamn: kap. 4, sid. 57 - nästlade if-else.py

# Kapitel 4 - Villkor, IF-satser
# Programmering 1 med Python - Lärobok

# Betygssättning på ett prov

r = int(input('Ange provpoäng (0 - 100): '))

if r >= 95:
    print('Betyg: A')
else:
    # körs om poäng är mellan 80 - 94
    if r >= 80:
        print('Betyg: B')
    else:
        # körs om poäng är mellan 70 - 79
        if r >= 70:
            print('Betyg: C')
        else:
            # körs om poäng är mellan 60 - 69
            if r >= 60:
                print('Betyg: D')
            else:
                # körs om poäng är mellan 50 - 59
                if r >= 50:
                    print('Betyg: E')
                else:
                    # körs om poäng är mindre än 50
                    print('Betyg: F')

                    
