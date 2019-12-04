#!/usr/bin/python3.8

# Filnamn: övn 5.19 - skriva ut en taltriangel med siffror - kap. 5, sid. 12.py

# Programmet skriver ut 10 rader med siffror. Se nedan:

# 0 1 2 3 4 5 6 7 8 9
#   0 1 2 3 4 5 6 7 8
#     0 1 2 3 4 5 6 7
#       0 1 2 3 4 5 6
#         0 1 2 3 4 5
#           0 1 2 3 4
#             0 1 2 3
#               0 1 2
#                 0 1
#                   0

for y in range(10, 0, -1):      # Betyder att vi ska skriva ut 10 rader
    for z in range(0, 10 - y):  # Betyder att vi ska skriva ut z antal 
        print(' ', end = ' ')   # mellanslag innan siffrorna
    for x in range(0, y):       # Betyder att vi ska skriva ut y antal siffror
                                # från 0 till y
        print(x, end = ' ')
    
    # radslutstecken
    print('')