#!/usr/bin/python3.7

# Filnamn: övn 5.17 - skriva ut asterisk - kap. 5, sid. 11.py

# Programmet skriver ut en asterisk på första raden med mellanrumm bakom, två 
# på nästa med mellanrum mellan varje asterisk osv. tills den skrivit ut 6 rader
# med 6 asterisker på den sista raden, radsluts tecken finns på varje rad. 

for y in range(1, 7):   # Betyder att vi ska köra loopen 6 ggr
    for x in range(1, y + 1): # y + 1 innebär att vi skriver ut något på en gång
        print('*', end = ' ')
    print('')
