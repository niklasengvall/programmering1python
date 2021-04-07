#!/usr/local/bin/python3.9

# Filnamn: kap. 5, sid. 67 - while-loopar, fråga efter lösenord.py

# Kapitel 5 - Loopar - upprepning, itteration
# Programmering 1 med Python - Lärobok

# Programmet frågar efter ett lösenord och fortsätter fråga tills det blir 
# rätt och då fortsätter programmet med att skriva "Välkommen, lösen ok!"

pw = input('Ange ditt lösenord: ')

while pw != 'qwe!123':
    print('Fel lösenord. Försök igen!')
    pw = input('Ange lösenord: ')

print('Välkommen, lösen ok!')