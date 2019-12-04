#!/usr/bin/python3.7

# Filnamn: kap. 5, sid. 64 - for-loopar i Python med strängar.py

# Kapitel 5 - Loopar - upprepning, itteration
# Programmering 1 med Python - Lärobok

# For-loop med en sträng
# Programmet loopar igenom och skriver ut alla tecken i användarens inmatade
# namn på konsolen

name = input('Tjenna! Vad heter du då? ')
for char in name: # För varje bokstav i strängen name
    print(char)   # Skriv ut dem på skärmen