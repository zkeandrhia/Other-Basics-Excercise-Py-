'''On a roulette wheel, the pockets are numbered from 
0 to 36. The colors of the pockets are as follows:

- Pocket 0 is green.
- For pockets 1 through 10, the odd-numbered pockets 
are red and the even-numbered pockets are black.
- For pockets 11 through 18, the odd-numbered pockets
are black and the even-numbered pockets are red.
- For pockets 19 through 28, the odd-numbered pockets
are red and the even-numbered pockets are black.
- For pockets 29 through 36, the odd-numbered pockets
are black and the even-numbered pockets are red.

Write a program that asks the user to enter a 
pocket number and displays whether the pocket is green,
red, or black. The program should display an 
error message if the user enters a number that is 
outside the range of 0 through 36.
'''

def color_wheel():
    
    player = int(input("Enter a pocket number: "))
    
    if player > 0 and player < 11:
        if player %2 == 1:
            print('red')
        else:
            print('black')
    if player > 11 and player < 18:
        if player %2 == 1:
            print('black')
        else:
            print('red')
    if player > 19 and player < 28:
        if player %2 == 1:
            print('red')
        else:
            print('black')
    if player > 19 and player < 28:
        if player %2 == 1:
            print('black')
        else:
            print('red')
    if player > 28 and player < 36:
        if player %2 == 1:
            print('black')
        else:
            print('red')
    elif player == 0:
        print('green')
color_wheel()
    