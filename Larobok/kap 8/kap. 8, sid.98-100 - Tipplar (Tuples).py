#!/usr/bin/python3.8

# Filnamn: kap. 8, sid.98-100 - Tipplar (Tuples).py

# Kapitel 8 - Listor och tipplar
# Programmering 1 med Python - Lärobok

# En tippel anges med parenteser
tippel = (7, 14, 21, 28)
print(tippel)

# Men för att komma åtenskilda elemet så använder vi precis som 
# för listor hakparenteser
print(tippel[2])

# elementen i en tippel är oföränderliga, följande rad ger ett felmeddelande
# ta bort kommentarsmarkeringen (fyrkanten) så ser du felmeddelandet vid körning
# tippel[0] = 3 # => TypeError: 'tuple' object does not support item assignment


# En tom tippel saknar innehåll innanför parenteserna
renTippel = ()
print(renTippel)

# För att lagra ett element, placera ett komma bakom.add()
# annars tolkas parentesen som en vanlig aritmetisk operation
enTippel = (7,)
print(enTippel)

# En tippel kan också anges utan parenteser
altTippel = 3, 6, 9, 12
print(altTippel)

# Alternativ metod för att tilldela andra variabler en tippels värde
at, bt, ct, dt = altTippel
print(at, bt, ct, dt)

# Växla värden melan variabler
x = 3
y = 7
print('Före växlingen: x =', x, 'y =', y)

# Beprövad metod
tmp = x
x = y
y = tmp
print('Efter växlingen: x =', x, 'y =', y)

# Växla med hjälp av tippel (kom ihåg inga parenteser behövs)
# et = x, y # Normalfall men det kan skippas
print('Före växlingen: x =', x, 'y =', y)
# y, x = et # Detta mellansteg kan skippas, skriv istället direkt
y, x = x, y
print('Efter växlingen: x =', x, 'y =', y)