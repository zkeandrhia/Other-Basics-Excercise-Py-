'''calculating mass and obj'''

def mass():
    scientists = float(input('Enter an objects mass: '))
    weight = scientists * 9.8
    
    if weight >= 500:
        print(f'\nMass: {scientists} \nAs Weight: {weight}')
        print("It's too heavy!")
    elif weight in range(0,200):
        print(f'\nMass: {scientists} \nAs Weight: {weight}')
        print("It's too light!")
        
mass()