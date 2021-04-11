#!/usr/local/bin/python3.9

# Filnamn: kap. 20, sid. 229 - envägslista.py

# Kapitel 20 - Länkade listor och andra datastrukturer
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Exempel från boken som visar hur man skapar en enkel envägslista med hjälp av en nodklass

class ListNode:
    """Nodklass för en länkad envägslista """
    def __init__(self, v = None):
        self.value = v
        self.next = None
    def __str__(self):
        """Skapar en sträng av nodens datavärde"""
        return str(self.value)

def append(oldlist, newnode):
    """Funktionen append används för att lägga till ett värde sist i listan"""
    node = oldlist
    while node.next: #
        node = node.next
    # Nu har vi nått slutet av befintlig lista
    node.next = newnode

def printlist(lista):
    """Skriv ut listans alla värden"""
    node = lista
    while node:
        print(node)
        node = node.next

def main():
    # Skapa listhuvud utan värde
    lista = ListNode()
    noOfValues = int(input("Hur många värden vill du mata in? "))

    for i in range(noOfValues):
        v = input("Ange värde " + str(i + 1) +": ")
        if not lista.value:
            # Om listan är tom, lägg in värdet i listhuvudet
            lista.value = v
        else:
            # Skapa ett nytt nodobjekt och lägg till i listan.
            newList = ListNode(v)
            append(lista, newList)
    printlist(lista)

# Här körs programmet
main()