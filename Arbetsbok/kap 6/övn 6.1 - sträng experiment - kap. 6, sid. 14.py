#!/usr/local/bin/python3.9

# Filnamn: övn 6.1 - sträng experiment - kap. 6, sid. 14.py

# Mer om teckensträngar i Python
# Programmeringsövningar till kapitel 6

# Övning 1 a) 
# Använda operatorn in på en sträng på olika sätt

str = 'Jag hoppas att du trivs med Python'
if 'a' in str:
    print("Bokstaven 'a' finns i strängen: " + str)
else:
    print("Bokstaven 'a' finns inte i strängen: " + str)
if 'oppa' in str:
    print("Bokstäverna 'oppa' finns i strängen: " + str)
else:
    print("Bokstäverna 'oppa' finns inte i strängen: " + str)

# Övning 1 b) 
# Skapa en sträng som består av ett antal multipler av en annan sträng
gmlStr = ".oOo."
enNySträng = 10 * gmlStr
print(enNySträng)

# Övning 1 c) 
# Skapa slices
ego = str[:3]
språk = str[28:34]
språktrivsel = str[18:]
baklänges = str[::-1]
varannan = str[::2]
print(ego, språk, språktrivsel)
print(baklänges)
print(varannan)

# Övning 1d till 1i 
# Testa olika strängmetoder
fras = '   eleMentärt, eller hur dr. Watson!   '

# 1 d) Enbart stora bokstäver
print(fras.upper())

# 1 e) Enbart gemena bokstäver
print(fras.lower())

# 1 f) Stor första bokstav och resten gemener
print(fras.strip().capitalize())

# 1 g) Stor bokstav i början av varje ord
print(fras.title())

# 1 h) Sträng med alla tecken i omvänd ordning
print(fras[::-1])

# 1 i) Ta bort alla mellanslag i början och i slutet av strängen
print(fras.strip())