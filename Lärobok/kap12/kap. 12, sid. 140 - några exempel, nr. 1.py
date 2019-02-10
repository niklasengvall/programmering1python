#!/usr/bin/python3.7

# Filnamn: kap. 12, sid. 140 - några exempel, nr. 1.py

# Kapitel 12 - Sköldpaddsgrafik
# Programmering 1 med Python - Lärobok

# Programmet ritar en massa cirklar, de vrids 6 grader för varje ny som ritas

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *

#Sätt canvas till 800x800 och skalan
setup(width = 900, height = 900)
setworldcoordinates(-300, -300, 300, 300)

# Sätt högst rithastighet och dölj sköldpaddan 
speed(0)
ht()

# Sätt bakgrundsfärg, pennfärg och penntjocklek
r = 255
g = 0
b = 0
colormode(255) # Nu kan vi använda rgb-värden på färger
bgcolor(0,0,0) # Svart bakgrundsfärg
pencolor(255,0,0) # Röd pennfärg
pensize(1)

# k-värde för att byta färg 60 ggr motsvarande 0-255 i färgskala 
ct = 4.25
# rita ut 60 cirklar och byt färg
for c in range(60):
    lt(6)
    circle(140)
    pencolor(int(r-(ct*c)),int((ct*c)),b) 
done()
