import calendar as cal

class MyCalendar(cal.Calendar):

    def count_weekday_in_year(self, year, weekday):
        number_of_days = 0
        for i in range(1, 13):
            lst_month = self.monthdays2calendar(year, i)
            for days in lst_month:
                if days[weekday][0] != 0:
                    number_of_days += 1
        return number_of_days

my_cal = MyCalendar()
number_of_days = my_cal.count_weekday_in_year(2000, 6)
print(number_of_days)


