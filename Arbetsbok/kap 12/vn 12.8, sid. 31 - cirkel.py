#!/usr/bin/python3.8

# Filnamn: övn 12.7, sid. 31 - kvadrat.py

# Sköldpaddsgrafik
# Programmeringsövningar till kapitel 12

# Programmet ritar ut 3 cirklar med radien radie, användaren kan välja om den 
# ska vara fylld och även ange färg

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *

# Funktionsdefinitioner
def cirkel(radie, fyllning, color):
    pencolor(color) # Röd pennfärg
    fillcolor(color)

    pd()
    if fyllning:
        begin_fill()
    circle(radie)
    if fyllning:
        end_fill()
    pu()

def kvadrat(s):
    pd()
    fd(s)
    lt(90)
    fd(s)
    lt(90)
    fd(s)
    lt(90)
    fd(s)
    pu()

# Huvudprogram
def main():
    #Sätt canvas till 800x800 och skalan
    setup(width = 800, height = 800)
    setworldcoordinates(-400, -400, 400, 400)

    # Sätt högst rithastighet och dölj sköldpaddan 
    speed(0)
    tracer(25)
    ht()
    pu()

    # Sätt bakgrundsfärg, pennfärg och penntjocklek
    colormode(255) # Nu kan vi använda rgb-värden på färger
    bgcolor(255,255,255) # Vit bakgrundsfärg
    
    # Rita 1:a cirkeln
    goto(0,0)
    cirkel(100,1,(255,0,0))

    # Rita 2:a cirkeln
    goto(-50,50)
    cirkel(100,0,(255,128,0))

    # Rita 3:e cirkeln
    goto(-75,75)
    cirkel(100,1,(255,128,192))

    update()
    done()

## Huvudprogram anropas 
main()