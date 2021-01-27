'''https://stepik.org/lesson/24463/step/9?unit=6771'''

class NonPositiveError(Exception):
    pass

class PositiveList(list):
    def append(self, item):
        if item > 0:
            super(PositiveList, self).append(item)
        else:
            raise NonPositiveError


a = PositiveList()
a.append(1)
print(a)
a.append(0)
print(a)
a.append(-41)
print(a)