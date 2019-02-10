#!/usr/bin/python3.7

# Filnamn: kap. 12, sid. 151-153 - ritar en funktion, första och andra 
# derivata.py

# Kapitel 12 - Sköldpaddsgrafik
# Programmering 1 med Python - Lärobok

# Programmet ritar ut angiven funktion
# Då ursprungskod är felaktig så har jag endast löst funktionsutritningen

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *
from math import *

# Konstantdefinitioner
DELTA = 1e-6

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

def f(funk, tal):
    """ Beräknar inmatad funktion
        rtype: string 
    """
    x = tal
    s = funk
    return eval(s)
 
#def D(funk):
#    def derivata(funk):
#        return(f(x + DELTA) - f(x - DELTA)) / (2 * DELTA)
#    return derivata

def koordinatsystem():
    setup(width = 1000, height= 1000)
    setworldcoordinates(-10.2, -10.2, 10.2, 10.2)
    
    ht() # hideturtle Göm turtlepekaren
    
    # Rita ut ett rutnät
    for i in range(-10,11):
        # rita lodräta linjer
        linje(i, 10, i, -10)
    for i in range(-10, 11):
        # rita horisontella linjer
        linje(-10, i, 10, i)

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
    linje(0, -10, 0, 10)
    setheading(90)
    stamp()
    pu()
    goto(0.3, 9.6)
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

def plotta(funk):
    x = -10
    pu()
    while x <= 10:
        # vi vill undvika division med noll eller logaritmer med negativa tal
        try:
            goto(x, f(funk,x))
        except:
            pass
        else: 
            pd()         
        x += 0.1

# Initiera snbb grafik och rita koordinatsystem
speed(0)
tracer(25)
koordinatsystem()

funktion = textinput('Funktion att rita ut','Ange funktion: ')

# Skriv ut funktionens namn som vi ska plotta
pu()
goto(-9.5, 9.5)
write('y = ' + funktion, font = ('Arial', 13, 'bold'))

# rita funktionen
pencolor('blue')
plotta(funktion)
# 0.25*x**3-4*x

update()
done()
