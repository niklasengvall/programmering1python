#!/usr/bin/python3.7

# Filnamn: övn 17.1-3, sid. 41 - interaktiv test.py

# Teckentabeller
# Programmeringsövningar till kapitel 17

# Import av modul

# Funktionsdefinitioner
def ovning1():
    print('Hallå där!\a\a\a')
    print('Hej\tpå\tdej')
    print('Hej\npå\ndej')
    print('Hej\vpå\vdej')
    print('Hejsan\rhopp')
    
def ovning2():
    print('\x41\x42\x43')

def ovning3():
    for char in range(32,256):
        print(chr(char),end="")
    print()
    print('Å =', ord('Å'),'å =',ord('å'))
    print('Ä =', ord('Ä'),'ä =',ord('ä'))
    print('Ö =', ord('Ö'),'ö =',ord('ö'))
    print(chr(176))

    print()

# Huvudprogram
def main():
    # Anropa övningarna 1-2
    ovning1()
    ovning2()
    ovning3()

        
# Huvudprogram anropas 
main()