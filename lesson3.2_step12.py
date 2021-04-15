'''https://stepik.org/lesson/24470/step/12'''
import sys
import re

pattern = r"human"

for line in sys.stdin:
    line = line.rstrip()
    finder = re.sub(pattern, 'computer', line)
    print(finder)