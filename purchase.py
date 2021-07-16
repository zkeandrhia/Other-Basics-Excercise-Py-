'''Customer = purchasing five items. 
program = asks for the price of each item
= displays the subtotal of the sale,
the amount of sales tax == 7%, and the total.'''

def purchase():
    shop1 = float(input('Item 1: '))
    shop2 = float(input('Item 2: '))
    shop3 = float(input('Item 3: '))
    shop4 = float(input('Item 4: '))
    shop5 = float(input('Item 5: \n'))
    
    while True:
        subtotal = (shop1 + shop2 + shop3 + shop4 + shop5)
        tax = 0.07 * subtotal
        total = subtotal + tax
        print(f' Subtotal: P{subtotal}\n Tax: P{tax} \n Total: P{total} ')
        break
purchase()
