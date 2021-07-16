'''Write a program that asks the user for the 
number of males and the number of females 
registered in a class. The program should display
the percentage of males and females in the class.

Hint: Suppose there are 8 males and 12 females
in a class. There are 20 students in the class.
The percentage of males can be calculated as
8 / 20 = 0.4, or 40%. The percentage of females
can be calculated as 12 / 20 = 0.6, or 60%.'''

def class_member():
    teacher = float(input('Class number: '))
    adviser = float(input('Male: '))
    adviser2 = float(input('Female: '))
    
    male = adviser / teacher
    female = adviser2 / teacher
    
    male2 = int(male * 100)
    female2 = int(female * 100)
    print(f'\nNumber of student: {teacher} \nPercentage of male in class: {male} or {male2}%\nPercentage of female in class: {female} or {female2}%\n')
    
class_member()