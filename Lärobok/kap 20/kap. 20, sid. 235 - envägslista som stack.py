#!/usr/local/bin/python3.9

# Filnamn: kap. 20, sid. 235 - envägslista som stack.py

# Kapitel 20 - Länkade listor och andra datastrukturer
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Exempel från boken som visar hur man skapar en stack med hjälp av en envägslista
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
    """Klass för att hantera en envägslista i form av en stack"""
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
            # Skriv ut ny nod med värde
            print("Lagt till värdet ", existingNode.value)
    
    def printList(self):
        """Skriv ut listans alla värden"""
        existingNode = self.firstNode
        while existingNode:
            print(existingNode)
            existingNode = existingNode.next

    def push(self, nn):
        """Lägger till ett nytt värde först i listan"""
        newNode = ListNode(nn) # Skapar upp en ny nod
        newNode.next = self.firstNode # Flyttar g:a värdet som låg först till nästa nod
        self.firstNode = newNode # Sätter den nya noden först i listan
    
    def pop(self):
        """Tar bort en nod i i början av listan och returnerar dess värde"""
        # Finns det något värde lagrat i listan 
        if self.firstNode == None:
            return None # Om inte returnera None
        else:
            existingNode = self.firstNode # Ta fram första noden från listan
            self.firstNode = existingNode.next # Sätt ny första nod till nästa nod 
            return existingNode.value # Returnera nodens värde som vi plockat bort
    
    def __bool__(self):
        """Tom lista ska returnera False, om noder/värden finns ska True returneras"""
        return self.firstNode != None

    def __repr__(self):
        """Skapa en representation av listan som kan användas interaktivt, t.ex. vid 
        utskrift av objektet. För att markera att det är en länkad lista skrivs 
        elementen ut med en pil mellan varje nod."""
        s ="["
        p = self.firstNode
        while p:
            s += str(p.value)
            if p.next:
                s += "->"
            p = p.next
        s += "]"
        return s

def main():
    # Skapa listhuvud utan värde
    lista = Listing()
    
    # Fråga användare om hur många värden han/hon vill mata in
    noOfValues = int(input("Hur många värden vill du mata in? "))

    # Låt användaren mata in värdena 
    for i in range(noOfValues):
        v = input("Ange värde " + str(i + 1) +": ")
        # Lägg till värdet till listan med push metod
        lista.push(v)

    # Skriv ut listans alla värden
    lista.printList()

    # Skriver ut listans kvarvarande noder/element och plockar bort dem en efter en enligt principen sist in först ut
    while lista:
        print(lista) # Anropar metoden __repr__
        print(lista.pop()) # Anropar metoden pop som i sig skriver ut värdet som plockas bort från listan    

# Här körs programmet
main()