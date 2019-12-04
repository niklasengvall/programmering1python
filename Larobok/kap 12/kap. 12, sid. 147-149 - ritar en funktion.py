#!/usr/bin/python3.8

# Filnamn: kap. 12, sid. 147-149 - ritar en funktion.py

# Kapitel 12 - Sköldpaddsgrafik
# Programmering 1 med Python - Lärobok

# Programmet ritar ut funktionen y = 2*sin(x)

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *
from math import cos

def linje(x1, y1, x2, y2): 
    """ Ritar en linje mellan koordinatsystemna x1, y1 och x2, y2 
        
        x1:    int
        y1:    int
        x2:    int
        y2:    int
        rtype: none
    """    
    pu() # pen up - rita inte
    goto(x1, y1) # flytta markören
    pd() # pen down - rita 
    goto(x2, y2) # flytta markören så att en linje ritas

def f(x):
    """ Funktionen 3 * cos(x) 

        x: vinkel i grader
        x: int
        rtype: float 
    """
    return 3*cos(x)
 
def koordinatsystem():
    setup(width = 1000, height= 300)
    setworldcoordinates(-10.2, -3.2, 10.2, 3.2)
    
    ht() # hideturtle Göm turtlepekaren
    
    # Rita ut ett rutnät
    for c in range(-10,11):
        # rita lodräta linjer
        linje(c, 3, c, -3)
    for i in range(-3, 4):
        # rita horisontella linjer
        linje(-10, c, 10, c)

    # Rita koordinataxlar med pilar i ena änden
    # vi börjar med x-axeln
    pensize(2)
    linje(-10,0,10,0)
    setheading(0) # Ändra ritriktning
    stamp()
    pu()
    goto(9.6, 0.3)
    write('X', font = ('Arial', 12, 'normal'))

    # y-axeln
    linje(0, -3, 0, 3)
    setheading(90)
    stamp()
    pu()
    goto(0.3, 2.6)
    write('Y', font = ('Arial', 12, 'normal'))    

    # Rita ut skalstreck och längdenhet 1 på bägge axlarna
    # x-axeln
    pu()
    goto(1, 0.2)
    pd()
    goto(1, -0.2)
    pu()
    goto(1.1, -0.5)
    write('1', font = ('Arial', 12, 'normal'))    

    # y-axeln
    pu()
    goto(-0.2, 1)
    pd()
    goto(0.2, 1)
    pu()
    goto(0.3, 1.05)
    write('1', font = ('Arial', 12, 'normal'))    

def rita():
    x = -10
    pu()
    goto(x, f(x))
    pencolor('blue')
    pd()
    while x <= 10:
        x += 0.1
        goto(x, f(x))

# Initiera snbb grafik och rita koordinatsystem
speed(0)
tracer(25)
koordinatsystem()

# Skriv ut funktionens namn som vi ska rita
pu()
goto(-9.5, 2.25)
write('y = 3cos(x)', font = ('Arial', 12, 'normal'))    

# rita funktionen
rita()
update()
done()
