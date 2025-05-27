import calendar
try:
    day, month, year = input().split(".")
except:
    print("make sure you wrote all data correct")
    exit()
try:
    weekday = calendar.weekday(int(year), int(month), int(day))
    weekday_name = calendar.day_name[weekday]
    month = calendar.month_name[int(month)]
    print(f'{weekday_name} {day} {month} {year}')
except:
    print("error. Write day, month and year using integers")
