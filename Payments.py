'''Write a program that asks the user to enter 
the amount of a purchase and the desired number 
of payment installments. 
The program should add 5 percent to the amount
to get the total purchase amount, and then divide 
it by the desired number of installments, then display messages
telling the user the total amount of the purchase
and how much each installment will cost.'''

def installment():
    
    client = float(input('Enter the amount of purchase: '))
    cashy = int(input('Enter the desire number of payment installments: '))
    
    totalp = (client * .05) + client
    toatli = totalp / cashy
    
    print(f'\n Purchase amount = P {client}\n Number of Installations = {cashy}\n Total Purchase = P {totalp}\n Installment = P {toatli}')
installment()
    