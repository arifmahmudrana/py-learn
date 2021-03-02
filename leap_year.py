year = int(input('Give a year to find leap year: '))

if year % 4:
    print('Not a leap year')
elif year % 100 is 0 and year % 400:
    print('Not a leap year')
else:
    print('Leap year')
