#!/usr/bin/python3.7

# Filnamn: kap. 12, sid. 135 - sköldpaddsgrafik kodexempel.py

# Kapitel 12 - Sköldpaddsgrafik
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Import av modul med sköldpaddsgrafiksfunktioner
from turtle import *
# Gör utritningsfönstret (canvas) 1200x900 pixlar
setup(width = 1200, height = 900)
# Sätt det som modalt, dvs. låst, längst fram på skärmen
getscreen()._root.attributes('-topmost',1)
# Tala om att vi ska prata grader
degrees()
# Så att vi kan ändra färg med hexadecimala siffror eller decimala
colormode(255)
# Sätt penfärg till orange och fyllning till ljusgul
color(('#ffcc88'), (255,255,192))
# Sätt högsta rithastighet
speed(0)
# Hoppa över en skärmritning, för att snabba upp utritandet
tracer(1)
# Göm sköldpaddstriangel
hideturtle()
# Tala om att vi ska börja rita
begin_fill()
while True:
    # Rita linje 360 pixlar åt höger (utgångspunkt)
    forward(360)
    # vrid åt vänster 115 grader
    left(115)
    if abs(pos()) < 1:
        break
end_fill()
# Se till och visa allt utritat (som kan ligga i buffert) på canvasen
update()
done()