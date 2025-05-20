import calendar
day, month, year = input().split(".")
weekday = calendar.weekday(int(year), int(month), int(day))
weekday_name = calendar.day_name[weekday]
month = calendar.month_name[int(month)]
print(f'{weekday_name} {day} {month} {year}')