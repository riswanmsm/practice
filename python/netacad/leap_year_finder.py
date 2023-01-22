year = int(input("Enter a year: "))

#
# Write your code here.
#
if year < 1582:
    message = "Not within the Gregorian calendar period"
elif year % 4 != 0:
    message = "Common year"
elif year % 100 != 0:
    message = "Leap year"
elif year % 400 != 0:
    message = "Common year"
else:
    message = "Leap year"
    
print(message)
