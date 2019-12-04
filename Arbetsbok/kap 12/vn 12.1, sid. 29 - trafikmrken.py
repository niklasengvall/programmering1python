#!/usr/bin/python3.7

# Filnamn: övn 12.1, sid. 29 - trafikmärken.py

# Sköldpaddsgrafik
# Programmeringsövningar till kapitel 12

# Programmet ritar ut 4 st trafikmärken

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *

# Funktionsdefinitioner
def cirkel(x, y, radie, color):
    pensize(1)
    pencolor(color) # Röd pennfärg
    fillcolor(color)
    goto(x, y)
    pd()
    begin_fill()
    circle(radie)
    end_fill()
    pu()

def pluttar(x, y, ic):
    pu()
    goto(x, y)
    pd()
    dot(25, "#000000")
    dot(17.5, ic)
    pu()

def linje(x1, y1, x2, y2, radie, color):
    pu()
    goto(x1,  y1)
    pencolor(color)
    pensize(radie)
    pd()
    goto(x2, y2)
    pu()

def triangel(x1, y1, x2, y2, x3, y3, radie, pc, fc):
    pu()
    pencolor(pc)
    fillcolor(fc)
    pensize(radie)
    goto(x1,y1)
    pd()
    begin_fill()
    begin_poly()
    goto(x2,y2)
    goto(x3,y3)
    goto(x1,y1)
    end_poly()
    end_fill()
    pu()

# Huvudprogram
def main():
    #Sätt canvas till 800x800 och skalan
    setup(width = 900, height = 200)
    setworldcoordinates(-450, -100, 450, 100)

    # Sätt högst rithastighet och dölj sköldpaddan 
    speed(0)
    tracer(25)
    ht()
    pu()

    # Sätt bakgrundsfärg, pennfärg och penntjocklek
    colormode(255) # Nu kan vi använda rgb-värden på färger
    bgcolor(255,255,255) # Vit bakgrundsfärg
    
    # Rita första trafikmärket 
    # Anropa egen cirkelfunktion
    cirkel(-350,-100,100,"#ff0000")
    cirkel(-350, -75, 75,"#ffff00")

    # Rita andra trafikmärket
    # Anropa egen triangelfunktion
    triangel(-225,-75,-125,75,-25,-75,25,"#ff0000","#ffff00")
    # Rita svart linje
    linje(-125,15,-125,-40,25,"#000000")

    # Rita tredje trafikmärket
    triangel(25,-75,125,75,225,-75,25,"#ff0000","#ffff00")
    # Rita tre små cirklar med mindre färgcirklar i sig
    pluttar(125, 20, "#ff0000")
    pluttar(125, -10, "#ffff00")
    pluttar(125, -40, "#00ff00")
    
    # Rita fjärde trafikmärket 
    cirkel(350,-100,100,"#ff0000")
    cirkel(350, -75, 75,"#000088")
    # Rita krysset
    linje(300,50,400,-50,25,"#ff0000")
    linje(400,50,300,-50,25,"#ff0000")
    
    update()
    done()

## Huvudprogram anropas 
main()