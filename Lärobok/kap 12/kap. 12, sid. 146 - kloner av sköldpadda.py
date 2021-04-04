#!/usr/local/bin/python3.9

# Filnamn: kap. 12, sid. 146 - kloner av sköldpadda.py

# Kapitel 12 - Sköldpaddsgrafik
# Programmering 1 med Python - Lärobok

# Programmet ritar ut lite linjer med hjälp av tre markörer och där 
# en markör är klonad

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *

# Skapa två markörobjekt
x = Turtle(shape = 'square')
y = Turtle(shape='arrow')

y.fd(200) # Gå 200 pixlar åt höger med pilmarkören
x.goto(200, 200) # Flytta fyrkantsmarkören 200 pixlar uppåt och åt höger
# Klona y markören
z = y.clone()
z.fillcolor('yellow')
# Låt den klonade markören gå 200 steg åt höger
z.forward(200)
done()