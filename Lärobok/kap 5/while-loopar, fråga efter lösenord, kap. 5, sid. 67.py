#!/usr/bin/python3

# Filnamn: while-loopar, fråga efter lösenord, kap. 5, sid. 67.py

# Programmet frågar efter ett lösenord och tjatar på användaren tills det blir 
# rätt och då fortsätter programmet med att skriva "Lösen ok!"

psw = input('Ange lösenord: ')

while psw != 'asd14x':
    print('Felaktigt lösenord. Försök igen!')
    psw = input('Ange lösenord: ')

print('Lösen ok!')