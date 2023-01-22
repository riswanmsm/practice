temps = [[0.0 for h in range(24)] for d in range(31)]
#
# The matrix is magically updated here.
#

# find the highest temperature in the month 
highest = -100.0
 
for day in temps:
    for temp in day:
        if temp > highest:
            highest = temp
 
print("The highest temperature was:", highest)

# find the number of hot days in the month
hot_days = 0
 
for day in temps:
    if day[11] > 20.0:
        hot_days += 1
 
print(hot_days, "days were hot.")