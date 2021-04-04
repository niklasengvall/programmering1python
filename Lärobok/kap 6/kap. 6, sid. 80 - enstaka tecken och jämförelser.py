#!/usr/local/bin/python3.9

# Filname: kap. 6, sid. 80 - enstaka tecken och jämförelser.py

# Kapitel 6 - Mer om teckensträngar i Python
# Programmering 1 med Python - Lärobok

# Enstaka tecken
# Ta reda på en bokstavs teckenkod
sträng = 'Agnes'
teckenkod1 = ord('A')
teckenkod2 = ord(sträng[1]) # Vi vill ha teckenkod för 2:a bokstaven g
print('teckenkod1:',teckenkod1,'teckenkod2:',teckenkod2)

# Skriv ut ett B och snabel-a
bokstav1 = chr(66)
bokstav2 = chr(64)
print('teckenkod 66:', bokstav1, 'teckenkod 64:', bokstav2)

# Jämförelser av strängar
s1 = 'abc'
s2 = 'bcd'
s3 = 'abc'

print("""s1 = \'abc\'
s2 = \'bcd\'
s3 = \'abc\'""")
if s1 == s2:
    print('Strängarna s1 och s2 är lika')
else: 
    print('Strängarna s1 och s2 är olika')

if s1 == s3:
    print('Strängarna s1 och s3 är lika')
else: 
    print('Strängarna s1 och s3 är olika')

if s1 != s2:
    print('Strängarna s1 och s2 är skild från varandra')
else: 
    print('Strängarna s1 och s2 är lika')

# Att jämföra strängar så här går bra om vi använder engelska uttryck, ej
# svenska uttryck med bokstäverna åäö. Dessa tecken har teckenkoder som inte 
# kommer i ordning efter bokstaven z
if s1 > s2:
    print('Sträng s1 är större än s2')
else: 
    print('Sträng s1 är inte större än s2')

# Ta fram bitar av en sträng, så kallade slices
# sträng[startindex:slutindex:n steg]
name = 'Tage Test'
print(name)
print('name[5:7] =', name[6:9]) 
print('name[0:3] =', name[0:3])
print('name[0:4] =', name[0:4])
print('name[:4] =', name[:4])
print('name[5:] =', name[5:])
print('name[:] =', name[:])
print('name[::-1] =', name[::-1]) # skriver ut baklänges
print('name[::2] =', name[::2])
