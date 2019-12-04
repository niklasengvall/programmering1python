#!/usr/bin/python3.8

# Filnamn: kap. 12, sid. 145 - ändra sköldpaddan.py

# Kapitel 12 - Sköldpaddsgrafik
# Programmering 1 med Python - Lärobok

# Programmet ritar ut och döljer olika sköldpadsmarkörer

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *

# lista med olika sköldpaddsutseenden
shapes = ['arrow', 'turtle', 'circle', 'square', 'triangle', 'classic']

# Sätt lite bättre färgmode
colormode(255)
bgcolor(0,0,0) # svart bakgrund

# Backa först 400 pixlar
back(400)
# Turkos penn- och fyllningsfärg
pencolor(64,128,192)
fillcolor(128,192,255)

# Här ska vi lagra stämplarna av sköldpaddspekaren
stamps = []

# sätt storleken på sköldpaddspekaren
turtlesize(3, 3, 4) # 3 x större bredd, 3 x större höjd och 4 px tjock kontur 

for sh in shapes:
    fd(100) # flytta 100 steg åt höger 
    shape(sh) # byt sködpaddspekarens utseende 
    h = stamp() # ta fram ett handtagsid till nuvarande sköldpaddsmarkör
    stamps.append(h) # lagra handtaget i listan 

# ta bort den fjärde lagrade sköldpaddsmarkören (kvadraten)
clearstamp(stamps[3])

done()