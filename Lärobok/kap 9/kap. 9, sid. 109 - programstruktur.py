#!/usr/bin/python3.8

# Filnamn: kap. 9, sid. 109 - programstruktur.py

# Kapitel 9 - Funktioner
# Programmering 1 med Python - Lärobok

# Proghramstruktur med funktionsanrop gör progam mer överskådliga.
# Överstskriver vi in alla funktionsdefinitioner och därefter programmets 
# huvudkod

def meny():
    """Skriver ut programmets rubrik
       
       Argument:   inga
       Returnerar: inget"""
    print('Medianberäkning')
    print('===============\n')

def matainLista():
    """Frågar användaren efter antal tal som ska matas in och låter sedan användaren mata in dem.
       
       Argument:   inga
       Returnerar: ett numeriskt listobjekt som datatypen list"""
    lista = []
    antalTal = int(input('Ange antal tal du vill mata in i listan: '))
    for i in range(antalTal):
        lista.append(float(input('Ange tal '+ str(i+1) + ': ')))
    return lista

# Beräkna och returnera medianen av en numerisk lista 
def median(lista):
    """Funktionen sorterar en given lista som angets som argument, därefter tas medianvärdet fram. 
    
       Argument:   ett numeriskt listobjekt som datatyp list
       Returnerar: medianvärdet som datatyp float"""
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

def återkoppla(median):
    """Funktionen skriver ut argumentet median på konsolen. 
    
       Argument:   medianvärde som datatyp float
       Returnerar: inget"""
    print('\nMedianen för listan är', median)

# Huvudloop för programmet, anges vanligen som main()
def main():
    """Funktionen är huvudloopen för programmet. 
    
       Argument:   inget
       Returnerar: inget"""
    lista = []
    meny()
    lista = matainLista()
    m = median(lista)
    återkoppla(m)

# Huvudprogram
main()
