#!/usr/local/bin/python3.9

# Filnamn: kap. 12, sid. 140 - några exempel, nr. 1.py

# Kapitel 12 - Sköldpaddsgrafik
# Programmering 1 med Python - Lärobok

# Programmet ritar en massa cirklar, de vrids 6 grader för varje ny som ritas

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *
from random import randrange

def cirkel(x, y, radie):
    pu() # penup() - ta upp pennan - rita inte
    goto(x, y) # flytta pennan 
    fd(radie) # forward() - flytta pennan åt höger radie punkter
    lt(90) # vrid pennan 90 grader åt vänster
    pd() # sätt ner pennan och rita 
    circle(radie) # rita cirkel
    pu() # ta upp penna och rita inte

#Sätt canvas till 800x800 och skalan
setup(width = 900, height = 900)
setworldcoordinates(-300, -300, 300, 300)
colormode(255)
bgcolor(0,0,0)

speed(0) # högsta rithastighet
tracer(25) # ???
ht() # hideturtle() - göm pennan för att rita snabbare
pensize(2) # penntjocklek

# Slumpa ny pennfärg för den ena cirkeln
r = randrange(0,256)
g = randrange(0,256)
b = randrange(0,256)

# rita ut en cirkel och för varje ny, 21 steg åt vänster samt en ökad 
# radie med 3 steg
for c in range(3, 600, 3):
    pencolor(r,g,b)
    cirkel(-21, 0, c)

# Slumpa ny pennfärg för den andra cirkeln
r = randrange(0,256)
g = randrange(0,256)
b = randrange(0,256)

# rita ut en cirkel och för varje ny, 21 steg åt höger samt en ökad 
# radie med 3 steg
for c in range(3, 600, 3):
    pencolor(r,g,b)
    cirkel(21, 0, c)

update() # rita ut allt som ev. inte ritats ut från bakgrundsbuffert
done()
