#!/usr/bin/python3.8

# Filnamn: övn 11.1 - ärflyttal.py

# Felhantering i Python - Undantag eller "Exceptions"
# Programmeringsövningar till kapitel 11

# Programmet kontrollerar om en sträng kan konverteras till flyttal eller ej

# Funktionsdefinitioner
def isFloatAble(sträng):        # Funktionshuvud
    try:
        tal = float(sträng)
    ex cept ValueError:
        returvärde = False
    else:
        returvärde = True

    return returvärde

# Huvudprogram
def main():
    tal1 = '-3.14'
    tal2 = '1,25'
    tal2.is
    if isFloatAble(tal1):
        print('Strängen',tal1, 'är möjlig att göra om till ett flyttal.')
    else:
        print('Strängen',tal1, 'är omöjlig att göra om till ett flyttal.')

    if isFloatAble(tal2):
        print('Strängen',tal2, 'är möjlig att göra om till ett flyttal.')
    else:
        print('Strängen',tal2, 'är omöjlig att göra om till ett flyttal.')

## Huvudprogram anropas 
main()