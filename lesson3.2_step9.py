'''https://stepik.org/lesson/24470/step/9'''
import sys
import re

pattern = r"z.{3}z"

for line in sys.stdin:
    line = line.rstrip()
    finder = re.search(pattern, line)
    if finder:
        print(line)