
weight = int(input('Enter the weight to be converted? '))
unit = input('Enter current unit of the weight? K for Kg / L for Lbp ')



unit_in_upper = unit.upper()

while(unit_in_upper != 'K' and unit_in_upper != 'L'):
    print(unit_in_upper)
    print('Your input is wrong, Please enter K / L')
    unit = input('Enter current unit of the weight? K for Kg / L for Lbp ')
    unit_in_upper = unit.upper()

if(unit_in_upper == 'K'):
    print('Weight in Pounds: ' + str(weight / 0.45))
else:
    print('Weight in Killo: ' + str(weight * 0.45))

# name = input('What\' your name? ')
# color = input('What\' your favourite color? ')


# if(name.upper() == 'ASNA'):
#     name += ' My Princes' 

# print(name + ' likes ' + color)

# birth_year = int(input('What is your birth year? '))
# current_year = 2021

# age = current_year - birth_year

# print('Your age is: ' + str(age))


