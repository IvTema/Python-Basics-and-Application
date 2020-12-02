'''https://stepik.org/lesson/24461/step/9?auth=registration&unit=6767'''

class Buffer:
    def __init__(self): # Накапливает элементы
        self.total_list = []
        self.for_print_sum = 0

    def add(self, *a): # добавляет элементы, возвращает сумму 5, если стакнулось
        self.total_list += a
        while len(self.total_list) >= 5:
            for i in range (5):
                self.for_print_sum += self.total_list[i]
            print(self.for_print_sum)
            del self.total_list[0:5]
            self.for_print_sum = 0

    def get_current_part(self): # Возвращает вакантные элементы
        return self.total_list


buf = Buffer()
buf.add(1, 2, 3)
buf.get_current_part() # вернуть [1, 2, 3]
buf.add(4, 5, 6) # print(15) – вывод суммы первой пятерки элементов
buf.get_current_part() # вернуть [6]
buf.add(7, 8, 9, 10) # print(40) – вывод суммы второй пятерки элементов
buf.get_current_part() # вернуть []
buf.add(1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1) # print(5), print(5) – вывод сумм третьей и четвертой пятерки
buf.get_current_part() # вернуть [1]