#!/usr/bin/python3

# Filnamn: övn 5.14 - while-loopar, fråga efter lösenord med avbryt funktion, kap. 5, sid. # 11.py

# Programmet frågar efter ett lösenord och tjatar på användaren tills det blir 
# rätt eller att hen avbryter med ENTER och då fortsätter programmet med att 
# antingen skriva "Lösen ok!" eller "Inloggning avbruten!"

psw = input('Ange lösenord (Enter avbryter): ')

while psw != 'asd14x':  # Kör loop så länge inte lösen asd14x angetts
    if psw != '':       # Om lösenordet inte endast är ett Enter, skriv ut 
                        # felmeddelande samt låt användaren ange ett nytt 
                        # lösenord 
        print('Felaktigt lösenord. Försök igen!')
        psw = input('Ange lösenord (Enter avbryter): ')
    else:
        break           # Om lösenordet endast består av ett Enter
                        # avbryts loopen

# Villkor för att ge rätt utmatning beroende på om lösenordet är korrekt 
# angivet eller om endast Enter tryckts ned
if psw != '':           
    print('Lösen ok!')
else:
    print('Inloggnings avbruten')



