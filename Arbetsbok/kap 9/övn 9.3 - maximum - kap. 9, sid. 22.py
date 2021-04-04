#!/usr/local/bin/python3.9

# Filnamn: övn 9.3 - maximum - kap. 9, sid. 22.py

# Funktioner
# Programmeringsövningar till kapitel 9

# Programmet returnerar det största av två angivna argument

# Funktionsdefinitioner
def maximum(x, y):        
    """ Tar reda på vilket av talen x eller y som är störst

    x : float
        Tal nr 1 som ska kontrolleras

    y : float
        Tal nr 2 som ska kontrolleras

    returvärde : float
        Returnerar det största talet av de angivna parametrarna
    """
    
    return max(x, y)
    

# Huvudprogram
def main():
    # Låt användaren mata in två tal i en lista
    tal = []
    for i in range(2):
        tal.append(float(input('Ange tal ' + str(i+1) + ': ')))
    
    störstaTalet = maximum(tal[0], tal[1])

    print('Största talet av:', tal, 'är', störstaTalet)

## Huvudprogram anropas
main()