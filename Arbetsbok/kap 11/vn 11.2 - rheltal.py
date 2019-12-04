#!/usr/bin/python3.7

# Filnamn: övn 11.2 - ärheltal.py

# Felhantering i Python - Undantag eller "Exceptions"
# Programmeringsövningar till kapitel 11

# Programmet kontrollerar om en sträng kan konverteras till heltal eller ej

# Funktionsdefinitioner
def isIntAble(sträng):        # Funktionshuvud
    try:
        tal = int(sträng)
    except ValueError:
        returvärde = False
    else:
        returvärde = True

    return returvärde

# Huvudprogram
def main():
    tal1 = '-3'
    tal2 = '1,25'

    if isIntAble(tal1):
        print('Strängen',tal1, 'är möjlig att göra om till ett heltal.')
    else:
        print('Strängen',tal1, 'är omöjlig att göra om till ett heltal.')

    if isIntAble(tal2):
        print('Strängen',tal2, 'är möjlig att göra om till ett heltal.')
    else:
        print('Strängen',tal2, 'är omöjlig att göra om till ett heltal.')

## Huvudprogram anropas 
main()