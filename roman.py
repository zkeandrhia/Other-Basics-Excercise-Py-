''' changing into roman numerals '''

def numbers():
    while True:      
        roman = int(input('Enter a number in range 1 to 5: '))
#proccess 
        if roman == 1:
            print('Roman Numeral: I')
            ask = input('Again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
        elif roman == 2:
            print('Roman Numeral: II')
            ask = input('Again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
        elif roman == 3:
            print('Roman Numeral: III')
            ask = input('Again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
        elif roman == 4:
            print('Roman Numeral: IV')
            ask = input('Again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
        elif roman == 5:
            print('Roman Numeral: V')
            ask = input('Again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
        else:
            print('Oh no, out of range!')
            ask = input('Again? y/n: ')
            if ask != 'y':
                break
            else:
                continue
numbers()