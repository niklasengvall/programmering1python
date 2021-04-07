#!/usr/local/bin/python3.9

# Filnamn: övn 4.6 - kreditvärdig - kap 4, sid. 8.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 4 - Arbetsbok

# Programmet frågar efter ålder, årsinkomst samt ev. kreditanmärkningar och 
# informerar sedan användaren om hen beviljas betala med faktura eller inte

# Skriv ut programmets rubrik
print('Kreditvärdighetskontroll')
print('========================\n')

# Fråga användaren hur gammal hen är
ålder = int(input('Ange din ålder: '))

# Fråga användaren om dennes brutto årsinkomst
årsInkomst = int(input('Ange din brutto årsinkomst: '))

# Fråga användaren om hen har någon betalningsanmärkning
anmärkning = input('Har du någon betalningsanmärkning (j/n): ')

# Kontrollera om användaren är 18 år eller äldre och om hen tjänar 120000 eller mer samt att hen inte har någon betalningsanmärkning
if ålder >= 18 and årsInkomst >= 120000 and (anmärkning == 'n' or anmärkning == 'N'):
    print('Fakturabetalning beviljad!')
else:
    print('Tyvärr kan vi inte bevilja fakturabetalning!')
