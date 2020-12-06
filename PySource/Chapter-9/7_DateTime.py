from datetime import datetime

# t_now = datetime.datetime.now() 
t_now = datetime.now()

weekday_short = t_now.strftime("%a")
weekday_full = t_now.strftime("%A")

month_numberd_and_year_numbered = t_now.strftime("%m %y")
dddd = t_now.strftime("%p %M %j")

print(weekday_short)
print(weekday_full)
print(dddd)

year = t_now.year
month = t_now.month
day = t_now.day
hour = t_now.hour 
minute = t_now.minute 
second = t_now.second

print(year)
print(month)
print(day)
print(hour)
print(minute)
print(second)
print(t_now)