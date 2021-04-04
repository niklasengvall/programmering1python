#!/usr/local/bin/python3.9

# Filnamn: kap. 9, sid. 112 - mer om lokala och globala variabler.py

# Kapitel 9 - Funktioner
# Programmering 1 med Python - Lärobok

# Innehållet i variabler och parametrar som definierats i en funktion är lokala 
# och är inte synliga untanför den
# Vid anrop så läggs variablerna i stack-minnet och frigörs därifrån när 
# funktionen lämnar tillbaka kontrollen till huvudprogrammet
# Variabler som definierats utanför funktionerna är så kallade globala 
# variabler, de är synliga och åtkomliga även innuti funktionerna, så länge
# de inte har egna variabler med samma namn som de globala, då har lokala 
# variabler företräde och då döljs just de globala variablerna för funktionen
# Man kan inte ändra globala variabler på ett enkelt sätt inuti en funktion

# Globala variabler
a = 2
b = 6 

def fun():
    b = 10 # Skymmer alla externa variabler b
    print(b)

def fun2():
    b = a # Att tilldela lokala variabler globalas innehåll är ok
    print(b)

def increase():
    global b # Nyckelordet global talar om att vi ska använda global variabel b
    b += 1

# Anrop av fun
print(b)
print('Anropar fun')
fun()
print(b)

# Anrop av fun2
print(b)
print('Anropar fun2')
fun2()
print(b)

# Anrop av increase
b = 6
print(b)
print('Anropar increase')
increase()
print(b)
