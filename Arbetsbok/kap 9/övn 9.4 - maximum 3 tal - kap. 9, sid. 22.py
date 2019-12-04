#!/usr/bin/python3.8

# Filnamn: övn 9.4 - maximum 3 tal - kap. 9, sid. 22.py

# Funktioner
# Programmeringsövningar till kapitel 9

# Programmet returnerar det största av tre angivna argument

# Funktionsdefinitioner
def maximum(x, y, z):        
    """ Tar reda på vilket av talen x,y eller z som är störst

    x : float
        Tal nr 1 som ska kontrolleras

    y : float
        Tal nr 2 som ska kontrolleras

    z : float
        Tal nr 2 som ska kontrolleras

    returvärde : float
        Returnerar det största talet av de angivna parametrarna
    """
    
    # return max(x, y, z) # En smartare lösning då funktionen är inbyggd 
    tal = [x, y, z]
    störst = tal[0]
    for i in range(3):
        if tal[i] > störst:
            störst = tal[i]
    return störst

# Huvudprogram
def main():
    # Låt användaren mata in tre tal i en lista
    tal = []
    for i in range(3):
        tal.append(float(input('Ange tal ' + str(i+1) + ': ')))
    
    störstaTalet = maximum(tal[0], tal[1], tal[2])

    print('Största talet av:', tal, 'är', störstaTalet)

## Huvudprogram anropas
main()