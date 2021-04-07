#!/usr/local/bin/python3.9

# Filnamn: övn 17.5-6, sid. 41 - teckensträng på binär form.py

# Teckentabeller
# Programmeringsövningar till kapitel 17

# Import av modul

# Funktionsdefinitioner
def ovning5_6():
    tecken = [0b1010000, 0b1010010, 0b1001111, 0b1000111, 0b1010010, 0b1000001,
              0b1001101, 0b1001101, 0b1000101, 0b1010010, 0b1000001]

    for c in range(0,len(tecken)):
        print(chr(tecken[c]), end = '')

# Huvudprogram
def main():
    # Anropa övningarna 1-2
    ovning5_6()
    # ovning6()

        
# Huvudprogram anropas 
main()