#!/usr/local/bin/python3.9

# Filnamn: övn 12.5, sid. 30 - stega mot origo.py

# Sköldpaddsgrafik
# Programmeringsövningar till kapitel 12

# Programmet ritar ut en linje som går mot origo på x-axeln och högst upp
# på y-axeln

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *

# Funktionsdefinitioner
def linje(x1, y1, x2, y2):
    pu()
    goto(x1, y1)
    pd()
    goto(x2, y2)
    pu()

# Huvudprogram
def main():
    #Sätt canvas till 800x800 och skalan
    setup(width = 800, height = 800)
    setworldcoordinates(-20, -20, 20, 20)

    # Sätt högst rithastighet och dölj sköldpaddan 
    #speed(0)
    #tracer(25)
    ht()
    
    # Sätt bakgrundsfärg, pennfärg och penntjocklek
    colormode(255) # Nu kan vi använda rgb-värden på färger
    bgcolor(255, 255, 255) # Vit bakgrundsfärg
    pensize(1)
    pencolor(0, 0, 0) # Svart pennfärg

    for i in range(0, 21):
        linje(20-i, 0, 0, i)

    update()
    done()

## Huvudprogram anropas 
main()