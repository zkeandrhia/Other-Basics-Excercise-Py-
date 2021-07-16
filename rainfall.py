# This program averages rainfall per month.  It asks the user for the number
# of years.  It will then display the number of months, the total inches of
# rainfaill, and the average rainfall per month for the entire period.

# Get the number of years.

total_years = int(input('Enter the amount of years: '))

# Get the amount of rainfall for each month of each year.

for years in range(total_years):
    # Initialize the accumulator.
    total = 0.0
    print('Year', years + 1)
    print('----------------')
    for month in ('January:', 'February:', 'March:', 'April:', 'May:', 'June:', 'July:', 'August:', 'September:', 'October:', 'November:', 'December:'):
        inches = float(input(month))
        total += inches

total_inches = total

total_month = total_years * 12

average_inches = total / total_month



        # Display the average.
print('The total number of months is: ', total_month)
print('The total inches of rainfall is: ', total_inches)
print('The average rainfall per month for the entire period is: ', average_inches)

print()