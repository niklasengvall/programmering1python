#!/usr/local/bin/python3.9

# Filnamn: kap. 20, sid. 231 - envägslista som klass.py

# Kapitel 20 - Länkade listor och andra datastrukturer
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Exempel från boken som visar hur man skapar en enkel envägslista med hjälp av en klass, metoder och attribut
# Vi använder 2 klasser en för själva listnoden och en för hela listan

class ListNode:
    """Nodklass för en länkad envägslista """
    def __init__(self, v = None):
        self.value = v
        self.next = None # Betecknar att det inte finns ett värde
        
    def __str__(self):
        """Skapar en sträng av nodens datavärde"""
        return str(self.value)

class Listing:
    """Klass för att hantera en envägslista"""
    def __init__(self):
        # Refererar till första noden (1:a elementet i listan)
        self.firstNode = None
    
    def append(self, nn):
        """Metoden append används för att lägga till en ny nod (ett nytt värde (element) sist i listan"""
        newNode = ListNode(nn)
        # Är listan ny så sätter första elementet till nn
        if self.firstNode == None:
            self.firstNode = newNode
        # Annars går vi igenom existerande listans alla element och lägger till den nya nn noden sist
        else:
            existingNode = self.firstNode # Börja vid första noden (elementet)
            while existingNode.next: # Fortsätt så länge det finns värden
                existingNode = existingNode.next
            # Nu har vi nått slutet av befintlig lista (värde None) och kan lägga till värdet
            existingNode.next = newNode
    
    def printList(self):
        """Skriv ut listans alla värden"""
        existingNode = self.firstNode
        while existingNode:
            print(existingNode)
            existingNode = existingNode.next

def main():
    # Skapa listhuvud utan värde
    lista = Listing()
    
    # Fråga användare om hur många värden han/hon vill mata in
    noOfValues = int(input("Hur många värden vill du mata in? "))

    # Låt användaren mata in värdena 
    for i in range(noOfValues):
        v = input("Ange värde " + str(i + 1) +": ")
        # Lägg till värdet till listan
        lista.append(v)

    # Skriv ut listans alla värden
    lista.printList()

# Här körs programmet
main()