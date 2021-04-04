#!/usr/local/bin/python3.9

# Filnamn: kap. 9, sid. 109 - returvärde.py

# Kapitel 9 - Funktioner
# Programmering 1 med Python - Lärobok

# Funktioner med returvärde 

# Beräkna och returnera medianen av en numerisk lista 
def median(lista):
    # Vi börjar med att sortera listan för att hitta det mellersta värdet 
    lista.sort() # sort() är en inbyggd metod/funktion i Python
    # Är det ett udda eller jämt antal numeriska argument så ska medianen tas 
    # fram på olika sätt
    if len(lista) % 2:
        # Index måste vara av typen heltal när jag sedan använder det som 
        # argument till lista, därav heltalsdivision
        index = len(lista) // 2      # För att få fram index för mellersta talet
        median = float(lista[index]) # Hämta median värdet
    else:
        # Är listan jämn i antal måste en medelberäkning ske på de två 
        # mellersta talen
        index = (len(lista) // 2)-1 # För att få fram index för det första talet
        median = float((lista[index] + lista[index + 1]) / 2)
    return median

# Huvudprogram
listaEtt = [4, 5, 6] 
listaTvå = [3, 5, 7, 9] 
print('Medianen för listaEtt:', listaEtt, 'är', median(listaEtt))
print('Medianen för listaTvå:', listaTvå, 'är', median(listaTvå))
