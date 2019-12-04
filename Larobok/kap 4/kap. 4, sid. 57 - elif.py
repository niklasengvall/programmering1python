#!/usr/bin/python3.7

# Filnamn: kap. 4, sid. 57 - elif.py

# Kapitel 4 - Villkor, IF-satser
# Programmering 1 med Python - Lärobok

# Villkorstest när det gäller betygssättning på prov

resultat = int(input('Ange provpoäng (0 - 100): '))

if resultat >= 95:
    print('Betyg: A')
elif resultat >= 80:
    # körs om poäng är mellan 80 - 94
    print('Betyg: B')
elif resultat >= 70:
    # körs om poäng är mellan 70 - 79
    print('Betyg: C')
elif resultat >= 60:
    # körs om poäng är mellan 60 - 69
    print('Betyg: D')
elif resultat >= 50:
    # körs om poäng är mellan 50 - 59
    print('Betyg: E')
else:
    # körs om poäng är mindre än 50
    print('Betyg: F')             
