'''https://stepik.org/lesson/24465/step/6?auth=registration&unit=6772'''
import os.path


with open("test.txt", 'w') as t:
    for current_dir, dirs, files in os.walk("C:/Users/Nameman/PycharmProjects/main"):
        for file in files:
            if file[-3:] == '.py':
                t.write(current_dir[33:] + '\n')
                break