#!/usr/local/bin/python3.9

# Filnamn: övn 12.7, sid. 31 - kvadrat.py

# Sköldpaddsgrafik
# Programmeringsövningar till kapitel 12

# Programmet ritar ut en kvadrat med sidan s i aktuell sköldpaddsmarkörsriktning

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *

# Funktionsdefinitioner

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
    
    # Rita 1:a kvadraten
    goto(0,0)
    kvadrat(200)

    # Rita 2:a kvadraten
    goto(-50,50)
    setheading(15)
    kvadrat(200)

    # Rita 3:e kvadraten
    goto(-75,75)
    setheading(30)
    kvadrat(200)

    update()
    done()

## Huvudprogram anropas 
main()