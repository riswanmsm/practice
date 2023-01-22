import calendar

# print(calendar.calendar(2022, m=4))
# calendar.prcal(2022) # like the above it will print the calendar without the print function
# print(calendar.month(2022,11))
# calendar.prmonth(2022, 11)
# calendar.setfirstweekday(6) # changing the first week day from monday to other
# calendar.setfirstweekday(calendar.SUNDAY) # above number can be given with the value from constant
# calendar.prmonth(2022, 12)
# print(calendar.weekday(2022, 12, 7)) # return the integer day number in week 0 - 6
# print(calendar.weekheader(9)) # change week header from Mo to Monday
# print(calendar.isleap(2020))
# print(calendar.leapdays(1952, 2025))

cal = calendar.Calendar(calendar.MONDAY)

# for weekday in cal.iterweekdays():
#     print(weekday, end = ' ')
# print()

# for date in cal.itermonthdates(2022, 12):
#     print(date, end = ' ')
# print()

# for date in cal.itermonthdays2(2022, 12):
#     print(date, end = ' ')
# print()

# for date in cal.itermonthdays3(2022, 12):
#     print(date, end = ' ')
# print()

# for date in cal.itermonthdays4(2022, 12):
#     print(date, end = ' ')
# print()

for date in cal.monthdays2calendar(2022, 12):
    print(date)

