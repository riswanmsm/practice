from datetime import datetime
from datetime import date

date_time = datetime(2020, 11, 4, 14, 53, 00)

print(date_time.strftime('%Y/%m/%d %H:%M:%S')) # 2020/11/04 14:53:00
print(date_time.strftime('%y/%B/%d %H:%M:%S %p')) # 20/November/04 14:53:00 PM
print(date_time.strftime('%a, %Y %b %d')) # Wed, 2020 Nov 04
print(date_time.strftime('%A, %Y %B %d')) # Wednesday, 2020 November 04
print(date_time.strftime('Weekday: %w')) # Weekday: 3
print(date_time.strftime('Day of the year: %j')) # Day of the year: 309
print(date_time.strftime('Week number of the year: %W')) # Week number of the year: 44
print("Today:", date.today()) # Displays: Today: 2022-11-06
print(date_time.day)
datetime_1 = datetime(2019, 11, 29, 11, 27, 22)
datetime_2 = datetime(2019, 11, 27, 0, 0, 0)
print(datetime_1 - datetime_2)