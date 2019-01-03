#!/usr/bin/python3.7

# Filnamn: kap. 8, sid. 100 - referenser, kopior och variablers liv.py

# Kapitel 8 - Listor och tipplar
# Programmering 1 med Python - Lärobok

# Python hanterar alla variabler som referenser
# Exempel med listor
# Skapa listan listaEtt
listaEtt = [9, 3, 7]
print(listaEtt)
# Skapa listaTvå och låt den refera till listaEtt
listaTvå = listaEtt
print(listaTvå) # Skriver ut samma innehåll som listaEtt

# Nu ändrar vi lite i listaEtt
listaEtt[0] = 1
# Skriver ut bägge listorna
print(listaEtt)
print(listaTvå) # Skriver fortfarande ut samma innehåll som listaEtt
                # vilket visar att Python refererar till samma minnespostion 
                # för den nytilldelade variabeln listaTvå

# Variablers livslängd
# I python behövs inte variabeldeklarationer, det räcker med att tilldela dem 
# någon form av värde/inehåll föratt de ska få existensberättigande

# Exempel på vad som händer när variabel saknar tilldelat värde, ta bort # 
# framför var på nästa rad. 
# var # är otilldelad och genererar felmeddelande
      # NameError: name 'var' is not defined

# Som programmerar är det god sed att tänka på att återlämna minne till 
# operativsystemet.Genom att låta variabler referera till None så talar du om 
# att de ska finnas kvar i listan med variabler men sluta referea till någon 
# minnesplats.

listaEtt = None  
listaTvå = None

print(listaEtt) # Blir en  utskrift med None som svar
# Behöver du ej längre variabelnamnen och vill frigöra dess minnesutrymme i 
# variabellistan, använd del kommandot

del listaEtt
del listaTvå

# När du tilldelar en variabel None och sålunda slutar referera till ett 
# specifikt minnesområde eller tar bort variabler frigörs perautomatik minne 
# till operativsystemet då Pythontolken nästa gång kör en sk "garbage 
# collection".

# Försöker du sedan accessa variablerna får du samma fel som om de inte var 
# definerade, se rad 32.
# print(listaEtt)