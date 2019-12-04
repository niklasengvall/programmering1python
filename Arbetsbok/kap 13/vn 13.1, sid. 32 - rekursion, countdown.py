#!/usr/bin/python3.8

# Filnamn: övn 13.1, sid. 32 - rekursion, countdown.py

# Rekursion- Funktioner som anropar sig själva
# Programmeringsövningar till kapitel 13

# Programmet räknar ner från x med hjälp av egen funktion

# Import av modul

# Funktionsdefinitioner
def countdown(x):
    if x == 0:
        print(x, end = ' ')
        return 0
    print(x, end = ' ')
    return countdown(x - 1)

# Huvudprogram
def main():
    countdown(10)

## Huvudprogram anropas 
main()