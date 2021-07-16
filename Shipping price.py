def shipping_charges():
    user = int(input('Enter the weight(lbs) of the package: '))
    
    if user <= 2:
        print("$1.00")
    elif user >2 and user <=6:
        print("$3.00")
    elif user >6 and user <=8:
        print("$4.00")
    elif user >=10:
        print("$4.75")
shipping_charges()