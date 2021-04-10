#!/usr/bin/python3

# Filnamn: övn 19.1, sid. 44 - bilar.py

# Klasser och objekt
# Programmeringsövningar till kapitel 19

# I den här övningen ska vi definiera en klass för bilar med några attibut och 
# metoder.
# Vi börjar med att skapa ett så kallat klassdiagram, därefter tar vi klass-
# definitionen och till sist gör vi ett huvudprogram som kör runt några fordon
# till olika positioner i ett koordinatsystem.

# K L A S S D I A G R A M

# +-----------------------------+
# |  Bilar                      |
# +-----------------------------+
# |  _farg (str)                |
# |  _typ (str)                 |
# |  _motoreffekt (int)         |  
# |  _igang (bool)              |
# |  _position (List)           |
# +-----------------------------+
# |  Starta()                   |
# |  Stanna()                   |
# |  KorTillPosition(position)  |
# |  AvlasPosition()            |
# +-----------------------------+

class Bilar:
    """Klass för att hantera bilar av olika slag, färg, typ, motoreffekt och om de är igång samt vilken position de har."""

    # Initieringsmetod som anropas när vi skapar objekt av klassen, första parametern ska kallas self
    # Dataattributen ska innuti klassen också refereras till self, vilket innebär att de blir unika för varje objekt
    def __init__(self, f = "Okänd", t = "Okänd", m = 0, i = False, p = [0,0]):
        """Klassinitiering: Nytt objekt är skapat av klassen Bilar."""
        self._farg = f
        # TODO: Felhantering här, endast tillåtna typer är personbil, kombi, pickup, van eller lastbil
        if t in ["Personbil", "Kombi", "Pickup", "Van", "Lastbil"]:
            self._typ = t
        else:
            print("Biltyp felaktig eller okänd! Bör sättas till någon av de tillåtna typerna personbil, kombi, pickup, van eller lastbil.")
            self._typ = "Okänd"
            
        self._motoreffekt = m
        self._igang = i
        self._position = p
        # Skriv ut att objekt av klassen med attribut är skapat
        print("Objekt av klassen " + str(self.__class__) + " med attributen " + str(self) + " är skapat.")

    # Metoden Starta ändrar attributet _igang till True, dvs. bilen är igång
    def Starta(self):
        """Metoden Starta ändrar attributet _igang till True, dvs. bilen är igång """
        self._igang = True

    # Metoden Stanna ändrar attributet _igang till False, dvs. bilen är avslagen
    def Stanna(self):
        """Metoden Stanna ändrar attributet _igang till False, dvs. bilen är avslagen """
        self._igang = False

    # Metoden KorTillPosition ändrar attributet _Position (x, y koordinater angivet i en lista)
    def KorTillPosition(self, position):
        """Metoden KorTillPosition ändrar attributet _Position (x, y koordinater angivet i en lista) """
        self._position = position

    # Metoden AvlasPosition returnerar attributet _Position (x, y koordinater angivet i en lista)
    def AvlasPosition(self):
        """Metoden AvlasPosition returnerar attributet _Position (x, y koordinater angivet i en lista) """
        return self._position

    # Reserverad metod som skriver ut objektets dataattribut i strängformat separerat med semikolon
    def __str__(self):
        """Metoden __str__ skriver ut objektets dataattribut i strängformat separerat med semikolon """
        return (self._farg + ";" + self._typ + ";" + str(self._motoreffekt) + ";" + str(self._igang) + ";" + str(self._position))


def main():
    # Skapar 6 objekt (instanser) av klassen Bilar, det första initieras per default och de andra får värden
    # personbil, kombi, pickup, van eller lastbil
    b1 = Bilar()
    b2 = Bilar("Röd", "Personbil", 51, False, [10,5])
    b3 = Bilar("Grön", "Kombi", 112, False, [5,0])
    b4 = Bilar("Svart", "Pickup", 141, False, [0,5])
    b5 = Bilar("Blå", "Van", 110, False, [10,10])
    b6 = Bilar("Gul", "Lastbil", 103, False, [0,0])
    b7 = Bilar("Rosa", "Cykel", 103, False, [1,1])

    # Starta några bilar, alla utom b1 och b7
    b2.Starta()
    b3.Starta()
    b4.Starta()
    b5.Starta()
    b6.Starta()

    #Flytta några bilar, närmare bestämt b3-b5
    b3.KorTillPosition([10,3])
    b4.KorTillPosition([5,5])
    b5.KorTillPosition([0,0])

    # Avläs de nya positionerna för de 3 flyttade bilarna
    print("Bil b3, ny position: {}".format(b3.AvlasPosition()))
    print("Bil b4, ny position: {}".format(b4.AvlasPosition()))
    print("Bil b5, ny position: {}".format(b5.AvlasPosition()))
    
    # Stanna alla startade bilar
    b2.Stanna()
    b3.Stanna()
    b4.Stanna()
    b5.Stanna()
    b6.Stanna()

    # Skriver ut objektets attribut via metoden __str__
    print(b1)
    print(b2)
    print(b3)
    print(b4)
    print(b5)
    print(b6)
    print(b7)

    # Skriver ut objektets docstring för både klass och alla metoder
    print(b2.__doc__)
    print(b2.__init__.__doc__)
    print(b2.Starta.__doc__)
    print(b2.Stanna.__doc__)
    print(b2.KorTillPosition.__doc__)
    print(b2.AvlasPosition.__doc__)
    print(b2.__str__.__doc__)

    # Ta bort objekten från minnet
    del b1
    del b2
    del b3
    del b4
    del b5
    del b6
    del b7

# Här körs programmet
main()