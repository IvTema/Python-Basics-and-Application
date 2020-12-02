'''https://stepik.org/lesson/24458/step/9?auth=registration&unit=6765'''

objects = [1, 2, 1, 2, 3]
a = []
ans = 0
for obj in objects: # доступная переменная objects
    if obj not in a:
        ans += 1
        a += [obj]
print(ans)