#!/usr/bin/python3.7

# Filnamn: övn 5.1 - räkna med programloopar - kap 5, sid 9.py

# Loopar - upprepning, iteration
# Programmeringsövningar till kapitel 5 - Arbetsbok

# Programmet kör fyra olika loopar som på räknar på skärmen...

# a) från och med 1 till och med 15
for i in range(1, 16):  # stop/räkna till ska vara det antal man vill att loopen
                        # ska inkludera + 1
    print(i)
# Pausa till nästa loop 
input('\nTryck på en tangent...\n')

# b) från 20 till och med 30
for i in range(20, 31):
    print(i)
input('\nTryck på en tangent...\n')

# c) från 0 till och med 1000
for i in range(1001):   # endast ett värde, från 0 till inkludera t.o.m. + 1
    print(i, end=' ')   # end=' ' talar om att det ska mellanslag och inte
                        # vagnretur som avslutande tecken i strängen.
input('\nTryck på en tangent...\n')

# d) från och med 10 till och med -10
for i in range(10, -11, -1):    # 3:e väerrdet anger om det ska vara upp- eller 
                                # nedräkning och i hur många steg, negativt 
                                # värde = nedräkning
    print(i)
input('\nTryck på en tangent...\n')