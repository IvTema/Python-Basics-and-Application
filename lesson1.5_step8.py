'''https://stepik.org/lesson/24461/step/8?auth=registration&unit=6767'''

class MoneyBox:
    def __init__(self, capacity):  # конструктор с аргументом – вместимость копилки
        self.capacity = capacity
        self.counter = 0

    def can_add(self, v): # True, если можно добавить v монет, False иначе
        return self.counter + v <= self.capacity

    def add(self, v): # положить v монет в копилку
        if self.can_add(v):
            self.counter += v


x = MoneyBox(10)
x.add(5)
x.add(3)