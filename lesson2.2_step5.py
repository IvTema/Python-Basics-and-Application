'''https://stepik.org/lesson/24466/step/5?unit=6773'''
import datetime


y, m, d = map(int, input().split())
a = datetime.date(y, m, d)
b = datetime.timedelta(days=int(input()))
c = a+b
print(c.year, c.month, c.day)