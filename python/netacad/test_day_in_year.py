def is_year_leap(year):
    #
    # Your code from the previous LAB.
    #
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def days_in_month(year, month):
    #
    # Your code from the previous lab.
    #
    if month in [1,3,5,7,8,10,12]:
        return 31
    elif month in [4,6,9,11]:
        return 30
    elif month == 2:
        if is_year_leap(year):
            return 29
        else:
            return 28
    else:
        return

def day_of_year(year, month, day):
    #
    # Write your new code here.
    #
    for current_month in range(1, month):
        day += days_in_month(year, current_month)
    return day

test_years = [1900, 2000, 2016, 1987]
test_months = [2, 2, 3, 11]
test_days = [12, 29, 5, 24]
test_results = [43, 60, 65, 328]

for i in range(len(test_results)):
    test_year = test_years[i]
    test_month = test_months[i]
    test_day = test_days[i]
    expected_result = test_results[i]
    observed_result = day_of_year(test_year, test_month, test_day)
    if observed_result == expected_result:
        print(test_year, '->', test_month, '->', test_day, '->', 'PASS')
    else:
        print(test_year, '->', test_month, '->', test_day, '->', 'FAILED')
    


