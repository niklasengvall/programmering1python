#!/usr/bin/python3.7

# Filnamn: övn 9.5 - nettopris - kap. 9, sid. 22.py

# Funktioner
# Programmeringsövningar till kapitel 9

# Programmet beräknar ett rabatterat nettopris beroende på bruttoprisets 
# storlek.

# Funktionsdefinitioner
def nettoPris(bruttoPris):        
    """ Beräknar ett eventuellt rabatterat nettopris utifrån givet bruttopris.

        Om bruttopris är >= 1000 kr, dras 5 % i rabatt på bruttopriset.
        Om bruttopris är >= 500 kr och < 1000 kr, dras 2 % i rabatt på bruttopriset.
        Om bruttopris är < 500 kr, dras ingen rabatt på bruttopriset.

        bruttopris: float
            Pris som ska kontrolleras och ev. bli rabatterat

        returvärde : float
            Returnerar nettopris med eventuell rabatt.
    """
    # Rabattkontoll
    if bruttoPris >= 1000:
        rabatt = 0.05       # Rabattsats 5 %
    elif bruttoPris >= 500:
        rabatt = 0.02       # Rabattsats 2 %
    else:
        rabatt = 0.0

    return (1 - rabatt) * bruttoPris 

# Huvudprogram
def main():
    
    # Variableinitieringar där priser tilldelas värden av typen float
    dator = 9995.0
    tangentbord = 795.0
    mus = 495.0

    # Formaterad utskrift med två decimaler, kronor och ören.
    print('Datorns bruttopris är {0:.2f} kr och då blir nettopriset {1:.2f} kr.'.format(dator, nettoPris(dator)))
    print('Tangentbordets bruttopris är {0:.2f} kr och då blir nettopriset {1:.2f} kr.'.format(tangentbord, nettoPris(tangentbord)))
    print('Musens bruttopris är {0:.2f} kr och då blir nettopriset {1:.2f} kr.'.format(mus, nettoPris(mus)))
    
## Huvudprogram anropas
main()