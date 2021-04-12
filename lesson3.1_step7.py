'''https://stepik.org/lesson/24469/step/7'''
s = input()
t = input()
counter = 0
for i in range(len(s)):
    if s.find(t, i) != -1 and s[i:].find(t) == 0:
        counter += 1
print(counter)