import datetime
t = datetime.time(5,22,1)
print(t)
print(t.hour)
print(t.minute)

print(datetime.time.min)
print(datetime.time.max)


today = datetime.date.today()
print(today)
print(today.timetuple())
print(today.year)
print(today.month)

d1 = datetime.date(2014,3,13)
print(d1)

d2 = d1.replace(year=1990)
print(d2)