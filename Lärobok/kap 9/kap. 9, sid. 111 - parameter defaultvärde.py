#!/usr/local/bin/python3.9

# Filnamn: kap. 9, sid. 111 - parameter defaultvärde.py

# Kapitel 9 - Funktioner
# Programmering 1 med Python - Lärobok

# Funktioner med dafaultvärde på parametrar och docstring
def greeting(name, message = 'nice to see you!'):
    """ Skriver ett hälsningsmeddelande 'message' till 'name' 
    
    Om inget hälsningsmeddelade ges, används defaultvärde

    name : string
        Namnet på den man skriver hälsningsmeddelandet till

    message : string, optional 
        Hälsningsmedelande

    raises : 
        Ingen felkontroll 

    rtype: Inget
        Returns nothing
    """

    print('Hi ' + name + ', ' + message)

# Programmet startar här
n = input("What's your name? ")
greeting(n)         
greeting(n, 'how are you?')