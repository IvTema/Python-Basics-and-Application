'''https://stepik.org/lesson/24469/step/6'''
s, a, b = input(), input(), input()
counter = 0
while a in s and counter < 1000:
    counter += 1
    s = s.replace(a, b)
if counter < 1000:
    print(counter)
else:
    print('Impossible')