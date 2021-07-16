'''which rect has a greater area'''

def area():
# rect 1
    landerL = float(input('Rectangle 1 (length): '))
    landerW = float(input('Rectangle 1 (width): '))
# rect 2   
    landerL_2 = float(input('Rectangle 2 (length): '))
    landerW_2 = float(input('Rectangle 2 (width): '))
#area computation
    rect_area = landerL * landerW
    rect_are2 = landerL_2 * landerW_2
#comparison
    if rect_area > rect_are2:
        print('\nMoment of Truth: ')
        print(f'\nRectangle 1, area {rect_area} is greater than Rectangle 2, area {rect_are2}. ')
    else:
        print('Moment of Truth: ')
        print(f'\nRectangle 2, area {rect_are2} is greater than Rectangle 1, area {rect_area}. ')
area()