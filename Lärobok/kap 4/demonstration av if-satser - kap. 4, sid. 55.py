#!/usr/bin/python3

# Filnamn: demonstration av if-satser - kap. 4, sid. 55.py

# Villkor, if-satser 

# Demonstration av if-satser
# Först initierar vi några variabler som vi sedan kan testa på

x = 7
y = 3
z = 7

# Enkla jämförelser
# Testar "mindre än" och "större än" 
if y < x:
    print('y är mindre än x')
if x < y:
    print('x är mindre än y')

# Test av "mindre än eller lika med"
if y <= z:
    print('y är mindre än eller lika med z')

# Test på likhet, demonstartion av större programblock och
# att vi kan "nästla" if-satserna
if z == x:
    print('z är lika med x')
    print('och vi kan skriva ut')
    print('flera rader också')
    if z > y:
        print('Dessutom är z större än y')
        print('och vi kan ha if-satser inuti andra if-satser')

# Test för olikhet
if z != 8:
    print('z är inte lika med 8')
