'''https://stepik.org/lesson/24463/step/6?unit=6771'''

try:
    foo()
except ZeroDivisionError as e:
    a = 'ZeroDivisionError'
    print(a)

except ArithmeticError as e:
    a = 'ArithmeticError'
    print(a)

except AssertionError as e:
    a = 'AssertionError'
    print(a)