#!/usr/local/bin/python3.9

# Filnamn: kap. 12, sid. 146 - flytta sköldpaddan med musen.py

# Kapitel 12 - Sköldpaddsgrafik
# Programmering 1 med Python - Lärobok

# Programmet använder en egendefinierad sköldpaddsmarkör och ritar linjer
# mellan de olika x och y koordinater som användaren klickar på muspekaren.

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *

def flytta(x, y):
    goto(x, y)

# Fånga sköldpaddspekaren och lagra den som en bild
# Du måste ändra sökvägen till din bild och ha den i samma mapp som denna fil
register_shape('/home/niklas/pyProjects/programmering1python/Lärobok/kap12/form.gif')
# Byt sköldpaddspekare
shape('/home/niklas/pyProjects/programmering1python/Lärobok/kap12/form.gif')
# rita sköldpaddsmarkör
stamp()

# Om man klickar med musen flytta sköldpadda till musposition
onscreenclick(flytta)
done()