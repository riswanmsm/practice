hour = int(input("Starting time (hours): "))
mins = int(input("Starting time (minutes): "))
dura = int(input("Event duration (minutes): "))

# Write your code here.
mins_with_dura = mins + dura
end_hour = (hour + mins_with_dura // 60) % 24
end_mins = mins_with_dura % 60

print(str(end_hour) + ':' + str(end_mins))
