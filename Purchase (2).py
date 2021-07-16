'''sells a package that retails for $99. Quantity discounts are given according to the following table:

Quantity      Discount
10–19          10% 
20–49          20% 
50–99          30%
100 or more    40%
asks the user to enter the number of packages purchased.The program should then display the 
amount of the discount (if any) and the total amount of the purchase after the discount.
'''
def sales():
    
    buyer = float(input('Enter the number of packages purchased: '))
    
    if buyer > 9 and buyer < 20:
        discount = float((99 / 100 )* 10)
        package = float(99 - discount )
        print(f'\nPurchase Package: {buyer}\nDiscount: ${discount} \nTotal: ${package}')
    elif buyer > 19 and buyer < 50:
        discount = float((99 / 100 )* 20)
        package = float(99 - discount )
        print(f'\nPurchase Package: {buyer}\nDiscount: ${discount} \nTotal: ${package}')
    elif buyer > 49 and buyer < 100:
        discount = float((99 / 100 )* 30)
        package = float(99 - discount ) 
        print(f'\nPurchase Package: {buyer}\nDiscount: ${discount} \nTotal: ${package}')
    elif buyer > 99:
        discount = float((99 / 100 )* 40)
        package = float(99 - discount )
        print(f'\nPurchase Package: {buyer}\nDiscount: ${discount} \nTotal: ${package}')
sales()