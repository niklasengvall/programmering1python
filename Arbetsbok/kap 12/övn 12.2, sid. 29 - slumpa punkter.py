#!/usr/bin/python3.8

# Filnamn: övn 12.2, sid. 29 - slumpa punkter.py

# Sköldpaddsgrafik
# Programmeringsövningar till kapitel 12

# Programmet slumpar ut 1000 st punkter i varierande storlek

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *
from random import *

# Funktionsdefinitioner
def pluttar(x, y, storlek, farg):
    goto(x, y)
    pd()
    dot(storlek, farg)
    pu()

# Huvudprogram
def main():
    #Sätt canvas till 1920x1080 och skalan
    setup(width = 1920, height = 1080)
    setworldcoordinates(0, 0, 1920, 1080)
    # Sätt högst rithastighet och dölj sköldpaddan 
    speed(0)
    tracer(60)
    ht()
    pu()
    # Sätt bakgrundsfärg, pennfärg och penntjocklek
    colormode(255) # Nu kan vi använda rgb-värden på färger
    bgcolor(255,255,255) # Vit bakgrundsfärg
    
    # Rita ut 1000 pluttar
    for i in range(1001): 
        # slumpa position
        x = randrange(0,1920)
        y = randrange(0,1080)
        # slumpa storlek
        storlek = randrange(1,100)
        # slumpa färg    
        r = randrange(256)
        g = randrange(256)
        b = randrange(256)
        farg = (r, g, b)
        pluttar(x, y, storlek, farg)
    
    update()    
    done()

## Huvudprogram anropas 
main()