'''https://stepik.org/lesson/24462/step/9?auth=registration&unit=6768'''

import time

class Loggable:
    def log(self, msg):
        print(str(time.ctime()) + ": " + str(msg))

class LoggableList(list, Loggable):
    def append(self, item):
        super(LoggableList, self).append(item)
        x = self[-1]
        Loggable.log(self, x)


a = LoggableList()
a.append('six')