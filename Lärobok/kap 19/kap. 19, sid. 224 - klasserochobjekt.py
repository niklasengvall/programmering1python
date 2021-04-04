#!/usr/local/bin/python3.9

# Filnamn: kap. 19, sid. 224 - klasserochobjekt.py

# Kapitel 19 - Klasser och objekt
# Programmering 1 med Python - Lärobok

# Kodexempel från boken med förklaringar

# Exempel från boken som visar hur man skapar klasser och metoder och hur de används

class Person:
    """Klass för att hantera personers adressuppgifter och saldo i ett register"""

    # Initieringsmetod som anropas när vi skapar objekt av klassen, första parametern ska kallas self
    # Dataattributen ska innuti klassen också refereras till self, vilket innebär att de blir unika för varje objekt
    def __init__(self, name = "John Doe", address ="Unknown", mobile = "?", balance = 0):
        self.name = name
        self.address = address
        self.mobile = mobile
        self.balance = balance
    
    # Metod för att skriva ut klassens dataattribut (medlemmar)
    def skrivut(self):
        print("Namn: {}\nAdress: {}\nMobil: {}\nSaldo: {:.2f}\n\n".format(self.name, self.address, self.mobile, self.balance))

    # Reserverad metod som skriver ut objektets dataattribut i strängformat separerat med semikolon
    def __str__(self):
        return (self.name+";"+self.address+";"+self.mobile+";"+str(self.balance))

# Skapar 2 objekt (instanser) av klassen Person, det först med givna attribut, det andra får initieras per default
customer1 = Person("Pelle Andersson","Testvägen 1, 123 45 Någonstad", "070-123 45 67", 1445667)
customer2 = Person()

# Skriver ut objektens dataattribut via klassmetoden skrivut
customer1.skrivut()
customer2.skrivut()
# Skriver ut klassens docstring
print(customer1.__doc__)
# Skriver ut objektets attribut vis metoden __str__
print(customer1)