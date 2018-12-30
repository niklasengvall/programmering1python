#!/usr/bin/python3

# Filnamn: for-loopar i Python med strängar, kap. 5, sid. 64.py

# For-loop med en sträng
# Programmet loopar igenom och skriver ut alla tecken i användarens inmatade
# namn på konsolen

namn = input('Hej, vad heter du? ')
for tecken in namn:
    print(tecken)  