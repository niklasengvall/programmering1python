#!/usr/local/bin/python3.9

# Filnamn: kap. 11, sid. 132 - rätt felhantering, inget brakar ihop.py

# Kapitel 11 - Felhantering i Python - undantag eller "Exceptions"
# Programmering 1 med Python - Lärobok

while True:
    try:
        tal = int(input('Ange ett heltal: ')) 
    except ValueError:
        print('Fel: Du har ej matat in ett korrekt heltal.')
    else:
        # Gå ur loopen när tal matats in
        break
    finally:
        print('Denna kodrad körs oavsett fel eller inte!')

print('Talet du angav är',tal)