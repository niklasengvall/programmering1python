#!/usr/bin/python3.7

# Filnamn: övn 4.7 - snabbare kreditvärdighetskontroll - kap 4, sid. 8.py

# Skapa program eller skript
# Programmeringsövningar till kapitel 4 - Arbetsbok

# Programmet frågar efter ålder, årsinkomst samt ev. kreditanmärkningar och 
# informerar användaren om hen beviljas betala med faktura eller inte direkt
# efter respektive fråga där svaret inte uppfyller vilkoren

# Skriv ut programmets rubrik
print('Snabbare kreditvärdighetskontroll')
print('=================================\n')

# Fråga användaren hur gammal hen är
# om användaren är yngre än arton avslutas if-satsen och 
# och hen får meddelande om att fakturabetalning ej beviljas
if int(input('Ange din ålder: ')) < 18:
    print('Tyvärr kan vi inte bevilja fakturabetalning!')
# Om hen är 18 år eller mer så frågar vi efter brutto års-
# inkomsten och om den är mindre än 120000 avslutas if-satsen 
# och hen får meddelande om att fakturabetalning ej beviljas
elif int(input('Ange din brutto årsinkomst: ')) < 120000:
    print('Tyvärr kan vi inte bevilja fakturabetalning!')
# Om hen har en bruttoårsinkomst på 120 000 ellermer så frågar vi om 
# hen har någon betalningsanmärkning, svarar hen j avslutas if-satsen 
# och hen får meddelande om att fakturabetalning ej beviljas
elif input('Har du någon betalningsanmärkning (j/n): ') == 'j':
    print('Tyvärr kan vi inte bevilja fakturabetalning!')
# Har alla vilkor uppfyllts ovan så beviljas fakturabetalning
else:
    print('Fakturabetalning beviljad!')