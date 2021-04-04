#!/usr/local/bin/python3.9

# Filnamn: övn 12.4, sid. 30 - klickbart rutnät.py

# Sköldpaddsgrafik
# Programmeringsövningar till kapitel 12

# Programmet ritar ut ett 20x20 stort rutnät som användaren sedan kan klicka i 
# och fylla med gröna rutor

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *

# Funktionsdefinitioner
def linje(x1, y1, x2, y2):
    pu()
    goto(x1, y1)
    pd()
    goto(x2, y2)
    pu()

def fyllRuta(x, y, c):
    pu()
    fillcolor(c)
    goto(x,y)
    pd()
    begin_fill()
    begin_poly()
    goto(x+1,y)
    goto(x+1,y+1)
    goto(x,y+1)
    goto(x,y)
    end_poly()
    end_fill()
    pu()

def gPos(x, y):
    # hämta koordinater och skriv ut dem på skärmen
    
    if x < 0:
        x1 = int(x)-1
    else: 
        x1 = int(x)
    
    if y < 0:
        y1 = int(y)-1
    else: 
        y1 = int(y)

    
    pu()
    goto(-9.5, 9.5)
    pd()
    write('X = ' + str(x1) + ', Y = ' + str(y1), font = ('Arial', 12, 'normal'))
    fyllRuta(x1,y1,(0,255,0))

# Huvudprogram
def main():
    #Sätt canvas till 800x800 och skalan
    setup(width = 800, height = 800)
    setworldcoordinates(-10, -10, 10, 10)

    # Sätt högst rithastighet och dölj sköldpaddan 
    speed(0)
    tracer(25)
    ht()
    
    # Sätt bakgrundsfärg, pennfärg och penntjocklek
    colormode(255) # Nu kan vi använda rgb-värden på färger
    bgcolor(255, 255, 255) # Vit bakgrundsfärg
    pensize(1)
    pencolor(0, 0, 0) # Svart pennfärg

    for i in range(-10, 11):
        linje(-10, i, 10, i)
        linje(i, -10, i, 10)

    onscreenclick(gPos)
    update()
    done()

## Huvudprogram anropas 
main()