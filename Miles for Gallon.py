'''A car’s miles-per-gallon (MPG) can be calculated 
with the following formula:

MPG = Miles driven / Gallons of gas used

Write a program that asks the user for the number of miles 
driven and the gallons of gas used. It should calculate 
the car’s MPG and display the result.'''

def miles_pg():
    driver = int(input('Enter the number of miles driven: '))
    gallons = float(input('Enter the gallons of gas used: '))
    MPG = driver / gallons
    print(f"\n Miles droven : {driver} \n Gas used(Gallons): {gallons} \n Car's MPG : {MPG} ")
miles_pg()