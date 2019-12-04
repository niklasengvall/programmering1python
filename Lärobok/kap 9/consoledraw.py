#!/usr/bin/python3.8

# Filnamn: consoledraw.py

# Kapitel 9 - Funktioner
# Programmering 1 med Python - Lärobok

# En egen modul för att rita med asterisker på konsolen
def line(length):
    """ Draw a line with asterisks
        
        length : integer
            The length of the line as an integer

    """
    
    print(length * '*')

def filledRect(length, height):
    """ Draw a filled Rectangle

        length : integer
            Width of the rectangle

        height : integer
            Height of the rectangle
    """
    
    for row in range(0, height):
        line(length)

def main():
    """ Main routine used to test this modules function

    """
    
    print('Test to draw a line with 20 asterisks')
    line(20)
    print()
    print('Test to draw a rectangle with length 14 and height 7')
    filledRect(14, 7)

# Call this modules testfuction if this module runs alone
if __name__ == "__main__":
    main()

