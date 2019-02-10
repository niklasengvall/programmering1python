#!/usr/bin/python3.7

# Filnamn: kap. 12, sid. 144 - kvadratspiral.py

# Kapitel 12 - Sköldpaddsgrafik
# Programmering 1 med Python - Lärobok

# Programmet ritar en massa trianglar, linjer vrids 121 grader för varje ny som
# ritas

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *

#Sätt canvas till 800x800 och skalan
setup(width = 800, height = 800)
setworldcoordinates(-400, -400, 400, 400)
ht() # hideturtle() - göm pennan för att rita snabbare
speed(0) # högsta rithastighet
#tracer(2) 
colormode(255)
bgcolor(0,0,0) # svart bakgrund
pencolor(128,64,192) #
pensize(1) # penntjocklek

# rita ut en kvadrat och för varje ny, 21 steg åt vänster samt en ökad 
# radie med 3 steg
for c in range(540): # rita ut 540 linjer
    fd(c) # flytta sköldpadda i pixlar
    rt(121) # rotera 121 grader medsols

update() # rita ut allt som ev. inte ritats ut från bakgrundsbuffert
done()
