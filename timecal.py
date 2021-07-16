'''enter a number of seconds and works as follows:

There are 60 seconds in a minute. If the number of seconds 
entered by the user is greater than or equal to 60, the program 
should display the number of minutes in that many seconds.

- There are 3600 seconds in an hour. If the number of seconds 
entered by the user is greater than or equal to 3600, the program 
should display the number of hours in that many seconds.

- There are 86400 seconds in a day. If the number of seconds entered
by the user is greater than or equal to 86400, the program should 
display the number of days in that many seconds.
'''

def time():
    user = int(input('Enter a number of seconds: '))
    
    days = int(user / 86400)
    hours = int((user % 86400 )/3600)
    minutes = int(((user % 86400 )%3600)/60)
    seconds = int(((user % 86400 )%3600)%60)
    
    print(f'{days} day(s), {hours} hour(s), {minutes} minute(s), {seconds} second(s).')
time()