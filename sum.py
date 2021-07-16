def sum():
    
    total = 0
    
    user = float(input('Negative number to exit, Positive number to proceed: '))
    while user > -1:
        total = total + user
        user = float(input('Enter a positive number: '))
        
    print(f'Total: {total}')
sum()